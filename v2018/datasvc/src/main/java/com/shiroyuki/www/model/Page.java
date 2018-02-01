package com.shiroyuki.www.model;

public class Page {
    private final String title;

    public Page() {
        this.title = null;
    }

    public Page(String title) {
        this.title = title;
    }

    public String getTitle() {
        return this.title;
    }
}
