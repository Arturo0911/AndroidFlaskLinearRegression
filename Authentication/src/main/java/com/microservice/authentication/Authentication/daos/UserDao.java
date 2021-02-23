package com.microservice.authentication.Authentication.daos;

import com.microservice.authentication.Authentication.entities.User;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.ArrayList;
import java.util.Optional;


public interface UserDao extends JpaRepository<User, Integer> {

    Optional<User> findUserByEmail(String email);

    /**
     *
     * @return An ArrayList with all the users stored in data base
     */
    ArrayList<User> findAllUsers();

}
