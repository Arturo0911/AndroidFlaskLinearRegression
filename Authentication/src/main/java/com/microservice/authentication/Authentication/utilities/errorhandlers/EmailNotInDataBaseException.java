package com.microservice.authentication.Authentication.utilities.errorhandlers;

public class EmailNotInDataBaseException extends Exception {

    public EmailNotInDataBaseException(String message){
        super(message);
    }
}
