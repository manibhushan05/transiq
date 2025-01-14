package in.aaho.android.ownr.requests;

import android.app.ProgressDialog;
import android.content.Intent;
import android.util.Log;
import android.view.View;

import com.android.volley.DefaultRetryPolicy;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONException;
import org.json.JSONObject;

import in.aaho.android.ownr.transaction.TransactionActivity;

/**
 * Created by mani on 19/8/16.
 */
public class CancelTransactionRequest {
    public static void cancelTransaction(final View v, String transactionID) {
        final ProgressDialog pDialog = new ProgressDialog(v.getContext());
        pDialog.setMessage("Loading...");
        pDialog.show();
        JSONObject obj = new JSONObject();
        try {
            obj.put("transaction_id", transactionID);
        } catch (JSONException e) {
            e.printStackTrace();
        }

        JsonObjectRequest jsonObjectRequest = new JsonObjectRequest(Request.Method.POST, Api.CANCEL_TRANSACTION_REQUEST, obj,
                new Response.Listener<JSONObject>() {
                    @Override
                    public void onResponse(JSONObject response) {
                        Log.e(Api.TAG, String.valueOf(response));
                        v.getContext().startActivity(new Intent(v.getContext(), TransactionActivity.class));
                        pDialog.dismiss();
                    }
                },
                new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        Log.e(Api.TAG, error.toString());
                        pDialog.dismiss();
                    }
                });
        RequestQueue requestQueue = Volley.newRequestQueue(v.getContext());
        requestQueue.add(jsonObjectRequest);
        jsonObjectRequest.setRetryPolicy(new DefaultRetryPolicy(10000,
                DefaultRetryPolicy.DEFAULT_MAX_RETRIES,
                DefaultRetryPolicy.DEFAULT_BACKOFF_MULT));
    }
}
