package in.aaho.android.ownr.common;

import android.app.Application;
import android.content.SharedPreferences;
import android.preference.PreferenceManager;
import android.util.Log;

import com.amazonaws.auth.AWSCredentials;
import com.amazonaws.mobileconnectors.s3.transferutility.TransferUtility;
import com.amazonaws.services.s3.AmazonS3;
import com.amazonaws.services.s3.AmazonS3Client;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.toolbox.Volley;

import org.acra.ACRA;
import org.acra.annotation.ReportsCrashes;
import org.acra.sender.HttpSender;
import org.json.JSONException;
import org.json.JSONObject;

import in.aaho.android.ownr.requests.AWSCredentialsRequest;

/**
 * Created by mani on 2/7/16.
 */

@ReportsCrashes(
        httpMethod = HttpSender.Method.PUT,
        reportType = HttpSender.Type.JSON,
        formUri = "http://aaho.in:5984/acra-aaho/_design/acra-storage/_update/report",
        formUriBasicAuthLogin = "shobhit",
        formUriBasicAuthPassword = "optimus"
)
public class MainApplication extends Application {
    private final String TAG = getClass().getSimpleName();
    private static String AWS_ACCESS_KEY;
    private static String AWS_ACCESS_SECRET_KEY;

    public static void setAwsAccessKey(String key){
        AWS_ACCESS_KEY = key;
    }

    public static void setAwsAccessSecretKey(String key){
        AWS_ACCESS_SECRET_KEY = key;
    }

    public static String getAwsAccessKey(){
        return AWS_ACCESS_KEY;
    }
    public static String getAwsAccessSecretKey(){
        return AWS_ACCESS_SECRET_KEY;
    }



    public static final AWSCredentials awsCredentials = new AWSCredentials() {
        @Override
        public String getAWSAccessKeyId() {
            return getAwsAccessKey();
        }

        @Override
        public String getAWSSecretKey() {
            return getAwsAccessSecretKey();
        }
    };

    private static MainApplication instance = null;
    private static SharedPreferences prefs = null;
    private static AmazonS3 s3 = null;
    private static TransferUtility transferUtility = null;
    private static RequestQueue requestQueue = null;

    public void getAWSCredentials(){
        AWSCredentialsRequest awsCredentialsRequest = new AWSCredentialsRequest(new AWSCredentialsListener());
        if(Utils.isNetworkConnected(this)) {
            MainApplication.queueRequest(awsCredentialsRequest);
//            if (progress) {
//                showProgress();
//            }
        } else {
            Utils.toast("Please check your internet connection!");
        }
    }
    private class AWSCredentialsListener extends ApiResponseListener {

        @Override
        public void onResponse(JSONObject response) {
            try {
                if (response != null && response.getString("status")
                        .equalsIgnoreCase("success")) {
                    if(response.has("data")){
                        Log.d(TAG, "AWS Credentials received and set");
                        JSONObject data = response.getJSONObject("data");
                        setAwsAccessKey(Utils.get(data, "AWS_ACCESS_KEY"));
                        setAwsAccessSecretKey(Utils.get(data, "AWS_ACCESS_SECRET_KEY"));
                    }
                }
            } catch (JSONException e) {
                e.printStackTrace();
                Utils.toast("Unable to fetch AWS Credentials!");
            }
        }
        @Override
        public void onError() {

        }
    }

    public void setPostLoginMainAppFields(){
        getAWSCredentials();
        s3 = new AmazonS3Client(awsCredentials);
        transferUtility = new TransferUtility(s3, this.getApplicationContext());
    }

    @Override
    public void onCreate() {
        super.onCreate();
        requestQueue = Volley.newRequestQueue(this.getApplicationContext());
        ACRA.init(this);
        instance = this;
        prefs = PreferenceManager.getDefaultSharedPreferences(this.getApplicationContext());
//        s3 = new AmazonS3Client(awsCredentials);
//        transferUtility = new TransferUtility(s3, this.getApplicationContext());
        Auth.setPersistentCookieStore();

    }

    public static SharedPreferences getPrefs() {
        return prefs;
    }

    public static MainApplication getInstance() {
        return instance;
    }

    public static AmazonS3 getS3() {
        return s3;
    }

    public static TransferUtility getTransferUtility() {
        return transferUtility;
    }

    public static void queueRequest(Request<?> request) {
        requestQueue.add(request);
    }
}