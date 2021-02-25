package com.microservice.authentication.Authentication.daos;

import com.microservice.authentication.Authentication.entities.Sales;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;

@Repository
public interface SalesDao extends JpaRepository<Sales, Integer> {

    @Query(value = "SELECT * FROM sales WHERE PRODUCT_NAME =:productName;", nativeQuery = true)
    Optional<Sales> findSalesByProduct(String productName);
}
