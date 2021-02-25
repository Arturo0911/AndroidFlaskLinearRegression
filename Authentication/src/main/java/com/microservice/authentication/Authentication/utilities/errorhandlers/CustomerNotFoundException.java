package com.microservice.authentication.Authentication.utilities.errorhandlers;

public class CustomerNotFoundException extends Exception {

    public CustomerNotFoundException(String message){
        super(message);
    }
}
