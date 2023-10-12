package io.dutwrapperlib.dutwrapper;

import org.junit.jupiter.api.Test;

import io.dutwrapperlib.dutwrapper.objects.dutschoolyear.DUTSchoolYear;
import io.dutwrapperlib.dutwrapper.objects.dutschoolyear.DUTSchoolYearItem;

public class UtilsTest {
    @Test
    void finalTest() throws Exception {
        Long currentUnix = Utils.getCurrentTimeInUnix();
        System.out.println(currentUnix);

        DUTSchoolYearItem item = Utils.getDUTSchoolYear(currentUnix);
        System.out.println(item.getName());
        System.out.println(item.getYear());
        System.out.println(item.getStart());

        Integer currentWeek = DUTSchoolYear.getCurrentWeekBySchoolYear(
                item,
                currentUnix
        );
        System.out.println(currentWeek);
    }
}
