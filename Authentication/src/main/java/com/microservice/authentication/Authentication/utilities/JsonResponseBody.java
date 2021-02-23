package com.microservice.authentication.Authentication.utilities;


import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@AllArgsConstructor @NoArgsConstructor
public class JsonResponseBody {


    @Setter @Getter
    private int server;

    @Setter @Getter
    private Object response;
}
