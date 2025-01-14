package in.aaho.android.ownr.transaction;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.util.Log;

import org.json.JSONException;
import org.json.JSONObject;

import java.util.List;

import in.aaho.android.ownr.common.BaseActivity;
import in.aaho.android.ownr.R;
import in.aaho.android.ownr.adapter.QuotationsAdapter;
import in.aaho.android.ownr.data.QuotationsData;
import in.aaho.android.ownr.parser.QuotationParser;
import in.aaho.android.ownr.requests.Api;

@SuppressWarnings("ConstantConditions")
public class QuotationActivity extends BaseActivity {
    private RecyclerView recyclerViewQuotations;
    private LinearLayoutManager layoutManagerQuotation;
    private QuotationsAdapter mQuotationsAdapter;
    private List<QuotationsData> quotationsDataList;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_quotation);
        setToolbarTitle("Quotations");

        recyclerViewQuotations = findViewById(R.id.recycler_view_quotation);
        SetQuotationRecycleView(recyclerViewQuotations);

    }
    public void SetQuotationRecycleView(RecyclerView recyclerView){
        recyclerView.setHasFixedSize(true);
        Intent intent = getIntent();
        Log.e(Api.TAG,getIntent().getStringExtra("quotations"));
        String quotationData = getIntent().getStringExtra("quotations");
        try {
            JSONObject jsonObject = new JSONObject(quotationData);
            QuotationParser quotationParser = new QuotationParser(jsonObject.getJSONArray("data"));


            layoutManagerQuotation = new LinearLayoutManager(this);
            layoutManagerQuotation.setOrientation(LinearLayoutManager.VERTICAL);
            recyclerView.setLayoutManager(layoutManagerQuotation);
            mQuotationsAdapter = new QuotationsAdapter(quotationParser.getQuotationsDataArrayList());
            recyclerView.setAdapter(mQuotationsAdapter);
        } catch (JSONException e) {
            e.printStackTrace();
        }
    }

}
