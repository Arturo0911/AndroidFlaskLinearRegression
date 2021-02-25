package com.microservice.authentication.Authentication.daos;

import com.microservice.authentication.Authentication.entities.Sales;
import org.springframework.data.jpa.repository.JpaRepository;

public interface SalesDao extends JpaRepository<Sales, Integer> {
}
