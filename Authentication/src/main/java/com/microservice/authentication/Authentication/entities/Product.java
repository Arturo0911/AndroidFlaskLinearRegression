package com.microservice.authentication.Authentication.entities;


import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import javax.persistence.*;
import javax.validation.constraints.NotBlank;
import javax.validation.constraints.NotEmpty;
import javax.validation.constraints.NotNull;
import java.util.Date;
import java.util.HashSet;
import java.util.Set;

@Entity
@Table(name = "products")
@AllArgsConstructor @NoArgsConstructor
public class Product {

    @Id
    @Column(name = "ID_PRODUCT")
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Getter @Setter
    private Integer idProduct;

    @ManyToMany(mappedBy = "productsSold")
    @Getter @Setter
    private Set<Sales> sales = new HashSet<>();



    @Column(name = "PRODUCT_NAME", length = 25)
    @Getter @Setter
    @NotNull @NotEmpty @NotBlank
    private String productName;

    @Column(name = "PRODUCT_CODE", length = 25)
    @Getter @Setter
    @NotNull @NotEmpty @NotBlank
    private String productCode;

    @Column(name = "DESCRIPTION", length = 100)
    @Getter @Setter
    @NotNull @NotEmpty @NotBlank
    private String description;

    @Column(name = "DATE")
    @Getter @Setter
    private Date date;

    @Column(name = "STOCK")
    @Getter @Setter
    @NotNull @NotEmpty @NotBlank
    private long stock;


}
