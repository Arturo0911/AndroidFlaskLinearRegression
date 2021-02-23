package com.microservice.authentication.Authentication.entities;


import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import javax.persistence.*;
import javax.validation.constraints.NotEmpty;
import javax.validation.constraints.NotNull;

@Entity
@Table(name = "users")
@AllArgsConstructor @NoArgsConstructor
public class User {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "ID")
    private Integer id;

    @Column(name = "CREDENTIALS", length = 25)
    @Getter @Setter
    @NotEmpty @NotEmpty @NotNull
    private String credentials;

    @Column(name = "NAMES", length = 50)
    @Getter @Setter
    @NotEmpty @NotEmpty @NotNull
    private String names;

    @Column(name = "LAST_NAMES", length = 50)
    @Getter @Setter
    @NotEmpty @NotEmpty @NotNull
    private String lastNames;

    @Column(name = "DEPARTMENT_NAME", length = 50)
    @Getter @Setter
    @NotEmpty @NotEmpty @NotNull
    private String departmentName;

    @Column(name = "PHONENUMBER", length = 25)
    @Getter @Setter
    @NotEmpty @NotEmpty @NotNull
    private String phoneNumber;

    @Column(name = "EMAIL", length = 50)
    @Getter @Setter
    @NotEmpty @NotEmpty @NotNull
    private String email;

    @Column(name = "PASSWORD", length = 100)
    @Getter @Setter
    @NotEmpty @NotEmpty @NotNull
    private String password;


}
