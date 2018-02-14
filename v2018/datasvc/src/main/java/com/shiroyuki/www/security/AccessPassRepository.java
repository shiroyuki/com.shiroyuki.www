package com.shiroyuki.www.security;

import org.springframework.stereotype.Component;

import com.shiroyuki.www.security.model.AccessPass;

@Component
public class AccessPassRepository {
    public AccessPass findByAppKey(String username) {
        return new AccessPass(username);
    }
}
