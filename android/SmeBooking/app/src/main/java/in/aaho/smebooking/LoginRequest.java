package in.aaho.smebooking;

/**
 * Created by mani on 1/6/16.
 */
import com.android.volley.Response;
import com.android.volley.toolbox.StringRequest;

import java.util.HashMap;
import java.util.Map;

/**
 * Created by mani on 05/05/2016.
 */
public class LoginRequest extends StringRequest {
    private static final String LOGIN_REQUEST_URL = "http://54.169.82.235:8000/login/";
    private Map<String, String> params;

    public LoginRequest(String loginData, Response.Listener<String> listener) {
        super(Method.POST, LOGIN_REQUEST_URL, listener, null);
        params = new HashMap<>();
        params.put("data", loginData);
        params.put("username", "sme");
    }

    @Override
    public Map<String, String> getParams() {
        return params;
    }

}