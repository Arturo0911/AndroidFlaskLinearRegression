package com.microservice.authentication.Authentication.services;

import com.microservice.authentication.Authentication.daos.CustomersDao;
import com.microservice.authentication.Authentication.daos.ProductDao;
import com.microservice.authentication.Authentication.daos.SalesDao;
import com.microservice.authentication.Authentication.entities.Customers;
import com.microservice.authentication.Authentication.entities.Product;
import com.microservice.authentication.Authentication.entities.Sales;
import com.microservice.authentication.Authentication.utilities.errorhandlers.CustomerNotFoundException;
import com.microservice.authentication.Authentication.utilities.errorhandlers.ProductNotInDatabase;
import com.microservice.authentication.Authentication.utilities.errorhandlers.SalesNotMatchException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class ProductSalesServiceImplementation implements ProductSalesService {

    @Autowired
    ProductDao productDao;

    @Autowired
    CustomersDao customersDao;

    @Autowired
    SalesDao salesDao;



    @Override
    public List<Product> findAllProducts() {
        return productDao.findAll();
    }

    @Override
    public List<Customers> findAllCustomers() {
        return customersDao.findAll();
    }

    @Override
    public List<Sales> findAllSales() {
        return salesDao.findAll();
    }

    /**
     *
     * @param productCode every product has a code
     * @return return the object Product found
     * @throws ProductNotInDatabase exception if the product code if wrong
     */
    @Override
    public Optional<Product> findProductByCode(String productCode) throws ProductNotInDatabase {
        Optional<Product> products = productDao.findProductByCode(productCode);
        if (products.isPresent()){
            Product product = products.get();
            if (product == null){
                throw new ProductNotInDatabase("The product code doesn't match anything");
            }
        }
        return products;
    }

    @Override
    public Optional<Sales> findSalesByProduct(String productName) throws SalesNotMatchException {
        Optional<Sales> saless = salesDao.findSalesByProduct(productName);
        if (saless.isPresent()){
            Sales sales = saless.get();
            if (sales == null){
                throw new SalesNotMatchException("The product code doesn't match anything");
            }
        }
        return saless;
    }

    @Override
    public Optional<Customers> findCustomersBy(String credentials) throws CustomerNotFoundException {
        Optional<Customers> customerss = customersDao.findByCredentials(credentials);
        if(customerss.isPresent()){
            Customers customers = customerss.get();
            if(customers == null) throw new CustomerNotFoundException("Customer did'nt matched");
        }
        return customerss;
    }
}
