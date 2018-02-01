package com.shiroyuki.www.repository;

import com.shiroyuki.www.model.Page;
import com.shiroyuki.www.service.YamlMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import java.io.File;

@Component
public class PageRepository {
    private YamlMapper mapper;

    @Autowired
    public PageRepository(YamlMapper mapper) {
        this.mapper = mapper;
    }

    public Page get(String name) throws Exception {
        return (Page) this.mapper.map(Page.class, "../data/static/pages/en/" + name + ".yml");
    }
}
