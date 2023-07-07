package io.dutwrapperlib.dutwrapper.customrequest;

import java.io.Serializable;
import java.io.UnsupportedEncodingException;
import java.net.URLEncoder;
import java.util.ArrayList;

public class CustomRequestList implements Serializable {
    ArrayList<CustomRequestItem> httpRequestParameters = null;

    public CustomRequestList() {
        this.httpRequestParameters = new ArrayList<CustomRequestItem>();
    }

    public CustomRequestList(ArrayList<CustomRequestItem> array) {
        this.httpRequestParameters = array;
    }

    public void addRequest(CustomRequestItem param) {
        this.httpRequestParameters.add(param);
    }

    public CustomRequestItem getRequests(int position) {
        return this.httpRequestParameters.get(position);
    }

    public void removeRequests(int position) {
        this.httpRequestParameters.remove(position);
    }

    public void removeRequests(Object obj) {
        this.httpRequestParameters.remove(obj);
    }

    public String toURLEncode() throws NullPointerException, UnsupportedEncodingException {
        String request = "";

        Boolean first = true;

        if (httpRequestParameters == null)
            throw new NullPointerException("HttpRequestParameters is null!");

        for (CustomRequestItem item : httpRequestParameters) {
            if (!first)
                request += "&";
            else first = false;

            request += URLEncoder.encode(item.getName(), "UTF-8")
                    + "="
                    + URLEncoder.encode(item.getValue(), "UTF-8");
        }

        return request;
    }

    public byte[] toURLEncodeByteArray(String charsetName) throws UnsupportedEncodingException {
        return this.toURLEncode().getBytes(charsetName);
    }
}
