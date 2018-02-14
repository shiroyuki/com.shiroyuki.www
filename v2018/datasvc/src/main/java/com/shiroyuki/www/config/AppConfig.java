package com.shiroyuki.www.config;

import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.EnableAspectJAutoProxy;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.dataformat.yaml.YAMLFactory;
import org.springframework.context.annotation.Primary;

@Configuration
@EnableAspectJAutoProxy
@ComponentScan
public class AppConfig {
    @Bean
    @Primary
    @Qualifier("json")
    public ObjectMapper objectMapper() {
        ObjectMapper objectMapper = new ObjectMapper();

        return objectMapper;
    }

    @Bean
    public YAMLFactory yamlFactory() {
        return new YAMLFactory();
    }

    @Bean
    @Qualifier("yaml")
    public ObjectMapper yamlObjectMapper(YAMLFactory yamlFactory) {
        return new ObjectMapper(yamlFactory);
    }
}
