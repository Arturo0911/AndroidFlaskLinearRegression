package com.example.puremango;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Toast;

import com.apollographql.apollo.ApolloCall;
import com.apollographql.apollo.ApolloClient;
import com.apollographql.apollo.api.Response;
import com.apollographql.apollo.exception.ApolloException;
import com.google.android.material.textfield.TextInputEditText;

import org.jetbrains.annotations.NotNull;

public class EditProfile extends AppCompatActivity {

    TextInputEditText credentialsEdit;
    TextInputEditText namesEdit;
    TextInputEditText lastnameEdit;
    TextInputEditText emailFieldEdit;
    TextInputEditText phoneNumberEdit;
    //TextInputEditText departmentNameEdit;
    TextInputEditText usernameFieldEdit;
    TextInputEditText passWordEdit;
    TextInputEditText repeatPassword;

    public void editProfile(View view){

        String credentials = credentialsEdit.getText().toString();
        String names = namesEdit.getText().toString();
        String lastNames = lastnameEdit.getText().toString();
        String email = emailFieldEdit.getText().toString();
        String phonenumber = phoneNumberEdit.getText().toString();
        String username = usernameFieldEdit.getText().toString();
        String password = passWordEdit.getText().toString();


        if (notEmptyFields(credentialsEdit,namesEdit, lastnameEdit,emailFieldEdit, phoneNumberEdit, usernameFieldEdit, passWordEdit, repeatPassword)){
            if (passWordEdit.getText().toString().equals(repeatPassword.getText().toString())){
                try {
                    ApolloClient apolloClient = ApolloClient.builder()
                            .serverUrl(ConnectionServer.urlServer)
                            .build();
                    apolloClient.mutate(new UpdateUsersMutation(credentials, names, lastNames, phonenumber, email, username, password))
                            .enqueue(new ApolloCall.Callback<UpdateUsersMutation.Data>() {
                                @Override
                                public void onResponse(@NotNull Response<UpdateUsersMutation.Data> response) {

                                }

                                @Override
                                public void onFailure(@NotNull ApolloException e) {

                                }
                            });

                    Toast.makeText(this, "Datos actualizados satisfactoriamente", Toast.LENGTH_SHORT).show();
                    Employee.credentials = credentials;
                    Employee.names = names;
                    Employee.lastnames = lastNames;
                    Employee.phoneNumber = phonenumber;
                    Employee.emailAddress = email;
                    clearFields(credentialsEdit,namesEdit, lastnameEdit,emailFieldEdit, phoneNumberEdit, usernameFieldEdit, passWordEdit, repeatPassword);
                    Intent intent = new Intent(EditProfile.this, LoginPage.class);
                    startActivity(intent);
                }catch (Exception e){
                    Toast.makeText(this, "Error al actualizar los datos", Toast.LENGTH_SHORT).show();
                }
            }else{
                Toast.makeText(this, "Las contraseñas deben ser iguales", Toast.LENGTH_SHORT).show();
            }
        }else{
            Toast.makeText(this, "Los campos no pueden estar vacios", Toast.LENGTH_SHORT).show();
        }
    }

    public void cancelEdit(View view){
        Intent intent = new Intent(EditProfile.this, MainActivity.class);
        startActivity(intent);
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_edit_profile);

        credentialsEdit = (TextInputEditText) findViewById(R.id.credentialsEdit);
        namesEdit = (TextInputEditText) findViewById(R.id.namesEdit);
        lastnameEdit = (TextInputEditText) findViewById(R.id.lastnameEdit);
        emailFieldEdit= (TextInputEditText) findViewById(R.id.emailFieldEdit);
        phoneNumberEdit= (TextInputEditText) findViewById(R.id.phoneNumberEdit);

        usernameFieldEdit= (TextInputEditText) findViewById(R.id.usernameFieldEdit);
        passWordEdit= (TextInputEditText) findViewById(R.id.passWordEdit);
        repeatPassword= (TextInputEditText) findViewById(R.id.repeatPassword);


        credentialsEdit.setText(Employee.credentials);
        namesEdit.setText(Employee.names);
        lastnameEdit.setText(Employee.lastnames);
        emailFieldEdit.setText(Employee.emailAddress);
        phoneNumberEdit.setText(Employee.phoneNumber);
        usernameFieldEdit.setText(Employee.username);

    }

    public boolean notEmptyFields(TextInputEditText credentials, TextInputEditText names,
                                  TextInputEditText lastnames, TextInputEditText phoneNumber, TextInputEditText emailField,
                                  TextInputEditText usernameField, TextInputEditText passWord, TextInputEditText repeatPassword){

        if (!credentials.getText().toString().equals("")&& !names.getText().toString().equals("" )&&!lastnames.getText().toString().equals("")
                &&!phoneNumber.getText().toString().equals("") &&!emailField.getText().toString().equals("") &&!usernameField.getText().toString().equals("")
                &&!passWord.getText().toString().equals("") &&!repeatPassword.getText().toString().equals("")) {
            return true;
        }else{
            return false;
        }

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
}