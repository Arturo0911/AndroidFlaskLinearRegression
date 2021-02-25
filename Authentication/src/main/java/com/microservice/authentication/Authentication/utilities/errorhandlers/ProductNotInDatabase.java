package com.microservice.authentication.Authentication.utilities.errorhandlers;

public class ProductNotInDatabase extends Exception {

    public ProductNotInDatabase(String message){
        super(message);
    }
}
