package io.dutwrapperlib.dutwrapper.objects.accounts;

import java.io.Serializable;

public class SubjectScheduleItem implements Serializable {
    private SubjectCodeItem id;
    private String name;
    private Integer credit;
    private Boolean isHighQuality;
    private String lecturer;
    private ScheduleStudy subjectStudy;
    private ScheduleExam subjectExam;
    private String pointFormula;

    public SubjectScheduleItem() {

    }

    public SubjectScheduleItem(SubjectCodeItem id, String name, Integer credit, Boolean isHighQuality,
                               ScheduleStudy subjectStudy, ScheduleExam subjectExam) {
        this.id = id;
        this.name = name;
        this.credit = credit;
        this.isHighQuality = isHighQuality;
        this.subjectStudy = subjectStudy;
        this.subjectExam = subjectExam;
    }

    public SubjectCodeItem getId() {
        return id;
    }

    public void setId(SubjectCodeItem id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Integer getCredit() {
        return credit;
    }

    public void setCredit(Integer credit) {
        this.credit = credit;
    }

    public Boolean getIsHighQuality() {
        return isHighQuality;
    }

    public void setIsHighQuality(Boolean isHighQuality) {
        this.isHighQuality = isHighQuality;
    }

    public String getLecturer() {
        return lecturer;
    }

    public void setLecturer(String lecturer) {
        this.lecturer = lecturer;
    }

    public ScheduleStudy getSubjectStudy() {
        return subjectStudy;
    }

    public void setSubjectStudy(ScheduleStudy subjectStudy) {
        this.subjectStudy = subjectStudy;
    }

    public ScheduleExam getSubjectExam() {
        return subjectExam;
    }

    public void setSubjectExam(ScheduleExam subjectExam) {
        this.subjectExam = subjectExam;
    }

    public String getPointFormula() {
        return pointFormula;
    }

    public void setPointFormula(String pointFormula) {
        this.pointFormula = pointFormula;
    }
}