import 'global_obj_var.dart';

class NewsLinkItem {
  String text;
  int position;
  String url;

  NewsLinkItem({
    required this.text,
    required this.position,
    required this.url,
  });
}

class NewsGlobal {
  String title = '';
  String content = '';
  String contentString = '';
  int date = 0;
  List<NewsLinkItem> links = [];
}

class NewsSubject extends NewsGlobal {
  List<SubjectGroupItem> affectedClasses = [];
  int affectedDate = 0;
  LessonStatus lessonStatus = LessonStatus.unknown;
  IntRange affectedLessons = IntRange();
  String affectedRoom = '';
  String lecturerName = '';
  LecturerGender lecturerGender = LecturerGender.other;
}
