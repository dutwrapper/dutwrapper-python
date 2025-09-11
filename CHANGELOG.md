# DUTWRAPPER CHANGE LOG

This file will list all version log for modified, added or removed functions of dutwrapper (Python language).

## 1.9.1
- IMPORTANT: We will deprecate this project on 2025/09/11. Learn more on [project homepage](https://github.com/dutwrapper).
- Added option to check if server is online or down.
- Optimized codes and updated dependencies to latest version.

## 1.9.0
- Changed all domains to `https` (since student page has been upgraded to `https`).
- Added `Student affairs`, `Examination`, `Tuition fee` and `Statute and Regulation` in `NewsType`.
- Fixed an issue (since page changed) cause exception in `fetch_subject_fee`.
- Improved unittest.

## 1.8.0
- Added `fetch_account_training_status()` function in `Accounts`.
- Adjust and resolved issues in all functions in `Accounts`.
- Removed `GetCurrentWeek()` function in `Utils`. This will be back soon.
- Sync all key in json with `dutwrapper-java` and `dutwrapper-dotnet`.
- Improved unittest.

## 1.7.1
- Fixed a issue prevent logging in to sv.dut.udn.vn.
- Improved unittest.

## 1.7.0
- Renamed package to dutwrapper.

## 1.6.1 and 1.6.1-hotfix1
- Added school year start for known dut school years.

## 1.6.0-hotfix1
- (No additional comments here)

## 1.6.0
- Fixed known issues and improvements performance.

## 1.5.1
- Added in Account Information: Student ID.
- Reformat in AccountColumnInfo.py

## 1.5.0
- Added Account Information when you logged in (remember: this will get data from page, not for edit them).

## 1.4.5
- Remove unnecessary key "gmt" (due to key "date" has already included).
- Add key "position" in GetNews(): Easier get link in key "contenttext".

## 1.4.4
- DateExamInString in subject schedule will be splitted to 2 items (managed by *`__string2ExamSchedule__()`*):
  - `DateExam`: isoformat
  - `RoomExam`: string
- Add Region GMT. This is useful when you host a server which its GMT is different from your computer/region.
  (managed by *`GetRegionGMT()`*)
- All date in json will be returned to isoformat instead of string, so you can use them directly with functions that can be initialized with isoformat string
  (note: **date in *`GetNews()['newslist']`* function won't be affected**).

## 1.4.3
- New function: Get current week (data from dut.udn.vn).
- Move 'GetNews' function to Utils.py (this will also remove file 'GetNews.py'.
- Functions in class 'Session.py' will be work independently (no more class 'Session').

## 1.4.2
[.NET]
- Optimize code line.

## 1.4.1
[.NET]
- Merge `GetNewsGeneral()` and `GetNewsSubject()` together.
  - To `GetNews()`.

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
