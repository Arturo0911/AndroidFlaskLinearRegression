package com.microservice.authentication.Authentication.utilities.errorhandlers;

public class ConnectionWithServerException extends  Exception {


    public ConnectionWithServerException(String message){
        super(message);
    }
}
