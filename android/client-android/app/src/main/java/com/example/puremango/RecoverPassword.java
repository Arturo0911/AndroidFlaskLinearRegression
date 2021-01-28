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

public class RecoverPassword extends AppCompatActivity {

    private TextInputEditText credentialRecoverField;
    public boolean message = true;

    public void onRecoverPassword(View view){
        credentialRecoverField = (TextInputEditText) findViewById(R.id.credentialRecoverField);
        String credential = credentialRecoverField.getText().toString();


        try {
            ApolloClient apolloClient = ApolloClient.builder()
                    .serverUrl(ConnectionServer.urlServer)
                    .build();

            apolloClient.mutate(new RecoverPasswordMutation(credential))
                    .enqueue(new ApolloCall.Callback<RecoverPasswordMutation.Data>() {
                        @Override
                        public void onResponse(@NotNull Response<RecoverPasswordMutation.Data> response) {
                                 //message =  response.getData().;
                            //STATUS MENSAJE DEL SERVIDOR VERDEADERO ES QUE SE PUDO RESTAURAR LA CONTRASEÑA
                            message = response.getData().recoverPassword.statusMessage;
                        }

                        @Override
                        public void onFailure(@NotNull ApolloException e) {
                            throw new RuntimeException(e);
                        }
                    });
        }catch (Exception e ){
            Toast.makeText(this, "Error en la conexión con el servidor", Toast.LENGTH_SHORT).show();
        }


        if (!message){
            Toast.makeText(this, "Error en el servidor", Toast.LENGTH_SHORT).show();
        }else{
            Intent intent = new Intent(RecoverPassword.this, LoginPage.class);
            startActivity(intent);
        }



    }

    public void onCancelButton (View view){
        Intent intent = new Intent(RecoverPassword.this, LoginPage.class);
        startActivity(intent);
    }



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_recover_password);
    }
}