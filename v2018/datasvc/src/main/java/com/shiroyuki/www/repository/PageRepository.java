package com.shiroyuki.www.repository;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
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

    public Page get(String name) throws Exception {
        return (Page) this.mapper.map(Page.class, this.basePath + "/" + name + ".yml");
    }
}
