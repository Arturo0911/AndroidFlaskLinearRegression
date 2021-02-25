package com.microservice.authentication.Authentication.daos;

import com.microservice.authentication.Authentication.entities.Product;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;

@Repository
public interface ProductDao extends JpaRepository<Product, Integer> {

    @Query(value = "SELECT * FROM products WHERE PRODUCT_CODE =:productCode;", nativeQuery = true)
    Optional<Product> findProductByCode(String productCode);


}
