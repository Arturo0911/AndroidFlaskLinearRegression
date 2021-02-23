package com.microservice.authentication.Authentication.services;

import com.microservice.authentication.Authentication.entities.User;
import com.microservice.authentication.Authentication.utilities.errorhandlers.EmailNotInDataBaseException;
import com.microservice.authentication.Authentication.utilities.errorhandlers.UserNotFoundException;

import java.util.ArrayList;
import java.util.Optional;

/**
 * @author Arthur Payload
 */


public interface UserService {

    Optional<User> getUserFromDb(String email, String password) throws EmailNotInDataBaseException;
    ArrayList<User> getAllUsers();
    User userAdd(User user) throws UserNotFoundException;
    void deleteUserByEmail(String email) throws UserNotFoundException;

}
