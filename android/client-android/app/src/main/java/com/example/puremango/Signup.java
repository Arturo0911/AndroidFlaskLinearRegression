package com.example.puremango;

import androidx.appcompat.app.ActionBar;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.graphics.Color;
import android.graphics.drawable.ColorDrawable;
import android.os.Bundle;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Spinner;
import android.widget.Toast;

import com.apollographql.apollo.ApolloCall;
import com.apollographql.apollo.ApolloClient;
import com.apollographql.apollo.api.Response;
import com.apollographql.apollo.exception.ApolloException;
import com.google.android.material.textfield.TextInputEditText;

import org.jetbrains.annotations.NotNull;

import java.util.ArrayList;
import java.util.Arrays;

public class Signup extends AppCompatActivity {
    ActionBar actionBar;

    private Spinner departmentName;
    private TextInputEditText credentials;
    private TextInputEditText names;
    private TextInputEditText lastname;
    private TextInputEditText emailField;
    private TextInputEditText phoneNumber;
    private TextInputEditText usernameField;
    private TextInputEditText passWord;
    private TextInputEditText repeatPassword;


    public void saveButtonNewEmployee(View view){
        Toast.makeText(this, "saved button", Toast.LENGTH_SHORT).show();
        int departmentId = 1;

        String credentials_  = credentials.getText().toString();
        String names_  = names.getText().toString();
        String lastnames_  = lastname.getText().toString();
        String phoneNumber_  = emailField.getText().toString();
        String emailAddress_  = phoneNumber.getText().toString();
        String username_  = usernameField.getText().toString();
        String password_  = passWord.getText().toString();
        String repeatPassword_  = repeatPassword.getText().toString();

        if (password_.equals(repeatPassword_)){
            if (departmentName.getSelectedItem().toString().equals("Finanzas")){
                departmentId = 1;
            }else if (departmentName.getSelectedItem().toString().equals("Marketing")){
                departmentId = 3;
            }else if (departmentName.getSelectedItem().toString().equals("Produccion")){
                departmentId = 4;
            }

            RegisterEmployeeServer(credentials_, names_, lastnames_, phoneNumber_, emailAddress_,
                    departmentId, departmentName.getSelectedItem().toString(), username_, password_, ConnectionServer.urlServer);
            clearFields(credentials, names, lastname, phoneNumber, emailField, usernameField, passWord, repeatPassword);
        }else{
            Toast.makeText(this, "Las contraseñas deben ser iguales", Toast.LENGTH_SHORT).show();
        }




        //Finanzas", "IT", "Marketing","Produccion"




    }

    public void onCancelButton(View view){
        //Toast.makeText(this, "cancel button", Toast.LENGTH_SHORT).show();
        Intent intent = new Intent(Signup.this, LoginPage.class);
        clearFields(credentials, names, lastname, phoneNumber, emailField, usernameField, passWord, repeatPassword);
        startActivity(intent);
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_signup);
        actionBar  = getSupportActionBar();
        actionBar.setBackgroundDrawable(new ColorDrawable(Color.parseColor("#273036")));
        actionBar.setTitle("Pure Mango");
        departmentName = (Spinner) findViewById(R.id.departmentName);
        //ArrayList<String> departments = new ArrayList<String>(Arrays.asList("Finanzas", "IT", "Marketing","Produccion" ));
        ArrayAdapter<CharSequence> adapter = ArrayAdapter.createFromResource(this,R.array.departmentsName, R.layout.support_simple_spinner_dropdown_item);
        adapter.setDropDownViewResource(R.layout.support_simple_spinner_dropdown_item);
        departmentName.setAdapter(adapter);

        credentials = (TextInputEditText) findViewById(R.id.credentials);
        names= (TextInputEditText) findViewById(R.id.names);
        lastname= (TextInputEditText) findViewById(R.id.lastname);
        phoneNumber= (TextInputEditText) findViewById(R.id.phoneNumber);
        emailField= (TextInputEditText) findViewById(R.id.emailField);
        usernameField= (TextInputEditText) findViewById(R.id.usernameField);
        passWord= (TextInputEditText) findViewById(R.id.passWord);
        repeatPassword= (TextInputEditText) findViewById(R.id.repeatPassword);



    }

    private void clearFields(TextInputEditText credentials, TextInputEditText names,
                             TextInputEditText lastnames, TextInputEditText phoneNumber, TextInputEditText emailField,
                             TextInputEditText usernameField, TextInputEditText passWord, TextInputEditText repeatPassword ){

        credentials.setText("");
        names.setText("");
        lastnames.setText("");
        phoneNumber.setText("");
        emailField.setText("");
        usernameField.setText("");
        passWord.setText("");
        repeatPassword.setText("");

    }


    private void RegisterEmployeeServer(String credentials, String names, String lastNames,
                                        String phoneNumber, String emailAddress,
                                        Integer departmentId, String departmentName, String username,
                                        String password, String urlServer){

        try {
            ApolloClient apolloClient = ApolloClient.builder()
                    .serverUrl(urlServer)
                    .build();

            apolloClient.mutate(new RegisterEmployeeMutation(credentials, names, lastNames, phoneNumber, emailAddress, departmentId, departmentName, username, password))
                    .enqueue(new ApolloCall.Callback<RegisterEmployeeMutation.Data>() {
                        @Override
                        public void onResponse(@NotNull Response<RegisterEmployeeMutation.Data> response) {

                        }

                        @Override
                        public void onFailure(@NotNull ApolloException e) {

                        }
                    });

            Toast.makeText(this, "Los usuario fue creado satisfactoriamente", Toast.LENGTH_SHORT).show();
        }catch (Exception e){
            e.printStackTrace();
            Toast.makeText(this, "Problemas al conectarse con el servidor", Toast.LENGTH_LONG).show();
        }




    }
}