package com.microservice.authentication.Authentication.controllers;


import com.microservice.authentication.Authentication.daos.UserDao;
import com.microservice.authentication.Authentication.entities.User;
import com.microservice.authentication.Authentication.services.UserService;
import com.microservice.authentication.Authentication.services.UserServiceImplementation;
import com.microservice.authentication.Authentication.utilities.JsonResponseBody;
import com.microservice.authentication.Authentication.utilities.errorhandlers.UserNotFoundException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpMethod;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;

import javax.validation.Valid;
import java.util.ArrayList;
import java.util.List;

@org.springframework.web.bind.annotation.RestController()
public class RestController {



    @Autowired
    UserService userService;


    @RequestMapping("/init")
    public String initSerivice(){
        return "<h1>Microservice Authentication initialized</h1>";
    }



    @RequestMapping(value = "/login", method = RequestMethod.POST)
    public String login(@RequestParam(value = "email") String email, @RequestParam(value = "password") String password){

        return "the email is: "+email+" and the password is: "+password;
    }



    @RequestMapping(value = "/createUser", method = RequestMethod.POST)
    ResponseEntity<JsonResponseBody> crateUser (@Valid User user){

        try {
            return ResponseEntity.status(HttpStatus.OK).body(new JsonResponseBody(HttpStatus.OK.value(), userService.userAdd(user)));
        }catch (Exception e ){
            e.printStackTrace();
            return ResponseEntity.status(HttpStatus.FORBIDDEN).body(new JsonResponseBody(HttpStatus.FORBIDDEN.value(), "Error by: "+e.toString()));
        }
    }

    @RequestMapping(value = "/showUsers", method = RequestMethod.GET)
    ResponseEntity<JsonResponseBody> getAllUsers(){

        return ResponseEntity.status(HttpStatus.OK).body(new JsonResponseBody(HttpStatus.OK.value(), userService.getAllUsers()));
    }


    /**
     *
     * @param user object to create new instance
     * @param result catching al possible errors
     * @return return null for now
     */
    @RequestMapping(value = "/newUser", method = RequestMethod.POST)
    ResponseEntity<JsonResponseBody>createNewUser(@Valid User user, BindingResult result){

        if (result.hasErrors()) {
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(new JsonResponseBody(HttpStatus.BAD_REQUEST.value(), "Error: "+result.hasErrors()));
        }
        return null;
    }

}
