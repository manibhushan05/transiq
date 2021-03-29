package in.aaho.android.employee.loads;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.List;

import in.aaho.android.employee.common.Utils;

/**
 * Created by aaho on 20/05/18.
 */

public class MyLoadRequest {

    public Integer id;
    public Integer rate;
    public Double tonnage;
    public Integer noOfVehicles;
    public Integer fromCityId;
    public Integer toCityId;
    public Integer typeOfVehicleId;
    public Integer clientId;
    public Integer officeId;
    ;
    public String fromShipmentDate, toShipmentDate;
    public String material;
    public String toCity;
    public String client;
    public String fromCity;
    public String typeOfVehicle;
    public String aahoOffice;
    public String fromState;
    public String toState;
    public String reqStatus;
    public String remark;
    public String cancelReason;

    public boolean rdOnlyStatus;

    private static final String KEY_ID = "id";
    private static final String KEY_TO_SHIPMENT_DATE = "to_shipment_date";
    private static final String KEY_MATERIAL = "material";
    private static final String KEY_RATE = "rate";
    private static final String KEY_REMARK = "remark";
    private static final String KEY_TONNAGE = "tonnage";
    private static final String KEY_NO_OF_VEHICLE = "no_of_vehicles";
    private static final String KEY_FROM_SHIPMENT_DATE = "from_shipment_date";
    private static final String KEY_TO_CITY = "to_city";
    private static final String KEY_CLIENT = "client";
    private static final String KEY_FROM_CITY = "from_city";
    private static final String KEY_TYPE_OF_VEHICLE = "type_of_vehicle";
    private static final String KEY_AAHO_OFFICE = "aaho_office";
    private static final String KEY_FROM_STATE = "from_state";
    private static final String KEY_TO_STATE = "to_state";

    private static final String KEY_FROM_CITY_ID = "from_city_id";
    private static final String KEY_TO_CITY_ID = "to_city_id";
    private static final String KEY_TYPE_OF_VEHICLE_ID = "type_of_vehicle_id";
    private static final String KEY_CLIENT_ID = "client_id";
    private static final String KEY_OFFICE_ID = "aaho_office_id";
    private static final String KEY_REQ_STATUS = "req_status";
    private static final String KEY_RDONLY_STATUS = "read_only";
    private static final String KEY_CANCEL_REASON = "cancel_reason";

//    private static final String KEY_VERIFIED = "verified";


    public MyLoadRequest(Integer id, Integer rate, Double tonnage, Integer noOfVehicles,
                         String fromShipmentDate, String toShipmentDate,
                         String material, String toCity, String client, String fromCity,
                         String typeOfVehicle, String aahoOffice, String fromState,
                         String toState, Integer fromCityId, Integer toCityId,
                         Integer typeOfVehicleId, Integer clientId, Integer officeId, String reqStatus,
                         boolean rdOnlyStatus, String remark, String cancelReason) {
        this.id = id;
        this.rate = rate;
        this.tonnage = tonnage;
        this.noOfVehicles = noOfVehicles;
        this.fromShipmentDate = fromShipmentDate;
        this.toShipmentDate = toShipmentDate;
        this.material = material;
        this.toCity = toCity;
        this.client = client;
        this.fromCity = fromCity;
        this.typeOfVehicle = typeOfVehicle;
        this.aahoOffice = aahoOffice;
        this.fromState = fromState;
        this.toState = toState;
        this.fromCityId = fromCityId;
        this.toCityId = toCityId;
        this.typeOfVehicleId = typeOfVehicleId;
        this.clientId = clientId;
        this.officeId = officeId;
        this.reqStatus = reqStatus;
        this.rdOnlyStatus = rdOnlyStatus;
        this.remark = remark;
        this.cancelReason = cancelReason;
    }

    public static MyLoadRequest fromJson(JSONObject jsonObject) throws JSONException {
        if (jsonObject == null || jsonObject.length() == 0) {
            return null;
        }
        return new MyLoadRequest(
                Utils.getInteger(jsonObject, KEY_ID),
                Utils.getInteger(jsonObject, KEY_RATE) == null ? null : Utils.getInteger(jsonObject, KEY_RATE),
                Utils.getDouble(jsonObject, KEY_TONNAGE),
                Utils.getInteger(jsonObject, KEY_NO_OF_VEHICLE) == null ? null : Utils.getInteger(jsonObject, KEY_NO_OF_VEHICLE),
                Utils.get(jsonObject, KEY_FROM_SHIPMENT_DATE),
                Utils.get(jsonObject, KEY_TO_SHIPMENT_DATE),
                Utils.get(jsonObject, KEY_MATERIAL),
                Utils.get(jsonObject, KEY_TO_CITY),
                Utils.get(jsonObject, KEY_CLIENT),
                Utils.get(jsonObject, KEY_FROM_CITY),
                Utils.get(jsonObject, KEY_TYPE_OF_VEHICLE),
                Utils.get(jsonObject, KEY_AAHO_OFFICE),
                Utils.get(jsonObject, KEY_FROM_STATE),
                Utils.get(jsonObject, KEY_TO_STATE),
                Utils.getInteger(jsonObject, KEY_FROM_CITY_ID) == null ? null : Utils.getInteger(jsonObject, KEY_FROM_CITY_ID),
                Utils.getInteger(jsonObject, KEY_TO_CITY_ID) == null ? null : Utils.getInteger(jsonObject, KEY_TO_CITY_ID),
                Utils.getInteger(jsonObject, KEY_TYPE_OF_VEHICLE_ID) == null ? null : Utils.getInteger(jsonObject, KEY_TYPE_OF_VEHICLE_ID),
                Utils.getInteger(jsonObject, KEY_CLIENT_ID) == null ? null : Utils.getInteger(jsonObject, KEY_CLIENT_ID),
                Utils.getInteger(jsonObject, KEY_OFFICE_ID) == null ? null : Utils.getInteger(jsonObject, KEY_OFFICE_ID),
                Utils.get(jsonObject, KEY_REQ_STATUS),
                jsonObject.getBoolean(KEY_RDONLY_STATUS),
                Utils.get(jsonObject, KEY_REMARK),
                Utils.get(jsonObject, KEY_CANCEL_REASON)
        );
    }

    private static JSONObject getObject(JSONObject jsonObject, String key) {
        if (jsonObject == null || jsonObject.length() == 0) {
            return null;
        }
        if (!jsonObject.has(key) || jsonObject.isNull(key)) {
            return null;
        }
        try {
            return jsonObject.getJSONObject(key);
        } catch (JSONException e) {
            return null;
        }
    }

    public static List<MyLoadRequest> fromJson(JSONArray jsonArray) throws JSONException {
        List<MyLoadRequest> vehicles = new ArrayList<>();
        List<MyLoadRequest> bottom = new ArrayList<>();
        for (int i = 0; i < jsonArray.length(); i++) {
            JSONObject obj = jsonArray.getJSONObject(i);
            MyLoadRequest vehicle = fromJson(obj);
            String req_status = Utils.def(vehicle.reqStatus, "");
            if(req_status.equalsIgnoreCase("fulfilled") ||
                    req_status.equalsIgnoreCase("cancelled") ||
                    req_status.equalsIgnoreCase("lapsed")){
                bottom.add(vehicle);
            }else{
                vehicles.add(vehicle);
            }
        }
        vehicles.addAll(bottom);
        return vehicles;
    }
}