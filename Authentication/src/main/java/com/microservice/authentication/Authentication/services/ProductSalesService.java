package com.microservice.authentication.Authentication.services;

import com.microservice.authentication.Authentication.entities.Customers;
import com.microservice.authentication.Authentication.entities.Product;
import com.microservice.authentication.Authentication.entities.Sales;
import com.microservice.authentication.Authentication.utilities.errorhandlers.CustomerNotFoundException;
import com.microservice.authentication.Authentication.utilities.errorhandlers.ProductNotInDatabase;
import com.microservice.authentication.Authentication.utilities.errorhandlers.SalesNotMatchException;

import java.util.List;
import java.util.Optional;

public interface ProductSalesService {

    List<Product> findAllProducts();
    List<Customers> findAllCustomers();
    List<Sales> findAllSales();
    Optional<Product> findProductByCode(String productCode) throws ProductNotInDatabase;
    Optional<Sales> findSalesByProduct(String productName) throws SalesNotMatchException, ProductNotInDatabase;
    Optional<Customers> findCustomersBy(String credentials) throws CustomerNotFoundException;




}
