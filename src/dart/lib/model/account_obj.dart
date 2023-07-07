import 'global_obj_var.dart';

class SubjectScheduleItem {
  SubjectCodeItem id = SubjectCodeItem();
  String name = '';
  int credit = 0;
  bool isHighQuality = false;
  String lecturerName = '';
  SubjectStudyList subjectStudy = SubjectStudyList();
  SubjectExamItem subjectExam = SubjectExamItem();
  String pointFormula = '';
}

class SubjectExamItem {
  int date = 0;
  String room = '';
  bool isGlobal = false;
  String group = '';
}

class SubjectStudyList {
  List<SubjectStudyItem> subjectStudyList = [];
  List<IntRange> weekList = [];
}

class SubjectStudyItem {
  // 0: Sunday, 1: Monday -> 6: Saturday
  int dayOfWeek = 0;
  IntRange lesson = IntRange();
  String room = '';
}
