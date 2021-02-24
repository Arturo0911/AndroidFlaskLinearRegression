package com.microservice.authentication.Authentication.entities;


import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;
import javax.validation.constraints.NotBlank;
import javax.validation.constraints.NotEmpty;
import javax.validation.constraints.NotNull;
import java.util.Date;

@Entity
@Table(name = "products")
@AllArgsConstructor @NoArgsConstructor
public class Product {

    @Id
    @Column(name = "ID_PRODUCT")
    private Integer idProduct;

    @Column(name = "PRODUCT_NAME")
    @Getter @Setter
    @NotNull @NotEmpty @NotBlank
    private String productName;

    @Column(name = "PRODUCT_CODE")
    @Getter @Setter
    @NotNull @NotEmpty @NotBlank
    private String productCode;

    @Column(name = "DESCRIPTION")
    @Getter @Setter
    @NotNull @NotEmpty @NotBlank
    private String description;

    @Column(name = "DATE")
    @Getter @Setter
    private Date date;


}
