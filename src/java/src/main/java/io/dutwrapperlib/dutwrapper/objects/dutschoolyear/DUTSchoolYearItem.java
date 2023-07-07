package io.dutwrapperlib.dutwrapper.objects.dutschoolyear;

import java.io.Serializable;

public class DUTSchoolYearItem implements Serializable {
    private String name;
    private Integer year;
    private Long start;

    public DUTSchoolYearItem(String name, Integer year, Long start) {
        this.name = name;
        this.year = year;
        this.start = start;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Integer getYear() {
        return year;
    }

    public void setYear(Integer year) {
        this.year = year;
    }

    public Long getStart() {
        return start;
    }

    public void setStart(Long start) {
        this.start = start;
    }
}