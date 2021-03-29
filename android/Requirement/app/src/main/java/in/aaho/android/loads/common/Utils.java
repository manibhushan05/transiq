package in.aaho.android.loads.common;

import android.app.ProgressDialog;
import android.content.Context;
import android.content.DialogInterface;
import android.support.v7.app.AlertDialog;
import android.text.TextUtils;
import android.widget.Toast;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.Date;
import java.util.List;
import java.util.Locale;
import java.util.Map;
import java.util.TimeZone;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import in.aaho.android.loads.R;

/**
 * Created by aaho on 18/04/18.
 */


public class Utils {
    private static final SimpleDateFormat dateFormat = new SimpleDateFormat("EEE, d MMM yyyy, h:mm a");
    private static final SimpleDateFormat jsonDateFormat = new SimpleDateFormat("yyyy/MM/dd HH:mm:ss");
    private static final SimpleDateFormat dateOnlyFormat = new SimpleDateFormat("yyyy/MM/dd");
    private static final SimpleDateFormat dateSimpleFormat = new SimpleDateFormat("d MMM ''yy");

    /** shipment date format as 'dd-MMM-yyyy' eg. 01-Jan-2018 */
    public static final SimpleDateFormat shipmentDateFormat = new SimpleDateFormat("dd-MMM-yyyy", Locale.getDefault());
    public static final SimpleDateFormat pickerDateFormat = new SimpleDateFormat("dd-MM-yyyy");
    /** For searching the text in editText */
    public static String searchText = "",fromDate = "",toDate = "";
    private static ProgressDialog progress;

    /** Regex for IFSC code */
    public static String REGEX_FOR_ALPHANEUMERIC = "[^a-zA-Z0-9]";
    public static String REGEX_FOR_IFSC = "^[A-Za-z]{4}0[A-Z0-9]{6}";
    public static String REGEX_FOR_PAN = "^[a-z]{3}[abcfghljptk][a-z]\\d{4}[a-z]{1}";



    public static String get(JSONObject jsonObject, String key) throws JSONException {
        if (jsonObject == null || jsonObject.length() == 0) {
            return null;
        }
        if (!jsonObject.has(key) || jsonObject.isNull(key)) {
            return null;
        }
        return jsonObject.getString(key);
    }

    public static Long getLong(JSONObject jsonObject, String key) throws JSONException {
        if (jsonObject == null || jsonObject.length() == 0) {
            return null;
        }
        if (!jsonObject.has(key) || jsonObject.isNull(key)) {
            return null;
        }
        return jsonObject.getLong(key);
    }

    public static Date getDate(JSONObject jsonObject, String key) throws JSONException {
        String dateStr = get(jsonObject, key);
        return jsonParseDate(dateStr);
    }

    public static boolean equals(String str1, String str2) {
        str1 = (str1 == null ? "" : str1.trim());
        str2 = (str2 == null ? "" : str2.trim());
        return str1.equals(str2);
    }

    public static boolean equals(Date date1, Date date2) {
        if (date1 != null) {
            return date1.equals(date2);
        } else {
            return date2 == null;
        }
    }

    public static boolean equals(Object obj1, Object obj2) {
        if (obj1 != null) {
            return obj1.equals(obj2);
        } else {
            return obj2 == null;
        }
    }

    public static String jsonFormatDate(Date date) {
        if (date == null) {
            return "";
        }
        return jsonDateFormat.format(date);
    }

    public static Date jsonParseDate(String dateStr) {
        if (dateStr == null) {
            return null;
        }
        dateStr = dateStr.trim();
        if (dateStr.isEmpty()) {
            return null;
        }
        try {
            return jsonDateFormat.parse(dateStr);
        } catch (ParseException e) {
            e.printStackTrace();
            return null;
        }
    }

    public static String formatDate(Date date) {
        if (date == null) {
            return "";
        }
        return dateOnlyFormat.format(date);
    }

    public static String formatDateSimple(Date date) {
        if (date == null) {
            return "";
        }
        return dateSimpleFormat.format(date);
    }

    public static Date parseDate(String dateStr) {
        try {
            return dateFormat.parse(dateStr);
        } catch (ParseException e) {
            e.printStackTrace();
            return null;
        }
    }

    public static Date getDate(int year, int month, int day, int hour, int minute) {
        Calendar cal = Calendar.getInstance();
        cal.set(Calendar.YEAR, year);
        cal.set(Calendar.MONTH, month);
        cal.set(Calendar.DAY_OF_MONTH, day);
        cal.set(Calendar.HOUR_OF_DAY, hour);
        cal.set(Calendar.MINUTE, minute);
        cal.set(Calendar.SECOND, 0);
        cal.set(Calendar.MILLISECOND, 0);
        return cal.getTime();
    }

    public static Date getDate(int year, int month, int day) {
        return getDate(year, month, day, 0, 0);
    }

    public static void toast(String msg) {
        MainApplication application = MainApplication.getInstance();
        if (application == null) {
            return;
        }
        Toast.makeText(application.getApplicationContext(), msg, Toast.LENGTH_LONG).show();
    }

    // to get something like python's `if not <any_type>` in java
    public static boolean not(String str) {
        return str == null || str.trim().isEmpty();
    }

    public static boolean not(List<?> list) {
        return list == null || list.isEmpty();
    }

    public static boolean not(Map<?, ?> map) {
        return map == null || map.isEmpty();
    }

    public static boolean not(JSONObject jsonObject) {
        return jsonObject == null || jsonObject.length() == 0;
    }

    public static boolean not(JSONArray jsonArray) {
        return jsonArray == null || jsonArray.length() == 0;
    }

    public static boolean not(Object object) {
        return object == null;
    }

    public static String def(String name, String defaultValue) {
        return not(name) ? defaultValue : name.trim();
    }

    public static boolean any(boolean... bools) {
        for (boolean bool : bools) {
            if (bool) {
                return true;
            }
        }
        return false;
    }

    public static boolean all(boolean... bools) {
        for (boolean bool : bools) {
            if (!bool) {
                return false;
            }
        }
        return true;
    }

    public static List<String> filter(List<String> list) {
        List<String> newList = new ArrayList<>();
        for (String item : list) {
            if (!Utils.not(item)) {
                newList.add(item);
            }
        }
        return newList;
    }

    public static String join(List<String> textList, String sep) {
        StringBuilder stringBuilder = new StringBuilder();
        for (int i = 0; i < textList.size(); i++) {
            if (i != 0) {
                stringBuilder.append(sep);
            }
            stringBuilder.append(textList.get(i));
        }
        return stringBuilder.toString();
    }

    public static Date parseShipmentDate(String dateStr) {
        try {
            shipmentDateFormat.setTimeZone(TimeZone.getTimeZone("GMT"));
            return shipmentDateFormat.parse(dateStr);
        } catch (ParseException e) {
            e.printStackTrace();
            return null;
        }
    }

    private static void setUpProgressDialog(Context context) {
        progress = new ProgressDialog(context);
        progress.setTitle(R.string.progress_title);
        progress.setMessage(context.getString(R.string.progress_msg));
        progress.setCanceledOnTouchOutside(false);
    }

    private static ProgressDialog getProgress(Context context) {
        if (progress == null) {
            setUpProgressDialog(context);
        }
        return progress;
    }

    public static void showProgress(Context context) {
        getProgress(context).show();
    }

    public static void dismissProgress(Context context) {
        getProgress(context).dismiss();
    }

    /** Common Alert dialog to get user yes/no type feedback*
     * @param context context
     * @param title Title of Alert dialog
     * @param msg Message to be display
     * @param positiveBtnCaption Positive Button caption eg. Yes or Submit
     * @param negativeBtnCaption Negative Button caption eg. No or Dismiss
     * @param alertDialogListener Listener to know which button is clicked
     */
    public static void showAlertDialog(Context context, String title,
                                       String msg, String positiveBtnCaption,
                                       String negativeBtnCaption,
                                       final AlertDialogListener alertDialogListener) {
        AlertDialog.Builder builder = new AlertDialog.Builder(context);

        builder.setTitle(title);
        builder.setMessage(msg);
        builder.setPositiveButton(positiveBtnCaption, new DialogInterface.OnClickListener() {
            public void onClick(DialogInterface dialog, int id) {
                alertDialogListener.onPositiveButtonClicked();
            }
        });
        builder.setNegativeButton(negativeBtnCaption, new DialogInterface.OnClickListener() {
            public void onClick(DialogInterface dialog, int id) {
                alertDialogListener.onNegativeButtonClicked();
            }
        });
        builder.show();
    }

    public interface AlertDialogListener {
        void onPositiveButtonClicked();
        void onNegativeButtonClicked();
    }

    /** Check if valid IFSC number or not
     * @param inputText text to validate as IFSC
     * @return true if valid pan else false */
    public static boolean isValidIFSC(String inputText) {
        Pattern p = Pattern.compile(REGEX_FOR_IFSC);
        Matcher m = p.matcher(inputText);
        return m.matches();
    }

    /** Check if valid PAN number or not
     * @param inputText text to validate as PAN
     * @return true if valid pan else false */
    public static boolean isValidPAN(String inputText) {
        if(TextUtils.isEmpty(inputText) || inputText.length() <10) {
            return false;
        }

        Pattern p = Pattern.compile(REGEX_FOR_PAN);
        Matcher m = p.matcher(inputText);
        return m.matches();
    }

}
