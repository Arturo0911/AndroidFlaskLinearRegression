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
@Table(name = "sales")
@AllArgsConstructor @NoArgsConstructor
public class Sales {


    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Getter @Setter
    @Column(name = "ID_SALES")
    private Integer idSales;

    @ManyToMany//(fetch = FetchType.LAZY, cascade =  CascadeType.ALL)
    @JoinTable(name = "sales_description",
            joinColumns = @JoinColumn(name = "SALES_ID") ,
            inverseJoinColumns = @JoinColumn(name = "PRODUCT_ID"))
    @Getter @Setter
    private Set<Product> productsSold = new HashSet<>();


    @Column(name = "PRODUCT_NAME", length = 50)
    @Getter @Setter
    @NotNull @NotEmpty @NotBlank
    private String productName;

    @Column(name = "PRODUCT_CODE", length = 50)
    @Getter @Setter
    @NotNull @NotEmpty @NotBlank
    private String productCode;


    @Column(name = "DATE_SALES")
    @Getter @Setter
    private Date dateSales;

    @Column(name = "QUANTITY")
    @Getter @Setter
    @NotNull @NotEmpty @NotBlank
    private long quantity;

    @Column(name = "CUSTOMER_NAME", length = 50)
    @Getter @Setter
    @NotNull @NotEmpty @NotBlank
    private String customersName;

    @Column(name = "PRODUCT_LAST_NAME", length = 50)
    @Getter @Setter
    @NotNull @NotEmpty @NotBlank
    private String customersLastName;

    @Column(name = "CREDENTIAL", length = 50)
    @Getter @Setter
    @NotNull @NotEmpty @NotBlank
    private String credential;

    @Column(name = "SALE_DESCRIPTION", length = 50)
    @Getter @Setter
    @NotNull @NotEmpty @NotBlank
    private String descriptionSale;


    @PrePersist
    private void initDate(){
        this.dateSales = new Date();
    }


}
