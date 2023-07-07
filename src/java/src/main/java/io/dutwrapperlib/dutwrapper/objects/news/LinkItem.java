package io.dutwrapperlib.dutwrapper.objects.news;

import java.io.Serializable;

public class LinkItem implements Serializable {
    private String text;
    private String url;
    private Integer position;

    public LinkItem() {

    }

    public LinkItem(String text, String url, Integer position) {
        this.text = text;
        this.url = url;
        this.position = position;
    }

    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }

    public Integer getPosition() {
        return position;
    }

    public void setPosition(Integer position) {
        this.position = position;
    }
}
