package io.dutwrapperlib.dutwrapper.objects.accounts;

import java.io.Serializable;

public class ScheduleExam implements Serializable {
    private String group = "";
    private Boolean isGlobal = false;
    private Long date = 0L;
    private String room = "";

    public ScheduleExam() {

    }

    public ScheduleExam(String group, Boolean isGlobal, Long date, String room) {
        this.group = group;
        this.isGlobal = isGlobal;
        this.date = date;
        this.room = room;
    }

    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }

    public Boolean getIsGlobal() {
        return isGlobal;
    }

    public void setIsGlobal(Boolean isGlobal) {
        this.isGlobal = isGlobal;
    }

    public Long getDate() {
        return date;
    }

    public void setDate(Long date) {
        this.date = date;
    }

    public String getRoom() {
        return room;
    }

    public void setRoom(String room) {
        this.room = room;
    }
}