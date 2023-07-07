package io.dutwrapperlib.dutwrapper.objects.accounts;

import java.io.Serializable;

public class ScheduleItem implements Serializable {
    private Integer dayOfWeek;
    private LessonItem lesson;
    private String room;

    public ScheduleItem() {

    }

    public ScheduleItem(Integer dayOfWeek, LessonItem lesson, String room) {
        this.dayOfWeek = dayOfWeek;
        this.room = room;
        this.lesson = lesson;
    }

    public Integer getDayOfWeek() {
        return dayOfWeek;
    }

    public void setDayOfWeek(Integer dayOfWeek) {
        this.dayOfWeek = dayOfWeek;
    }

    public LessonItem getLesson() {
        return lesson;
    }

    public void setLesson(LessonItem lesson) {
        this.lesson = lesson;
    }

    public String getRoom() {
        return room;
    }

    public void setRoom(String room) {
        this.room = room;
    }


}