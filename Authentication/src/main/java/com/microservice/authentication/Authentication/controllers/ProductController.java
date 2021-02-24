package com.microservice.authentication.Authentication.controllers;


import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController()
@RequestMapping("/product")
public class ProductController {


    @RequestMapping("/initProduct")
    public String product(){
        return "Hello product";
    }
}
