namespace DutWrapper.Model
{
    public enum Gender
    {
        Unknown = -1,
        Male,
        Female,
    }

    /// <summary>
    /// Account status while logging in.
    /// </summary>
    public enum LoginStatus
    {
        Unknown = -2,
        NoInternet = -1,
        /// <summary>
        /// This acconut has logged in.
        /// </summary>
        LoggedIn,
        /// <summary>
        /// Logged out or not logged in yet.
        /// </summary>
        LoggedOut,
        /// <summary>
        /// This account has been locked.
        /// </summary>
        AccountLocked,
    }

    public enum NewsType
    {
        /// <summary>
        /// Global news.
        /// </summary>
        Global,
        /// <summary>
        /// Subject news.
        /// </summary>
        Subject,
    }

    public enum SubjectStatus
    {
        /// <summary>
        /// Unknown status for this subject.
        /// </summary>
        Unknown = -1,
        /// <summary>
        /// This subject is only send notify to students and won't be changed.
        /// </summary>
        Notify,
        /// <summary>
        /// This subject can't be performed as scheduled and will be make-up lesson later.
        /// </summary>
        Leaving,
        /// <summary>
        /// This subject scheduled a lesson for previous leaving lesson.
        /// </summary>
        MakeUpLesson
    }
}
