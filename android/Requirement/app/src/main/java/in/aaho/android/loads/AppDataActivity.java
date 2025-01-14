package in.aaho.android.loads;

import android.content.Intent;
import android.util.Log;

import org.json.JSONObject;


import in.aaho.android.loads.common.ApiResponseListener;
import in.aaho.android.loads.common.BaseActivity;
//import in.aaho.android.requirement.booking.App;

/**
 * Created by aaho on 18/04/18.
 */


public class AppDataActivity extends BaseActivity {


    private void startLandingActivity() {
        Log.e("[LoginActivity]", "startLandingActivity");
        startActivity(new Intent(this, LandingActivity.class));
        finish();
    }

    protected void fetchData(boolean showProgessBar) {
        startLandingActivity();
        //AppDataRequest appDataRequest = new AppDataRequest(new AppDataResponseListener());
        //queue(appDataRequest, showProgessBar);
    }

    private class AppDataResponseListener extends ApiResponseListener {

        @Override
        public void onResponse(JSONObject response) {
            dismissProgress();
            String resp = response.toString();
            Log.e("[APP DATA REQUEST]", resp);
            //try {
                //App.createAppData(resp);
                startLandingActivity();
//            } catch (JSONException e) {
//                e.printStackTrace();
//                toast("error fetching data");
//            }
        }

        @Override
        public void onError() {
            dismissProgress();
        }
    }

}

