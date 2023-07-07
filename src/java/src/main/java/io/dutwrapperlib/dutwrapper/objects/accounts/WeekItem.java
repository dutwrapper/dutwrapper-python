package io.dutwrapperlib.dutwrapper.objects.accounts;

import java.io.Serializable;

public class WeekItem implements Serializable {
    private Integer start;
    private Integer end;

    public WeekItem() {

    }

    public WeekItem(Integer start, Integer end) {
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
}