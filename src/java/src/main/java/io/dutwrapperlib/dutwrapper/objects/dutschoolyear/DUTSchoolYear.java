package io.dutwrapperlib.dutwrapper.objects.dutschoolyear;

import java.io.Serializable;
import java.util.List;
import java.util.stream.Collectors;

public class DUTSchoolYear implements Serializable {
    public static final String TimeInMilliSeconds = "milliseconds";
    public static final String TimeInSeconds = "seconds";

    private int gmt;
    private String unix = TimeInMilliSeconds;
    private List<DUTSchoolYearItem> list;

    public DUTSchoolYear(int gmt, String unix, List<DUTSchoolYearItem> list) {
        this.gmt = gmt;
        this.unix = unix;
        this.list = list;
    }

    public static Integer getCurrentWeekBySchoolYear(
            DUTSchoolYearItem schoolYearItem,
            Long unixTimestamp
    ) {
        return Math.toIntExact(((unixTimestamp - schoolYearItem.getStart()) / 1000 / 60 / 60 / 24 / 7) + 1);
    }

    public int getGmt() {
        return gmt;
    }

    public void setGmt(int gmt) {
        this.gmt = gmt;
    }

    public String getUnix() {
        return unix;
    }

    public void setUnix(String unix) {
        this.unix = unix;
    }

    public List<DUTSchoolYearItem> getList() {
        return list;
    }

    public void setList(List<DUTSchoolYearItem> list) {
        this.list = list;
    }

    public DUTSchoolYearItem getCurrentSchoolYear(Long unixTimestamp) {
        List<DUTSchoolYearItem> list1 = list.stream()
                .filter(p -> p.getStart() < unixTimestamp)
                .sorted((left, right) -> Long.compare(right.getStart(), left.getStart()))
                .collect(Collectors.toList());

        if (list1.isEmpty())
            return null;
        else return list1.get(0);
    }
}
