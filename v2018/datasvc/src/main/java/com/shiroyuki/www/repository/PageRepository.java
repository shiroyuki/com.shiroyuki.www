package com.shiroyuki.www.repository;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.stereotype.Component;

import com.shiroyuki.www.model.Page;
import com.shiroyuki.www.service.YamlMapper;

@Component
public class PageRepository {
    private YamlMapper mapper;

    @Value("${STATIC_PAGE_DATA_PATH}")
    private String basePath;

    @Autowired
    public PageRepository(YamlMapper mapper) {
        this.mapper = mapper;
    }

    @PreAuthorize("hasAnyRole('ROLE_VISITOR', 'ROLE_ADMIN')")
    public Page getEnglish(String name) throws Exception {
        return this.get("en", name);
    }

    @PreAuthorize("hasRole('ROLE_ADMIN')")
    public Page getJapanese(String name) throws Exception {
        return this.get("jp", name);
    }

    public Page get(String locale, String name) throws Exception {
        System.out.println(String.format("LOCALE: %s, NAME: %s", locale, name));

        return (Page) this.mapper.map(Page.class, this.basePath + "/" + locale + "/" + name + ".yml");
    }
}
