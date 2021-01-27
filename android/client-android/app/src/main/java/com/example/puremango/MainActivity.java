package com.example.puremango;

import androidx.appcompat.app.ActionBar;
import androidx.appcompat.app.AppCompatActivity;

import android.graphics.Color;
import android.graphics.drawable.ColorDrawable;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Toast;

import com.apollographql.apollo.ApolloCall;
import com.apollographql.apollo.ApolloClient;
import com.apollographql.apollo.api.Response;
import com.apollographql.apollo.exception.ApolloException;

import org.jetbrains.annotations.NotNull;

public class MainActivity extends AppCompatActivity {
    ActionBar actionBar;
    private static final String postRquest = "http://" + "10.0.2.2"+":"+5000+"/graphql";

    public void onButtonTestClick(View view){
        try {
            ApolloClient apolloClient = ApolloClient.builder()
                    .serverUrl(postRquest)
                    .build();

            apolloClient.query(new QueryEmployeeQuery())
                    .enqueue(new ApolloCall.Callback<QueryEmployeeQuery.Data>() {

                        @Override
                        public void onResponse(@NotNull Response<QueryEmployeeQuery.Data> response) {
                            Log.i("on response: ", "onResponse: "+response.getData().allEmployee.edges.get(0).node.credentials());
                            //Toast.makeText(MainActivity.this, response.getData().toString(), Toast.LENGTH_SHORT).show();
                        }
                        @Override
                        public void onFailure(@NotNull ApolloException e) {
                            e.printStackTrace();
                            //Toast.makeText(MainActivity.this, "Error in: "+e.toString(), Toast.LENGTH_SHORT).show();
                        }
                    });

        }catch (Exception e){
            Toast.makeText(this, "Error by: "+e.toString(), Toast.LENGTH_SHORT).show();
        }
    }

    public void onTestButton(View view){
        Toast.makeText(this, "the name of the employee is: "+Employee.names, Toast.LENGTH_SHORT).show();
    }


    //private

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        actionBar  = getSupportActionBar();
        actionBar.setBackgroundDrawable(new ColorDrawable(Color.parseColor("#273036")));
        actionBar.setTitle("Pure Mango");
    }
}