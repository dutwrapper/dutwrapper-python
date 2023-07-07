using System;
using System.Collections.Generic;
using System.Text;

namespace DutWrapper.Model.Account
{
    public class SubjectFee
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
        #endregion

        #region Fee information
        public double Price { get; set; } = 0.0;

        public bool Debt { get; set; } = false;

        public bool IsReStudy { get; set; } = false;

        public string? VerifiedPaymentAt { get; set; } = null;
        #endregion
    }
}
