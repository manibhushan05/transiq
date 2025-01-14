package in.aaho.android.aahocustomers;

import android.os.Bundle;
import android.os.Handler;
import android.support.v4.app.Fragment;
import android.support.v4.app.FragmentManager;
import android.support.v4.app.FragmentTransaction;
import android.support.v7.app.AppCompatActivity;

import java.util.ArrayList;

/**
 * Created by aaho on 14/06/18.
 */


public class ViewPODActivity extends AppCompatActivity implements PODListFragment.IOnListItemSelectionListener {

    FragmentManager mFragmentManager;
    FragmentTransaction mFragmentTransaction;
    final int MI_POD_LIST_FRAGMENT = 1;
    final int MI_POD_DETAIL_FRAGMENT = 2;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_view_pod);

        mFragmentManager = getSupportFragmentManager();

        new Handler().postDelayed(new Runnable() {
            @Override
            public void run() {
                loadFragment(MI_POD_LIST_FRAGMENT,null);
            }
        },100);

        /*mFragmentTransaction = mFragmentManager.beginTransaction();
        mFragmentTransaction.add(R.id.container,PODListFragment.newInstance(pod_docsArrayList),"frag_pod_list");
        mFragmentTransaction.commit();*/

    }

    @Override
    public void onBackPressed() {
        processBackStack();
    }

    void processBackStack() {
        int count = mFragmentManager.getBackStackEntryCount();
        if(count == 1) {
            mFragmentManager.popBackStack();
        } else {
            super.onBackPressed();
        }
    }

    private void loadFragment(int id,Bundle bundle) {
        switch (id) {
            case MI_POD_LIST_FRAGMENT:
                /*ArrayList<POD_DOCS> pod_docsArrayList = (ArrayList<POD_DOCS>)
                        getIntent().getSerializableExtra("Pod_Docs_List");*/

                ObjectFileUtil<ArrayList<POD_DOCS>> objectFileUtil = new ObjectFileUtil<>(
                        this,"PodDocList");
                ArrayList<POD_DOCS> pod_docsArrayList = objectFileUtil.get();


                addFragment(new PODListFragment(),
                        "frag_pod_list", false);
                break;
            case MI_POD_DETAIL_FRAGMENT:
                POD_DOCS pod_docs = null;
                if (bundle != null) {
                    pod_docs = (POD_DOCS) bundle.getSerializable("Pod_Docs");
                }
                addFragment(PodDetailFragment.newInstance(pod_docs),
                        "frag_pod_details", true);
                break;
            default:
                break;
        }
    }

    void addFragment(Fragment fragment, String tag, boolean isAddToBackStack) {
        mFragmentTransaction = mFragmentManager.beginTransaction();
        mFragmentTransaction.add(R.id.container,fragment,tag);
        if(isAddToBackStack)
            mFragmentTransaction.addToBackStack(tag);
        mFragmentTransaction.commit();
    }

    @Override
    public void onListItemSelected(POD_DOCS pod_docs) {
        // load the view pod detail fragment from here
        Bundle bundle = new Bundle();
        bundle.putSerializable("Pod_Docs",pod_docs);
        loadFragment(MI_POD_DETAIL_FRAGMENT,bundle);
    }
}
