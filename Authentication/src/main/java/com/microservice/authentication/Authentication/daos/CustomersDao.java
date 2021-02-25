package com.microservice.authentication.Authentication.daos;

import com.microservice.authentication.Authentication.entities.Customers;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import java.util.Optional;

@Repository
public interface CustomersDao extends JpaRepository<Customers, Integer> {

    @Query(value = "SELECT * FROM customers WHERE CREDENTIALS =:credentials;", nativeQuery = true)
    Optional<Customers> findByCredentials(String credentials);
}
