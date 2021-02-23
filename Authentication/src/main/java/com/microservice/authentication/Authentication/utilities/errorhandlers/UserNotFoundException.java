package com.microservice.authentication.Authentication.utilities.errorhandlers;

public class UserNotFoundException extends Exception {
    public UserNotFoundException(String message){
        super(message);
    }
}
