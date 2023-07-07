package io.dutwrapperlib.dutwrapper.objects.accounts;

import java.io.Serializable;

public class SubjectFeeItem implements Serializable {
    private SubjectCodeItem id;
    private String name;
    private Integer credit;
    private Boolean isHighQuality;
    private Double price;
    private Boolean debt;
    private Boolean isRestudy;
    private String verifiedPaymentAt;

    public SubjectFeeItem() {

    }

    public SubjectFeeItem(SubjectCodeItem id, String name, Integer credit, Boolean isHighQuality, Double price, Boolean debt,
                          Boolean isRestudy, String verifiedPaymentAt) {
        this.id = id;
        this.name = name;
        this.credit = credit;
        this.isHighQuality = isHighQuality;
        this.price = price;
        this.debt = debt;
        this.isRestudy = isRestudy;
        this.verifiedPaymentAt = verifiedPaymentAt;
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

    public Double getPrice() {
        return price;
    }

    public void setPrice(Double price) {
        this.price = price;
    }

    public Boolean getDebt() {
        return debt;
    }

    public void setDebt(Boolean debt) {
        this.debt = debt;
    }

    public Boolean getIsRestudy() {
        return isRestudy;
    }

    public void setIsRestudy(Boolean isRestudy) {
        this.isRestudy = isRestudy;
    }

    public String getVerifiedPaymentAt() {
        return verifiedPaymentAt;
    }

    public void setVerifiedPaymentAt(String verifiedPaymentAt) {
        this.verifiedPaymentAt = verifiedPaymentAt;
    }
}