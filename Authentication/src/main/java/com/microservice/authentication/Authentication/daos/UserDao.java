package com.microservice.authentication.Authentication.daos;

import com.microservice.authentication.Authentication.entities.User;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.ArrayList;

public interface UserDao extends JpaRepository<User, Integer> {

    ArrayList<User> findUserByEmail(String email);

}
