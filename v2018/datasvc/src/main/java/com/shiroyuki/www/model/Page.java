package com.shiroyuki.www.model;

import java.util.Date;

public class Page {
    private String title;
    private Date lastLoadedAt;

    public Page() {
        this.title = null;
        this.lastLoadedAt = null;
    }

    public Page(String title) {
        this.title = title;
        this.lastLoadedAt = null;
    }

    public String getTitle() {
        return this.title;
    }

    public void setTitle(String title) {
        this.title = title; 
    }

    public Date getLastLoadedAt() {
        return lastLoadedAt;
    }

    public void setLastLoadedAt(Date lastLoadedAt) {
        this.lastLoadedAt = lastLoadedAt;
    }
}
