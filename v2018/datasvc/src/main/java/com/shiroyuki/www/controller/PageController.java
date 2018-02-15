package com.shiroyuki.www.controller;

import static org.springframework.web.bind.annotation.RequestMethod.GET;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.shiroyuki.www.model.Page;
import com.shiroyuki.www.repository.PageRepository;

@RestController
@RequestMapping("/v1/data/pages/{locale}/{name}")
public class PageController {
    private PageRepository pageRepository;

    @Autowired
    public void setPageRepository(PageRepository pageRepository) {
        this.pageRepository = pageRepository;
    }

    @RequestMapping(method = GET)
    public Page pages(@PathVariable("locale") String locale, @PathVariable("name") String name) {
        try {
            System.out.println("0");
            switch (locale.toLowerCase()) {
            case "en": System.out.println("X-1"); return this.pageRepository.getEnglish(name);
            case "jp": System.out.println("X-2"); return this.pageRepository.getJapanese(name);
            }
        } catch (Exception exception) {
            System.out.println("X-3");
            return new Page(exception.getMessage());
        }

        System.out.println("X-4");

        return new Page("not translated");
    }
}
