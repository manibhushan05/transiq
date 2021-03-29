package in.aaho.android.ownr.transaction;

import android.content.Context;
import android.os.Bundle;
import android.support.annotation.NonNull;
import android.support.annotation.Nullable;
import android.support.v4.app.Fragment;
import android.support.v4.app.FragmentManager;
import android.support.v7.widget.AppCompatEditText;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.text.Editable;
import android.text.TextUtils;
import android.text.TextWatcher;
import android.util.Log;
import android.view.GestureDetector;
import android.view.LayoutInflater;
import android.view.MotionEvent;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageButton;
import android.widget.RelativeLayout;
import android.widget.TextView;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;

import in.aaho.android.ownr.R;
import in.aaho.android.ownr.adapter.ConfirmedTransactionAdapter;
import in.aaho.android.ownr.adapter.InTransitTransactionAdapter;
import in.aaho.android.ownr.common.DatePickerDialogFragment;
import in.aaho.android.ownr.common.Utils;
import in.aaho.android.ownr.data.ConfirmedTransactionData;
import in.aaho.android.ownr.parser.BookingDataParser;


public class PODPendingFragment extends Fragment implements View.OnClickListener,
        DatePickerDialogFragment.FilterDialogListener {

    ImageButton filterImageButton;
    AppCompatEditText filterEditText;
    TextView textViewNumberOfBooking,textViewTotalAmount,textViewPaidAmount,
            textViewBalanceAmount;
    ConfirmedTransactionAdapter mAdapter;
    List<ConfirmedTransactionData> mDataList = new ArrayList<>();
    RecyclerView recyclerView;
    IOnUploadPodClickedListener iOnUploadPodClickedListener;
    RelativeLayout rlTripDetailsMainContent;

    public interface IOnUploadPodClickedListener {
        void onUploadPodClicked(ConfirmedTransactionData confirmedTransactionData);
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        View rootView = inflater.inflate(R.layout.fragment_confirmed, container, false);
        //setHasOptionsMenu(true);
        findViews(rootView);
        SetupRecycleView();
        /*filter(Utils.searchText);
        filterWithDateRange(Utils.fromDate,Utils.toDate);*/

        return rootView;
    }

    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);
        setData();
    }

    @Override
    public void onAttach(Context context) {
        super.onAttach(context);
        if(context instanceof IOnUploadPodClickedListener) {
            iOnUploadPodClickedListener = (IOnUploadPodClickedListener) context;
        }
    }

    @Override
    public void onDetach() {
        super.onDetach();
        if(iOnUploadPodClickedListener != null) {
            iOnUploadPodClickedListener = null;
        }
    }

    /** find/bind data to views */
    void findViews(View view) {
        rlTripDetailsMainContent = view.findViewById(R.id.rlTripDetailsMainContent);
        filterImageButton = view.findViewById(R.id.filterImageButton);
        filterImageButton.setOnClickListener(this);
        filterEditText = view.findViewById(R.id.filterEditText);
        textViewNumberOfBooking = view.findViewById(R.id.tvNumberOfBookingsValue);
        textViewTotalAmount = view.findViewById(R.id.tvTotalAmountValue);
        textViewPaidAmount = view.findViewById(R.id.tvPaidValue);
        textViewBalanceAmount = view.findViewById(R.id.tvBalanceValue);
        recyclerView = view.findViewById(R.id.recycler_view_confirmed_transaction);
    }

    void SetupRecycleView() {
        recyclerView.setHasFixedSize(true);
        LinearLayoutManager layoutManager = new LinearLayoutManager(getActivity());
        layoutManager.setOrientation(LinearLayoutManager.VERTICAL);
        recyclerView.setLayoutManager(layoutManager);
        setRecyclerScroll();
    }

    @Override
    public void onClick(View view) {
        switch (view.getId()) {
            case R.id.filterImageButton:
                showFilterDialog();
                break;
            default:
                break;
        }
    }

    @Override
    public void onFinishFilterDialog(String fromDate, String toDate) {
        /*List<ConfirmedTransactionData> dataList = filterListWithDateRange(mDataList,
                "01-Dec-2017","01-Jan-2018");*/

        List<ConfirmedTransactionData> dataList = filterListWithDateRange(mDataList,
                fromDate,toDate);

        // refresh the adapter with new filtered list
        mAdapter = new ConfirmedTransactionAdapter(getActivity(),dataList, iOnUploadPodClickedListener);
        recyclerView.setAdapter(mAdapter);
        mAdapter.notifyDataSetChanged();
    }

    public interface ClickListener {
        void onClick(View view, int position);

        void onLongClick(View view, int position);
    }

    public static class RecyclerTouchListener implements RecyclerView.OnItemTouchListener {

        private GestureDetector gestureDetector;
        private ClickListener clickListener;

        public RecyclerTouchListener(Context context, final RecyclerView recyclerView, final ClickListener clickListener) {
            this.clickListener = clickListener;
            gestureDetector = new GestureDetector(context, new GestureDetector.SimpleOnGestureListener() {
                @Override
                public boolean onSingleTapUp(MotionEvent e) {
                    return true;
                }

                @Override
                public void onLongPress(MotionEvent e) {
                    View child = recyclerView.findChildViewUnder(e.getX(), e.getY());
                    if (child != null && clickListener != null) {
                        clickListener.onLongClick(child, recyclerView.getChildPosition(child));
                    }
                }
            });
        }

        @Override
        public boolean onInterceptTouchEvent(RecyclerView rv, MotionEvent e) {

            View child = rv.findChildViewUnder(e.getX(), e.getY());
            if (child != null && clickListener != null && gestureDetector.onTouchEvent(e)) {
                clickListener.onClick(child, rv.getChildPosition(child));
            }
            return false;
        }

        @Override
        public void onTouchEvent(RecyclerView rv, MotionEvent e) {
        }

        @Override
        public void onRequestDisallowInterceptTouchEvent(boolean disallowIntercept) {

        }
    }


    /** filter the given list with given date range and return the filtered list
     * @param fromDate from date
     * @param toDate to date
     */
    private List<ConfirmedTransactionData> filterListWithDateRange(List<ConfirmedTransactionData> listToFilter,
                                                                   String fromDate, String toDate) {
        List<ConfirmedTransactionData> confirmedTransactionDataArrayList = new ArrayList<>();
        try {
            Date dtFromDate = Utils.parseShipmentDate(fromDate);
            Date dtToDate = Utils.parseShipmentDate(toDate);
            if(listToFilter != null && listToFilter.size() > 0) {
                for (int iCount = 0; iCount < listToFilter.size() ; iCount++) {
                    String shipmentDate = listToFilter.get(iCount).getShipmentDate();
                    Date dtShipmentDate = Utils.parseShipmentDate(shipmentDate);
                    if( (dtShipmentDate.compareTo(dtFromDate) < 0)
                            || (dtShipmentDate.compareTo(dtToDate) > 0)) {
                        // not within range
                    } else {
                        // within range
                        confirmedTransactionDataArrayList.add(listToFilter.get(iCount));
                    }
                }
            }

        } catch (Exception ex) {
            Log.e("filterListWithDateRange","Exception while filtering with date range!"+ex.getLocalizedMessage());
        }

        return confirmedTransactionDataArrayList;
    }

    private void showFilterDialog() {
        FragmentManager fm = getChildFragmentManager();
        //DatePickerDialogFragment editNameDialogFragment = DatePickerDialogFragment.newInstance("Some Title");
        DatePickerDialogFragment editNameDialogFragment = new DatePickerDialogFragment(new DatePickerDialogFragment.FilterDialogListener() {
            @Override
            public void onFinishFilterDialog(String fromDate, String toDate) {
                /*List<ConfirmedTransactionData> dataList = filterListWithDateRange(mDataList,
                        fromDate,toDate);

                // refresh the adapter with new filtered list
                mAdapter = new ConfirmedTransactionAdapter(getActivity(),dataList);
                recyclerView.setAdapter(mAdapter);
                mAdapter.notifyDataSetChanged();*/
            }
        });
        editNameDialogFragment.show(fm, "fragment_pick_date");
    }

    public void filter(String query) {
        if(mAdapter != null)
            mAdapter.filter(query);
    }

    public void filterWithDateRange(String fromDate, String toDate) {
        if(!TextUtils.isEmpty(fromDate) && !TextUtils.isEmpty(toDate)) {
            List<ConfirmedTransactionData> dataList = filterListWithDateRange(mDataList,
                    fromDate, toDate);

            // refresh the adapter with new filtered list
            mAdapter = new ConfirmedTransactionAdapter(getActivity(), dataList, iOnUploadPodClickedListener);
            if(recyclerView != null)
                recyclerView.setAdapter(mAdapter);
            if(mAdapter != null)
                mAdapter.notifyDataSetChanged();
        }
    }

    public void setSummaryVisibility(boolean visibility) {
        if(rlTripDetailsMainContent != null) {
            if (visibility) {
                rlTripDetailsMainContent.setVisibility(View.VISIBLE);
            } else {
                rlTripDetailsMainContent.setVisibility(View.GONE);
            }
        }
    }

    public void setData() {
        String transactionData = ((TransactionActivity)getActivity()).getJsonArrayTransaction();
        try {
            if(!TextUtils.isEmpty(transactionData)) {
                JSONArray jsonArray = new JSONArray(transactionData);
                if(jsonArray != null && jsonArray.length() > 0) {
                    BookingDataParser bookingDataParser = new BookingDataParser(jsonArray);
                    mDataList.addAll(bookingDataParser.getPODPendingBookingDataArrayList());
                    mAdapter = new ConfirmedTransactionAdapter(getActivity(), mDataList, iOnUploadPodClickedListener);
                    recyclerView.setAdapter(mAdapter);
                }
            }

            // Set summary data
            String summaryData = ((TransactionActivity)getActivity()).getJsonSummary();
            if(!TextUtils.isEmpty(summaryData)) {
                JSONObject summary = new JSONObject(summaryData);
                if (summary != null) {
                    JSONObject podPendingData = summary.getJSONObject("pending_pod");
                    if (podPendingData != null) {
                        textViewNumberOfBooking.setText(Utils.get(podPendingData, "number_of_booking"));
                        textViewTotalAmount.setText(Utils.get(podPendingData, "total_amount"));
                        textViewBalanceAmount.setText(Utils.get(podPendingData, "balance"));
                        textViewPaidAmount.setText(Utils.get(podPendingData, "amount_paid"));
                    }
                }
            }

        } catch (JSONException e) {
            e.printStackTrace();
        }
    }

    private void setRecyclerScroll() {
        recyclerView.addOnScrollListener(new RecyclerView.OnScrollListener() {
            @Override
            public void onScrollStateChanged(RecyclerView recyclerView, int newState) {
                super.onScrollStateChanged(recyclerView, newState);

                if (!recyclerView.canScrollVertically(1)) {
                    ((TransactionActivity)getActivity()).loadMoreData();
                }
            }
        });
    }

    public void resetData() {
        try {
            mDataList = new ArrayList<>();
            mAdapter = new ConfirmedTransactionAdapter(getActivity(), mDataList, iOnUploadPodClickedListener);
            recyclerView.setAdapter(mAdapter);
        } catch (Exception ex) {

        }
    }
}