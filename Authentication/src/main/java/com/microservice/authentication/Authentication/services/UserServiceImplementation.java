package com.microservice.authentication.Authentication.services;

import com.microservice.authentication.Authentication.daos.UserDao;
import com.microservice.authentication.Authentication.entities.User;
import com.microservice.authentication.Authentication.utilities.errorhandlers.EmailNotInDataBaseException;
import com.microservice.authentication.Authentication.utilities.errorhandlers.UserNotFoundException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.Optional;

/**
 * @author Arthur Payload
 * @version 1.0.0
 */

@Service
public class UserServiceImplementation implements UserService {

    @Autowired
    UserDao userDao;

    /**
     *
     * @param email email
     * @param password password
     * @return the user matched with the values above, and this is for the login
     * @throws EmailNotInDataBaseException even if the user doesn't exists
     */
    @Override
    public Optional<User> getUserFromDb(String email, String password) throws EmailNotInDataBaseException {

        Optional<User> users = userDao.findUserByEmail(email);
        if(users.isPresent()){
            User user = users.get();
            if(!user.getPassword().equals(password)){ throw new EmailNotInDataBaseException("Password doesn't match with the value stored");}
        }
        return users;
    }

    /**
     *
     * @return all the users in the arrayList object
     */

    @Override
    public ArrayList<User> getAllUsers() {
        return userDao.findAll();
    }

    /**
     *
     * @param user new User object
     * @return return the user added in database
     * @throws UserNotFoundException
     */
    @Override
    public User userAdd(User user) {
        return userDao.save(user);
    }

    /**
     *
     * @param email email for search and delete
     * @throws UserNotFoundException in case that the user not in database
     */
    @Override
    public void deleteUserByEmail(String email) {
        userDao.deleteByEmail(email);
    }
}
