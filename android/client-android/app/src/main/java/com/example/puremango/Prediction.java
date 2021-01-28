package com.example.puremango;

import androidx.appcompat.app.ActionBar;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.graphics.Color;
import android.graphics.drawable.ColorDrawable;
import android.os.Bundle;
import android.view.View;
import android.widget.TextView;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONException;
import org.json.JSONObject;

public class Prediction extends AppCompatActivity {



    ActionBar actionBar;
    TextView actualPrediction;
    TextView desirePrediction;

    public void onClickVolverPrediction(View view){
        Intent intent = new Intent(Prediction.this, MainActivity.class);
        startActivity(intent);
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_prediction);
        actionBar  = getSupportActionBar();
        assert actionBar != null;
        actionBar.setBackgroundDrawable(new ColorDrawable(Color.parseColor("#273036")));
        actionBar.setTitle("Pure Mango");


        actualPrediction = (TextView) findViewById(R.id.actualPrediction);
        desirePrediction = (TextView) findViewById(R.id.desirePrediction);

        actualPrediction.setText(PredictionModel.actual_precission);
        desirePrediction.setText(PredictionModel.desire_prediction);
        /*try {
            RequestQueue requestQueue = Volley.newRequestQueue(Prediction.this);
            JsonObjectRequest jsonObjectRequest = new JsonObjectRequest(
                    Request.Method.GET,
                    url,
                    null,
                    new Response.Listener<JSONObject>() {
                        @Override
                        public void onResponse(JSONObject response) {
                            try {
                                actualPrediction.setText(response.get("porcentaje_precision_actual").toString());
                                desirePrediction.setText(response.get("prediction_optima").toString());
                            } catch (JSONException e) {
                                e.printStackTrace();
                            }
                        }
                    }, new Response.ErrorListener() {
                @Override
                public void onErrorResponse(VolleyError error) {

                }
            });
        }catch (Exception e ){
            e.printStackTrace();
        }*/



        //actualPrediction.setText();

    }
}