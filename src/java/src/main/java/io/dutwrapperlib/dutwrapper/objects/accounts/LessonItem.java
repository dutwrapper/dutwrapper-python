package io.dutwrapperlib.dutwrapper.objects.accounts;

import java.io.Serializable;

public class LessonItem implements Serializable {
    private Integer start;
    private Integer end;

    public LessonItem() {

    }

    public LessonItem(Integer start, Integer end) {
        this.start = start;
        this.end = end;
    }

    public Integer getStart() {
        return start;
    }

    public void setStart(Integer start) {
        this.start = start;
    }

    public Integer getEnd() {
        return end;
    }

    public void setEnd(Integer end) {
        this.end = end;
    }

    @Override
    public String toString() {
        return String.format("%d-%d", start, end);
    }
}