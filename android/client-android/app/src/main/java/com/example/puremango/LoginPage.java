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

import com.apollographql.apollo.ApolloCall;
import com.apollographql.apollo.ApolloClient;
import com.apollographql.apollo.api.Response;
import com.apollographql.apollo.exception.ApolloException;
import com.google.android.material.textfield.TextInputEditText;

import org.jetbrains.annotations.NotNull;

public class LoginPage extends AppCompatActivity {

    private TextInputEditText userField;
    private TextInputEditText passField;

    ActionBar actionBar;

    public void initLoginButton(View view){
        try {
            ApolloClient apolloClient = ApolloClient.builder()
                    .serverUrl(ConnectionServer.urlServer)
                    .build();


            apolloClient.mutate(new LoginUserMutation(userField.getText().toString(), passField.getText().toString()))
                    .enqueue(new ApolloCall.Callback<LoginUserMutation.Data>() {
                        @Override
                        public void onResponse(@NotNull Response<LoginUserMutation.Data> response) {
                            Log.i("response: ", ": "+response.getData().loginUser.employee.credentials);
                            Employee.credentials = response.getData().loginUser.employee.credentials.toString();
                            Employee.names = response.getData().loginUser.employee.names.toString();
                            Employee.lastnames = response.getData().loginUser.employee.lastNames.toString();
                            Employee.phoneNumber = response.getData().loginUser.employee.phoneNumber.toString();
                            Employee.emailAddress = response.getData().loginUser.employee.emailAddress.toString();
                            Employee.departmentId = response.getData().loginUser.employee.departmentId;
                            Employee.departmentName = response.getData().loginUser.employee.departmentName.toString();

                            Intent intent = new Intent(LoginPage.this, MainActivity.class);
                            startActivity(intent);
                        }

                        @Override
                        public void onFailure(@NotNull ApolloException e) {
                            e.printStackTrace();
                            Toast.makeText(LoginPage.this, "Error in the server response", Toast.LENGTH_SHORT).show();
                        }
                    });

            Toast.makeText(this, "name of the user is: "+Employee.names, Toast.LENGTH_SHORT).show();
        }catch (Exception e){
            e.printStackTrace();
            Toast.makeText(this, "Error in connection with the server", Toast.LENGTH_SHORT).show();
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
        actionBar.setBackgroundDrawable(new ColorDrawable(Color.parseColor("#273036")));
        actionBar.setTitle("Pure Mango");

        userField = (TextInputEditText) findViewById(R.id.userField);
        passField = (TextInputEditText) findViewById(R.id.passField);

    }
}