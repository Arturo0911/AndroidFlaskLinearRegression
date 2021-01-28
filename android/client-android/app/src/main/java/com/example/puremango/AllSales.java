package com.example.puremango;

import androidx.appcompat.app.ActionBar;
import androidx.appcompat.app.AppCompatActivity;

import android.Manifest;
import android.content.Intent;
import android.graphics.Color;
import android.graphics.drawable.ColorDrawable;
import android.os.Bundle;
import android.view.View;
import android.widget.TextView;

public class AllSales extends AppCompatActivity {
    ActionBar actionBar;
    TextView Ganancias;
    TextView Perdidas;
    TextView nombreProducto;
    TextView timeStart;
    TextView timeEnd;

    public void onClickVolver(View view){
        Intent intent  = new Intent(AllSales.this, MainActivity.class);
        startActivity(intent);
    }



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_all_sales);
        actionBar  = getSupportActionBar();
        assert actionBar != null;
        actionBar.setBackgroundDrawable(new ColorDrawable(Color.parseColor("#273036")));
        actionBar.setTitle("Pure Mango");

        Ganancias = (TextView) findViewById(R.id.Ganancias);
        Perdidas = (TextView) findViewById(R.id.Perdidas);
        nombreProducto = (TextView) findViewById(R.id.nombreProducto);
        timeStart = (TextView) findViewById(R.id.timeStart);
        timeEnd = (TextView) findViewById(R.id.timeEnd);


        nombreProducto.setText(LastBalance.productName);
        timeStart.setText(LastBalance.timeStart);
        timeEnd.setText(LastBalance.timeEnd);
        Ganancias.setText("$ "+String.valueOf((int)LastBalance.income));
        Perdidas.setText("$ "+String.valueOf((int)LastBalance.expenses));

    }
}