using DutWrapper.UWP.Model;
using DutWrapper.UWP.Model.News;
using HtmlAgilityPack;
using System;
using System.Collections.Generic;
using System.Globalization;
using System.Net;
using System.Net.Http;

namespace DutWrapper.UWP
{
    public static partial class News
    {
        private static List<NewsGlobalItem> GetNews(NewsType newsType, int page = 1, string query = null)
        {
            if (page < 1)
                throw new ArgumentException($"Page must be greater than 0! (current is {page})");

            List<NewsGlobalItem> result = new List<NewsGlobalItem>();

            try
            {
                HttpClient client = new HttpClient();
                client.BaseAddress = new Uri("http://sv.dut.udn.vn");

                HttpResponseMessage response = client.GetAsync($"/WebAjax/evLopHP_Load.aspx?E={(newsType == NewsType.Global ? "CTRTBSV" : "CTRTBGV")}&PAGETB={(page > 0 ? page : 1)}&COL=TieuDe&NAME={query}&TAB=1").Result;
                if (!response.IsSuccessStatusCode)
                    throw new Exception(String.Format("The request has return code {0}.", response.StatusCode));

                HtmlDocument htmlDoc = new HtmlDocument();
                htmlDoc.LoadHtml(response.Content.ReadAsStringAsync().Result);

                HtmlNodeCollection htmlDocNews = htmlDoc.DocumentNode.SelectNodes("//div[@class='tbBox']");

                // TODO: Add exception here.
                if (htmlDocNews == null || htmlDocNews.Count == 0)
                    throw new Exception($"No datas from sv.dut.udn.vn in page {page}.");

                foreach (HtmlNode htmlItem in htmlDocNews)
                {
                    NewsGlobalItem item = new NewsGlobalItem();

                    var htmlTemp = new HtmlDocument();
                    htmlTemp.LoadHtml(htmlItem.InnerHtml);

                    string title = htmlTemp.DocumentNode.SelectNodes("//div[@class='tbBoxCaption']")[0].InnerText;
                    string[] titleTemp = title.Split(new string[] { ":&nbsp;&nbsp;&nbsp;&nbsp; " }, StringSplitOptions.None);

                    if (titleTemp.Length == 2)
                    {
                        item.Date = DateTime.ParseExact(titleTemp[0].Replace(" ", ""), "dd/MM/yyyy", CultureInfo.InvariantCulture);
                        item.Title = WebUtility.HtmlDecode(titleTemp[1]);
                        item.Content = htmlTemp.DocumentNode.SelectNodes("//div[@class='tbBoxContent']")[0].InnerHtml;
                        item.ContentString = htmlTemp.DocumentNode.SelectNodes("//div[@class='tbBoxContent']")[0].InnerText;
                    }
                    else
                    {
                        item.Title = WebUtility.HtmlDecode(title);
                        item.Content = htmlTemp.DocumentNode.SelectNodes("//div[@class='tbBoxContent']")[0].InnerHtml;
                        item.ContentString = htmlTemp.DocumentNode.SelectNodes("//div[@class='tbBoxContent']")[0].InnerText;
                    }

                    result.Add(item);
                }
            }
            catch
            {
                result.Clear();
                result = null;
            }

            return result;
        }

        public static List<NewsGlobalItem> GetNewsGlobal(int page = 1, string query = null)
        {
            return GetNews(NewsType.Global, page, query);
        }

        public static List<NewsGlobalItem> GetNewsSubject(int page = 1, string query = null)
        {
            return GetNews(NewsType.Subject, page, query);
        }
    }
}
