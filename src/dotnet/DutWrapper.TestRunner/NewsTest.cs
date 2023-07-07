using DutWrapper.Model.News;

namespace DutWrapper.TestRunner
{
    [TestClass]
    public class NewsTest
    {
        [TestMethod]
        public void GetNews_Global()
        {
            int NEWS_COUNT = 5;

            List<NewsGlobalItem> news = new List<NewsGlobalItem>();
            for (int i = 1; i <= NEWS_COUNT; i++)
            {
                var data = News.GetNewsGlobal(i);
                if (data == null)
                    throw new NullReferenceException($"Internal error from function. Did you connected the internet?");
                if (data.Count == 0)
                    throw new NullReferenceException($"No datas in page {i}. Did you connected the internet?");

                news.AddRange(data);
            }

            Console.WriteLine($"Total news in {NEWS_COUNT} page(s): {news.Count}");
        }

        [TestMethod]
        public void GetNews_Subject()
        {
            int NEWS_COUNT = 5;

            List<NewsGlobalItem> news = new List<NewsGlobalItem>();
            for (int i = 1; i <= NEWS_COUNT; i++)
            {
                var data = News.GetNewsSubject(i);
                if (data == null)
                    throw new NullReferenceException($"Internal error from function. Did you connected the internet?");
                if (data.Count == 0)
                    throw new NullReferenceException($"No datas in page {i}. Did you connected the internet?");

                news.AddRange(data);
            }

            Console.WriteLine($"Total news in {NEWS_COUNT} page(s): {news.Count}");
        }
    }
}