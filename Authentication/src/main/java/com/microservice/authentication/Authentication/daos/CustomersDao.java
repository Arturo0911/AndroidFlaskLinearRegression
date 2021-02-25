package com.microservice.authentication.Authentication.daos;

import com.microservice.authentication.Authentication.entities.Customers;
import org.springframework.data.jpa.repository.JpaRepository;

public interface CustomersDao extends JpaRepository<Customers, Integer> {
}
