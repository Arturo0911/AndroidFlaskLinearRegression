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
@Table(name = "customers")
@AllArgsConstructor @NoArgsConstructor
public class Customers {

    @Id
    @Column(name = "ID")
    @Getter @Setter
    private Integer id;

    @Column(name = "NAMES")
    @Setter @Getter
    @NotEmpty @NotNull @NotBlank
    private String names;

    @Column(name = "LAST_NAMES")
    @Setter @Getter
    @NotEmpty @NotNull @NotBlank
    private String lastNames;

    @Column(name = "CREDENTIALS")
    @Setter @Getter
    @NotEmpty @NotNull @NotBlank
    private String credentials;
    

    @Column(name = "EMAIL")
    @Setter @Getter
    @NotEmpty @NotNull @NotBlank
    private String email;

    @Column(name = "PHONE_NUMBER")
    @Setter @Getter
    @NotEmpty @NotNull @NotBlank
    private String phoneNumber;

    @Column(name = "BIRTH_DATE")
    @Setter @Getter
    @NotEmpty @NotNull @NotBlank
    private Date birthDate;


}
