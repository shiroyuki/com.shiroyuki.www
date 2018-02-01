package com.shiroyuki.www.controller;

import static org.springframework.web.bind.annotation.RequestMethod.GET;

import com.shiroyuki.www.repository.PageRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import com.shiroyuki.www.model.Page;

import java.awt.*;

@RestController
@RequestMapping("/v1/data/pages")
public class PageController {
    private PageRepository pageRepository;

    @Autowired
    public void setPageRepository(PageRepository pageRepository) {
        this.pageRepository = pageRepository;
    }

    @RequestMapping(method = GET)
    public Page pages() throws Exception {
        // return new Page("ジュティでございます。");
        return this.pageRepository.get("sample");
    }
}
