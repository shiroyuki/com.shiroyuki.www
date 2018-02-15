package com.shiroyuki.www.security;

import java.io.IOException;
import java.util.ArrayList;

import javax.servlet.FilterChain;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.security.web.authentication.www.BasicAuthenticationFilter;

import com.shiroyuki.www.model.security.Authority;

import io.jsonwebtoken.Claims;
import io.jsonwebtoken.Jwts;

public class AuthorizationFilter extends BasicAuthenticationFilter {
    private static final String SECRET = "secret";
    private static final String HEADER_STRING = "Authorization";
    private static final String TOKEN_PREFIX = "Bearer ";

    private static final Authority visitorAuthority = new Authority("ROLE_VISITOR");
    private static final Authority adminAuthority = new Authority("ROLE_ADMIN");

    public AuthorizationFilter(AuthenticationManager authManager) {
        super(authManager);
    }

    @Override
    protected void doFilterInternal(HttpServletRequest req,
                                    HttpServletResponse res,
                                    FilterChain chain) throws ServletException, IOException {
        String header = req.getHeader(HEADER_STRING);

        if (header == null || !header.startsWith(TOKEN_PREFIX)) {
            ArrayList<GrantedAuthority> authorityList = new ArrayList<GrantedAuthority>();
            authorityList.add(visitorAuthority);

            UsernamePasswordAuthenticationToken token = new UsernamePasswordAuthenticationToken("visitor", null, authorityList);

            SecurityContextHolder.getContext().setAuthentication(token);

            chain.doFilter(req, res);

            return;
        }

        UsernamePasswordAuthenticationToken token = this.getAuthentication(req);

        SecurityContextHolder.getContext().setAuthentication(token);
        chain.doFilter(req, res);
    }

    private UsernamePasswordAuthenticationToken getAuthentication(HttpServletRequest request) {
        String token = request.getHeader(HEADER_STRING);

        if (token == null) {
            return null;
        }

        // parse the token.
        Claims claim = Jwts.parser()
                .setSigningKey(SECRET.getBytes())
                .parseClaimsJws(token.replace(TOKEN_PREFIX, ""))
                .getBody();

        if (claim == null) {
            return null;
        }

        ArrayList<GrantedAuthority> authorityList = new ArrayList<GrantedAuthority>();
        authorityList.add(adminAuthority);

        return new UsernamePasswordAuthenticationToken(claim, null, authorityList);
    }
}
