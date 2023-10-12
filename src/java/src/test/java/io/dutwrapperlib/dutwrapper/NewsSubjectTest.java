package io.dutwrapperlib.dutwrapper;

import org.junit.jupiter.api.Test;

import io.dutwrapperlib.dutwrapper.objects.enums.LessonStatus;
import io.dutwrapperlib.dutwrapper.objects.news.NewsSubjectItem;

import java.util.List;

public class NewsSubjectTest {
    @Test
    void getNews() throws Exception {
        int page = 1;
        int pageMax = 10;

        while (page <= pageMax) {
            System.out.println("==================================");
            System.out.println("Page " + page);

            List<NewsSubjectItem> newsList = News.getNewsSubject(page);
            System.out.println("Item count: " + newsList.size());

            for (NewsSubjectItem newsItem : newsList) {
                System.out.println("============================");
                System.out.println(newsItem.getTitle());
                System.out.println(newsItem.getDate());
                System.out.printf("%s|%s%n", newsItem.getLecturerName(), newsItem.getLecturerGender() ? "true" : "false");
                if (newsItem.getLessonStatus() == LessonStatus.Leaving) {
                    System.out.println("Leaving");
                    System.out.println("Date: " + newsItem.getAffectedDate());
                    System.out.println("Lesson: " + newsItem.getAffectedLesson().toString());
                }
                else if (newsItem.getLessonStatus() == LessonStatus.MakeUp) {
                    System.out.println("MakeUp");
                    System.out.println("Date: " + newsItem.getAffectedDate());
                    System.out.println("Lesson: " + newsItem.getAffectedLesson().toString());
                    System.out.println("Room: " + newsItem.getAffectedRoom());
                }
                else {
                    System.out.println(newsItem.getContentString());
                }
            }
            page += 1;
        }
    }
}
