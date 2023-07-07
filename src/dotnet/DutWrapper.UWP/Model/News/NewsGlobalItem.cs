using System;

namespace DutWrapper.UWP.Model.News
{
    public class NewsGlobalItem
    {
        /// <summary>
        /// News title.
        /// </summary>
        public string Title { get; set; } = null;

        /// <summary>
        /// News content in HTML.
        /// </summary>
        public string Content { get; set; } = null;

        /// <summary>
        /// News content in plain text.
        /// </summary>
        public string ContentString { get; set; } = null;

        /// <summary>
        /// News date when it posted.
        /// </summary>
        public DateTime? Date { get; set; }

        public bool Equals(NewsGlobalItem news)
        {
            if (base.Equals(news))
                return true;

            if (news.Title != Title ||
                news.Content != Content ||
                news.ContentString != ContentString ||
                news.Date != Date
                )
                return false;

            return true;
        }
    }
}
