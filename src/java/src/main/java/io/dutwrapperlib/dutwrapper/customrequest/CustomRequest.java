package io.dutwrapperlib.dutwrapper.customrequest;

import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.RequestBody;
import okhttp3.Response;

import java.io.IOException;
import java.util.Objects;
import java.util.concurrent.TimeUnit;

public class CustomRequest {
    public static CustomResponse get(String cookies, String url, Integer timeout) throws IOException {
        OkHttpClient client = new OkHttpClient.Builder()
                .connectTimeout(timeout, TimeUnit.SECONDS)
                .readTimeout(timeout, TimeUnit.SECONDS)
                .writeTimeout(timeout, TimeUnit.SECONDS)
                .build();
        Request request = new Request.Builder()
                .url(url)
                .addHeader("Cookie", cookies != null ? cookies : "")
                .addHeader("Content-Type", "text/html; charset=utf-8")
                .get()
                .build();

        Response response = client.newCall(request).execute();

        // This is for Session ID getter in Set-Cookie response.
        String cookieResponseHeader = response.headers().get("Set-Cookie");
        String sessionId = getSessionIdFromHeader(cookieResponseHeader);

        // Create a custom response, close response and return.
        CustomResponse customResponse = new CustomResponse(
                response.code(),
                Objects.requireNonNull(response.body()).string(),
                sessionId
        );
        response.close();
        return customResponse;
    }

    public static CustomResponse post(String cookies, String url, byte[] requestBytes, Integer timeout) throws IOException {
        OkHttpClient client = new OkHttpClient.Builder()
                .connectTimeout(timeout, TimeUnit.SECONDS)
                .readTimeout(timeout, TimeUnit.SECONDS)
                .writeTimeout(timeout, TimeUnit.SECONDS)
                .build();

        RequestBody body = RequestBody.create(requestBytes);

        Request request = new Request.Builder()
                .url(url)
                .addHeader("Cookie", cookies != null ? cookies : "")
                .addHeader("content-type", "application/x-www-form-urlencoded; charset=UTF-8")
                .post(body)
                .build();

        Response response = client.newCall(request).execute();

        // This is for Session ID getter in Set-Cookie response.
        String cookieResponseHeader = response.headers().get("Set-Cookie");
        String sessionId = getSessionIdFromHeader(cookieResponseHeader);

        return new CustomResponse(
                response.code(),
                Objects.requireNonNull(response.body()).string(),
                sessionId
        );
    }

    private static String getSessionIdFromHeader(String header) {
        if (header != null) {
            String splitChar;
            if (header.contains("; ")) splitChar = "; ";
            else splitChar = ";";

            String[] cookieHeaderSplit = header.split(splitChar);
            for (String item : cookieHeaderSplit) {
                if (item.contains("ASP.NET_SessionId")) {
                    String[] sessionIdSplit = item.split("=");
                    return sessionIdSplit[1];
                }
            }
        }

        return null;
    }
}
