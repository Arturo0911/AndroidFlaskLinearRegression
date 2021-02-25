package com.microservice.authentication.Authentication.daos;

import com.microservice.authentication.Authentication.entities.Product;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface ProductDao extends JpaRepository<Product, Integer> {
}
