package io.dutwrapperlib.dutwrapper.customrequest;

import java.io.Serializable;

import io.dutwrapperlib.dutwrapper.Utils;

public class CustomResponse implements Serializable {
    private Integer returnCode;
    private String contentHtmlString;
    private String sessionId;
    private Long responseUnix;

    public CustomResponse() {
    }

    public CustomResponse(Integer returnCode, String contentHtmlString, String sessionId) {
        this.returnCode = returnCode;
        this.contentHtmlString = contentHtmlString;
        this.sessionId = sessionId;
        this.responseUnix = Utils.getCurrentTimeInUnix();
    }

    public Integer getReturnCode() {
        return returnCode;
    }

    public void setReturnCode(Integer returnCode) {
        this.returnCode = returnCode;
    }

    public String getContentHtmlString() {
        return contentHtmlString;
    }

    public void getContentHtmlString(String contentString) {
        this.contentHtmlString = contentString;
    }

    public String getSessionId() {
        return sessionId;
    }

    public void setSessionId(String sessionId) {
        this.sessionId = sessionId;
    }

    public Long getResponseUnix() {
        return responseUnix;
    }
}
