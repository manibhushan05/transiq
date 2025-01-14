package in.aaho.android.driver.tracking;

import android.Manifest;
import android.content.Context;
import android.content.pm.PackageManager;
import android.location.GpsStatus;
import android.location.Location;
import android.location.LocationListener;
import android.location.LocationManager;
import android.os.Bundle;
import android.support.v4.app.ActivityCompat;
import android.util.Log;


public class MixedPositionProvider extends BasePositionProvider implements LocationListener, GpsStatus.Listener {

    private static int FIX_TIMEOUT = 30 * 1000;

    private LocationListener backupListener;
    private long lastFixTime;

    private boolean updating = false;

    public MixedPositionProvider(Context context, PositionListener listener) {
        super(context, listener);
    }

    public void startUpdates() {
        StatusDialog.addMessage("Starting mixed provider updates");
        if (!updating) {
            updating = true;
            lastFixTime = System.currentTimeMillis();
            addGpsListener();
            try {
                requestUpdates(LocationManager.GPS_PROVIDER, this);
            } catch (IllegalArgumentException e) {
                Log.w(TAG, e);
            }
        }
    }

    private void addGpsListener() {
        if (ActivityCompat.checkSelfPermission(context, Manifest.permission.ACCESS_FINE_LOCATION) != PackageManager.PERMISSION_GRANTED) {
            StatusDialog.addMessage("Permissions not available");
            return;
        }
        locationManager.addGpsStatusListener(this);
    }

    public void stopUpdates() {
        if (updating) {
            updating = false;
            removeUpdates(this);
            locationManager.removeGpsStatusListener(this);
            stopBackupProvider();
        }
    }

    private void startBackupProvider() {
        Log.i(TAG, "backup provider start");
        if (backupListener == null) {
            backupListener = new BackupLocationListener();
            requestUpdates(LocationManager.NETWORK_PROVIDER, backupListener);
        }
    }

    private class BackupLocationListener implements LocationListener {
        @Override
        public void onLocationChanged(Location location) {
            Log.i(TAG, "backup provider location");
            updateLocation(location);
        }

        @Override
        public void onStatusChanged(String s, int i, Bundle bundle) {
        }

        @Override
        public void onProviderEnabled(String s) {
        }

        @Override
        public void onProviderDisabled(String s) {
        }
    }

    private void stopBackupProvider() {
        Log.i(TAG, "backup provider stop");
        if (backupListener != null) {
            removeUpdates(backupListener);
            backupListener = null;
        }
    }

    @Override
    public void onLocationChanged(Location location) {
        Log.i(TAG, "provider location");
        stopBackupProvider();
        lastFixTime = System.currentTimeMillis();
        updateLocation(location);
    }

    @Override
    public void onStatusChanged(String provider, int status, Bundle extras) {
    }

    @Override
    public void onProviderEnabled(String provider) {
        Log.i(TAG, "provider enabled");
        stopBackupProvider();
    }

    @Override
    public void onProviderDisabled(String provider) {
        Log.i(TAG, "provider disabled");
        startBackupProvider();
    }

    @Override
    public void onGpsStatusChanged(int event) {
        if (backupListener == null && System.currentTimeMillis() - (lastFixTime + period) > FIX_TIMEOUT) {
            startBackupProvider();
        }
    }

}
