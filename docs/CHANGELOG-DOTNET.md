# DUTWRAPPER CHANGE LOG - NET

This file will list all version log for modified, add or remove function of DutWrapper.

## 1.6.1
- Fixed crash library when system date format is not dd/MM/yyyy.

## 1.6
- Upgrade .NET used for this project is 6.0.
- Changed namespace (~~DUTAPI~~ to DutWrapper).
- GetNews() now separated to two functions for news global and news subject (this will develop news subject easier).
- Account now switched to session id (so, Session class has been dropped).

## 1.5
- Changed namespace (~~ZoeMeow.DUTAPI~~ to DUTAPI).

## 1.4.2
- Optimize code line.

## 1.4.1
- Merge GetNewsGeneral() and GetNewsSubject() together.
  - To GetNews().

## 1.4
- Inital commit for Java.

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
