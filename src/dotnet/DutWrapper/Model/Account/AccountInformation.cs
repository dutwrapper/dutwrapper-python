using System;

namespace DutWrapper.Model.Account
{
    public class AccountInformation
    {
        /// <summary>
        /// Student name
        /// </summary>
        public string? Name { get; set; } = null;

        /// <summary>
        /// Student account ID
        /// </summary>
        public string? ID { get; set; } = null;

        /// <summary>
        /// Student date of birth
        /// </summary>
        public DateTime DateOfBirth { get; set; }

        /// <summary>
        /// Student gender
        /// </summary>
        public Gender Gender { get; set; } = Gender.Unknown;

        /// <summary>
        /// Student identity ID
        /// </summary>
        public string? IdentityID { get; set; } = null;

        /// <summary>
        /// Student bank information
        /// </summary>
        public string? BankInfo { get; set; } = null;

        /// <summary>
        /// Student health insurance ID
        /// </summary>
        public string? HIID { get; set; } = null;

        /// <summary>
        /// Student email
        /// </summary>
        public string? PersonalEmail { get; set; } = null;

        /// <summary>
        /// Student phone number
        /// </summary>
        public string? PhoneNumber { get; set; }

        /// <summary>
        /// Student account email for education
        /// </summary>
        public string? EducationEmail { get; set; } = null;

        /// <summary>
        /// Student class name (ex. 20R12)
        /// </summary>
        public string? ClassName { get; set; } = null;
    }
}
