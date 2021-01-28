package com.example.puremango;

import androidx.appcompat.app.ActionBar;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.graphics.Color;
import android.graphics.drawable.ColorDrawable;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.TextView;
import android.widget.Toast;

import com.apollographql.apollo.ApolloCall;
import com.apollographql.apollo.ApolloClient;
import com.apollographql.apollo.api.Response;
import com.apollographql.apollo.exception.ApolloException;

import org.jetbrains.annotations.NotNull;

public class MainActivity extends AppCompatActivity {
    ActionBar actionBar;
    private static final String postRquest = "http://" + "10.0.2.2"+":"+5000+"/graphql";

    private TextView profileCredential;
    private TextView profileNames;
    private TextView profileLastNames;

    private TextView profits;
    private TextView expenses;


    public void editProfileButton(View view){
        Intent intent = new Intent(MainActivity.this, EditProfile.class);
        startActivity(intent);
    }

    public void onClickCheckBalance(View view){
        ApolloClient apolloClient = ApolloClient.builder()
                .serverUrl(ConnectionServer.urlServer)
                .build();

        apolloClient.query(new LastSalesQuery("2019-10-01"))
                .enqueue(new ApolloCall.Callback<LastSalesQuery.Data>() {
                    @Override
                    public void onResponse(@NotNull Response<LastSalesQuery.Data> response) {
                        LastBalance.timeStart = response.getData().search.timeStart;
                        LastBalance.timeEnd = response.getData().search.timeEnd;
                        LastBalance.income = response.getData().search.income;
                        LastBalance.expenses = response.getData().search.expenses;
                        LastBalance.productName = response.getData().search.productName;
                    }

                    @Override
                    public void onFailure(@NotNull ApolloException e) {

                    }
                });


        Intent intent = new Intent(MainActivity.this, AllSales.class);
        startActivity(intent);
    }

    public void onClickPrediction(View view){
        Intent intent = new Intent(MainActivity.this, Prediction.class);
        startActivity(intent);
    }

    //private

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        actionBar  = getSupportActionBar();
        actionBar.setBackgroundDrawable(new ColorDrawable(Color.parseColor("#273036")));


        profileCredential = (TextView) findViewById(R.id.profileCredential);
        profileNames = (TextView) findViewById(R.id.profileNames);
        profileLastNames = (TextView) findViewById(R.id.profileLastNames);

        profileCredential.setText(Employee.credentials);
        profileNames.setText(Employee.names);
        profileLastNames.setText(Employee.lastnames);
        /*profits.setText((int)LastBalance.income);
        expenses.setText((int)LastBalance.expenses);*/

    }

    public void finisheActivity(View view){
        finish();
    }


}