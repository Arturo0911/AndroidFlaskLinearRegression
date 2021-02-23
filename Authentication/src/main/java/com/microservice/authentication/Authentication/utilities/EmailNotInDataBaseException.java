package com.microservice.authentication.Authentication.utilities;

public class EmailNotInDataBaseException extends Exception {

    public EmailNotInDataBaseException(String message){
        super(message);
    }
}
