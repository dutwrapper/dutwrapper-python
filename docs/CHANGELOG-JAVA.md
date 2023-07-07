# DUTWRAPPER CHANGE LOG - JAVA

This file will list all version log for modified, add or remove function of dutapi.

## 1.7.5
- Changed package name to io.dutwrapperlib.dutwrapper. Get package in JitPack still is io.dutwrapper-lib.java.

## 1.7.4
- Fixed a issue which in web fault cause news subject failed to fetch data if different split condition is used (ex: 20Nh92 instead of 20.Nh92).

## 1.7.3
- Optimize code performance.
- **[NOTE]:** You can use 1.7.2-hotfix1 if your code ran properly.

## 1.7.2-hotfix1
- Instead of load file, directly save json to Variables.java.

## 1.7.2
- An issue is included a fix, but not testing: getDUTSchoolYear() in Utils.
- Added lecturer name and lecturer gender in NewsSubjectItem, however, this is still in alpha.

## 1.7.1 (Hotfix for 1.7.0)
- Fixed an issue in SubjectCodeItem cause string parameter in constructor isn't working.

## 1.7.0
- Updated implementations to latest.
- Update features in News Subject. More details please view code [here](src\main\java\io\zoemeow\dutapi\News.java).
- Add a function to get current DUT week.

## 1.6.3

- Extended timeout limit to 60 seconds.
- Fixed issues and optimize codes.

## 1.6.2

- JitPack.io support for this library.
- Fixed issues and optimize codes.

## 1.6.1

- Fix critical error.

## 1.6.0

- Move from VS Code to Intellij IDEA.
- Migrate with old commits.
- Rename from Session to Accounts and Major changes for Accounts.
- Used OkHttp3.

## 1.5.1

- Switched to Gradle.

## 1.5

- Chaged variables for Subject Schedue.
- Schedule Study and Schedule Exam will be independence.

## 1.4.2

[.NET]

- Optimize code line.

## 1.4.1

[.NET]

- Merge GetNewsGeneral() and GetNewsSubject() together.
    - To GetNews().

## 1.4

- Inital commit for Java.
- Move trello schedule link to [DEVPLANNING.md](DEVPLANNING.md).

## 1.3

- Inital commit for Python.
- Delete unneed files for .NET.
- Optimize code :)

## 1.2

- Added feature: Get all subjects fee list.
- Change file and function name: ~~GetScheduleSubject~~ to **GetSubjectsSchedule**.
- Add [CHANGELOG.md](CHANGELOG.md) for all old logs.
- Optimize code.

## 1.1

- Added feature: Get schedule about subjects and examimation.

## 1.0

Inital commit with features:

- Get news general (Nhận thông báo chung).
- Get news subjects (Nhận thông báo lớp học phần).
- Sesion (Phiên, dùng để đăng nhập/đăng xuất/lấy thông tin tài khoản).