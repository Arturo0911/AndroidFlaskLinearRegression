package com.example.puremango;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.graphics.Color;
import android.graphics.drawable.ColorDrawable;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Toast;

import androidx.appcompat.app.ActionBar;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.Volley;
import com.apollographql.apollo.ApolloCall;
import com.apollographql.apollo.ApolloClient;
import com.apollographql.apollo.exception.ApolloException;
import com.google.android.material.textfield.TextInputEditText;

import org.jetbrains.annotations.NotNull;
import org.json.JSONObject;

public class LoginPage extends AppCompatActivity {

    private TextInputEditText userField;
    private TextInputEditText passField;
    private static final String url = "http://" + "10.0.2.2"+":"+5000+"/login_resolve";


    ActionBar actionBar;

    public void initLoginButton(View view){
        String username = userField.getText().toString();
        String password = passField.getText().toString();
        try {
            loginUser(username,password, ConnectionServer.urlServer);
        }catch (Exception e){
            Log.i("java error: ", e.toString());
            Toast.makeText(this, ": "+e.toString(), Toast.LENGTH_SHORT).show();
        }
    }

    public void loginUser(String username, String password, String urlServer){
        ApolloClient apolloClient = ApolloClient.builder()
                .serverUrl(urlServer)
                .build();
        try {
            apolloClient.mutate(new LoginUserMutation(username,password ))
                    .enqueue(new ApolloCall.Callback<LoginUserMutation.Data>(){
                        @Override
                        public void onResponse(@NotNull com.apollographql.apollo.api.Response<LoginUserMutation.Data> response) {
                            Employee.credentials = response.getData().loginUser.employee.credentials;
                            Employee.names = response.getData().loginUser.employee.names;
                            Employee.lastnames = response.getData().loginUser.employee.lastNames;
                            Employee.phoneNumber = response.getData().loginUser.employee.phoneNumber;
                            Employee.emailAddress = response.getData().loginUser.employee.emailAddress;
                            Employee.departmentId = response.getData().loginUser.employee.departmentId;
                            Employee.departmentName = response.getData().loginUser.employee.departmentName;
                            Intent intent = new Intent(LoginPage.this, MainActivity.class);
                            startActivity(intent);
                        }

                        @Override
                        public void onFailure(@NotNull ApolloException e) {
                            e.printStackTrace();
                        }
                    });

        }catch (Exception e){
            e.printStackTrace();
            Toast.makeText(this, "Error en la conexión con el servidor", Toast.LENGTH_SHORT).show();
        }
    }

    public void onClickCreateAccountButton(View view){
        Intent intentCreateAccount = new Intent(LoginPage.this,Signup.class);
        startActivity(intentCreateAccount);
    }

    public void onClickForgotPassword(View view ){
        Intent intentForgotPassword = new Intent(LoginPage.this, RecoverPassword.class);
        startActivity(intentForgotPassword);
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login_page);
        actionBar  = getSupportActionBar();
        assert actionBar != null;
        actionBar.setBackgroundDrawable(new ColorDrawable(Color.parseColor("#273036")));
        actionBar.setTitle("Pure Mango");

        userField = (TextInputEditText) findViewById(R.id.userField);
        passField = (TextInputEditText) findViewById(R.id.passField);

    }
}