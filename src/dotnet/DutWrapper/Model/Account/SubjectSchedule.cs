using System;
using System.Collections.Generic;
using System.Text;

namespace DutWrapper.Model.Account
{
    public class SubjectSchedule
    {
        #region Basic Information
        /// <summary>
        /// Subject ID.
        /// </summary>
        public string? ID { get; set; } = null;
        /// <summary>
        /// Subject name.
        /// </summary>
        public string? Name { get; set; } = null;

        /// <summary>
        /// Subject credit
        /// </summary>
        public float Credit { get; set; } = 0;
        #endregion

        #region Subject Information
        public bool IsHighQuality { get; set; } = false;

        public string? Lecturer { get; set; } = null;

        public string? ScheduleStudy { get; set; } = null;

        public string? Weeks { get; set; } = null;

        public string? PointFomula { get; set; } = null;
        #endregion

        #region Subject Examination Information
        public string? GroupExam { get; set; } = null;

        public bool IsGlobalExam { get; set; } = false;

        public string? RoomExam { get; set; } = null;

        public string? DateExamInString { get; set; } = null;

        public long DateExamInUnix { get; set; } = 0;

        #endregion

        public bool Equals(SubjectSchedule sub)
        {
            if (base.Equals(sub))
                return true;

            // Basic information
            if (sub.ID != ID ||
                sub.Name != Name
                )
                return false;

            // Subject information
            if (sub.Credit != Credit ||
                sub.IsHighQuality != IsHighQuality ||
                sub.Lecturer != Lecturer ||
                sub.ScheduleStudy != ScheduleStudy ||
                sub.Weeks != Weeks ||
                sub.PointFomula != PointFomula
                )
                return false;

            // Subject Examination Information
            if (sub.GroupExam != GroupExam ||
                sub.IsGlobalExam != IsGlobalExam ||
                sub.RoomExam != RoomExam ||
                sub.DateExamInUnix != DateExamInUnix ||
                sub.DateExamInString != DateExamInString
                )
                return false;

            return true;
        }
    }
}
