package com.shiroyuki.www.service;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.shiroyuki.www.model.Page;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Component;
import java.io.File;

@Component
public class YamlMapper {
    private ObjectMapper mapper;

    @Autowired
    @Qualifier("yaml")
    public void setYamlObjectMapper(ObjectMapper mapper) {
        this.mapper = mapper;
    }

    public Object map(Class<?> cls, String path) throws Exception {
        return this.mapper.readValue(new File(path), cls);
    }
}
