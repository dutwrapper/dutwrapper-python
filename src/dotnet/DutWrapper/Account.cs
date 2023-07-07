using DutWrapper.Model;
using DutWrapper.Model.Account;
using HtmlAgilityPack;
using System;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using System.Net.Http;

namespace DutWrapper
{
    public static class Account
    {
        private static string BASE_ADDRESS = "http://sv.dut.udn.vn";
        private static string __VIEWSTATE = "/wEPDwUKMTY2NjQ1OTEyNA8WAh4TVmFsaWRhdGVSZXF1ZXN0TW9kZQIBFgJmD2QWAgIFDxYCHglpbm5lcmh0bWwF4i08dWwgaWQ9J21lbnUnIHN0eWxlPSd3aWR0aDogMTI4MHB4OyBtYXJnaW46IDAgYXV0bzsgJz48bGk+PGEgSUQ9ICdsUGFIT01FJyBzdHlsZSA9J3dpZHRoOjY1cHgnIGhyZWY9J0RlZmF1bHQuYXNweCc+VHJhbmcgY2jhu6c8L2E+PGxpPjxhIElEPSAnbFBhQ1REVCcgc3R5bGUgPSd3aWR0aDo4NXB4JyBocmVmPScnPkNoxrDGoW5nIHRyw6xuaDwvYT48dWwgY2xhc3M9J3N1Ym1lbnUnPjxsaT48YSBJRCA9J2xDb0NURFRDMicgICBzdHlsZSA9J3dpZHRoOjE0MHB4JyBocmVmPSdHX0xpc3RDVERULmFzcHgnPkNoxrDGoW5nIHRyw6xuaCDEkcOgbyB04bqhbzwvYT48L2xpPjxsaT48YSBJRCA9J2xDb0NURFRDMScgICBzdHlsZSA9J3dpZHRoOjE0MHB4JyBocmVmPSdHX0xpc3RIb2NQaGFuLmFzcHgnPkjhu41jIHBo4bqnbjwvYT48L2xpPjxsaT48YSBJRCA9J2xDb0NURFRDMycgICBzdHlsZSA9J3dpZHRoOjIwMHB4JyBocmVmPSdHX0xpc3RDVERUQW5oLmFzcHgnPlByb2dyYW08L2E+PC9saT48L3VsPjwvbGk+PGxpPjxhIElEPSAnbFBhS0hEVCcgc3R5bGUgPSd3aWR0aDo2MHB4JyBocmVmPScnPkvhur8gaG/huqFjaDwvYT48dWwgY2xhc3M9J3N1Ym1lbnUnPjxsaT48YSBJRCA9J2xDb0tIRFRDMScgICBzdHlsZSA9J3dpZHRoOjIwMHB4JyBocmVmPSdodHRwczovLzFkcnYubXMvYi9zIUF0d0tsRFo2VnFidG5RY2JqUVFwS05rbUswX2g/ZT1uQ2I3eVAnPkvhur8gaG/huqFjaCDEkcOgbyB04bqhbyBuxINtIGjhu41jPC9hPjwvbGk+PGxpPjxhIElEID0nbENvS0hEVEMyJyAgIHN0eWxlID0nd2lkdGg6MjAwcHgnIGhyZWY9J2h0dHA6Ly9kazQuZHV0LnVkbi52bic+xJDEg25nIGvDvSBo4buNYzwvYT48L2xpPjxsaT48YSBJRCA9J2xDb0tIRFRDMycgICBzdHlsZSA9J3dpZHRoOjIwMHB4JyBocmVmPSdodHRwOi8vZGs0LmR1dC51ZG4udm4vR19Mb3BIb2NQaGFuLmFzcHgnPkzhu5twIGjhu41jIHBo4bqnbiAtIMSRYW5nIMSRxINuZyBrw708L2E+PC9saT48bGk+PGEgSUQgPSdsQ29LSERUQzQnICAgc3R5bGUgPSd3aWR0aDoyMDBweCcgaHJlZj0nR19Mb3BIb2NQaGFuLmFzcHgnPkzhu5twIGjhu41jIHBo4bqnbiAtIGNow61uaCB0aOG7qWM8L2E+PC9saT48bGk+PGEgSUQgPSdsQ29LSERUQzUnICAgc3R5bGUgPSd3aWR0aDoyMDBweCcgaHJlZj0naHR0cDovL2RrNC5kdXQudWRuLnZuL0dfREt5Tmh1Q2F1LmFzcHgnPkto4bqjbyBzw6F0IG5odSBj4bqndSBt4bufIHRow6ptIGzhu5twPC9hPjwvbGk+PGxpPjxhIElEID0nbENvS0hEVEM2JyAgIHN0eWxlID0nd2lkdGg6MjAwcHgnIGhyZWY9J2h0dHA6Ly9jYi5kdXQudWRuLnZuL1BhZ2VMaWNoVGhpS0guYXNweCc+VGhpIGN14buRaSBr4buzIGzhu5twIGjhu41jIHBo4bqnbjwvYT48L2xpPjxsaT48YSBJRCA9J2xDb0tIRFRDNycgICBzdHlsZSA9J3dpZHRoOjIwMHB4JyBocmVmPSdHX0RLVGhpTk4uYXNweCc+VGhpIFRp4bq/bmcgQW5oIMSR4buLbmgga+G7sywgxJHhuqd1IHJhPC9hPjwvbGk+PGxpPjxhIElEID0nbENvS0hEVEM4JyAgIHN0eWxlID0nd2lkdGg6MjAwcHgnIGhyZWY9J0dfTGlzdExpY2hTSC5hc3B4Jz5TaW5oIGhv4bqhdCBs4bubcCDEkeG7i25oIGvhu7M8L2E+PC9saT48bGk+PGEgSUQgPSdsQ29LSERUQzknICAgc3R5bGUgPSd3aWR0aDoyMDBweCcgaHJlZj0naHR0cDovL2ZiLmR1dC51ZG4udm4nPkto4bqjbyBzw6F0IMO9IGtp4bq/biBzaW5oIHZpw6puPC9hPjwvbGk+PGxpPjxhIElEID0nbENvS0hEVEM5JyAgIHN0eWxlID0nd2lkdGg6MjAwcHgnIGhyZWY9J0dfREtQVkNELmFzcHgnPkhv4bqhdCDEkeG7mW5nIHBo4bulYyB24bulIGPhu5luZyDEkeG7k25nPC9hPjwvbGk+PC91bD48L2xpPjxsaT48YSBJRD0gJ2xQYVRSQUNVVScgc3R5bGUgPSd3aWR0aDo3MHB4JyBocmVmPScnPkRhbmggc8OhY2g8L2E+PHVsIGNsYXNzPSdzdWJtZW51Jz48bGk+PGEgSUQgPSdsQ29UUkFDVVUwMScgICBzdHlsZSA9J3dpZHRoOjI0MHB4JyBocmVmPSdHX0xpc3ROZ3VuZ0hvYy5hc3B4Jz5TaW5oIHZpw6puIG5n4burbmcgaOG7jWM8L2E+PC9saT48bGk+PGEgSUQgPSdsQ29UUkFDVVUwMycgICBzdHlsZSA9J3dpZHRoOjI0MHB4JyBocmVmPSdHX0xpc3RMb3AuYXNweCc+U2luaCB2acOqbiDEkWFuZyBo4buNYyAtIGzhu5twPC9hPjwvbGk+PGxpPjxhIElEID0nbENvVFJBQ1VVMDQnICAgc3R5bGUgPSd3aWR0aDoyNDBweCcgaHJlZj0nR19MaXN0Q0NDTlRULmFzcHgnPlNpbmggdmnDqm4gY8OzIGNo4bupbmcgY2jhu4kgQ05UVDwvYT48L2xpPjxsaT48YSBJRCA9J2xDb1RSQUNVVTA1JyAgIHN0eWxlID0nd2lkdGg6MjQwcHgnIGhyZWY9J0dfTGlzdENDTk4uYXNweCc+U2luaCB2acOqbiBjw7MgY2jhu6luZyBjaOG7iSBuZ2/huqFpIG5n4buvPC9hPjwvbGk+PGxpPjxhIElEID0nbENvVFJBQ1VVMDYnICAgc3R5bGUgPSd3aWR0aDoyNDBweCcgaHJlZj0naHR0cDovL2Rhb3Rhby5kdXQudWRuLnZuL1NWL0dfS1F1YUFuaFZhbi5hc3B4Jz5TaW5oIHZpw6puIHRoaSBUaeG6v25nIEFuaCDEkeG7i25oIGvhu7M8L2E+PC9saT48bGk+PGEgSUQgPSdsQ29UUkFDVVUwNycgICBzdHlsZSA9J3dpZHRoOjI0MHB4JyBocmVmPSdHX0xpc3REb0FuVE4uYXNweCc+U2luaCB2acOqbiBsw6BtIMSQ4buTIMOhbiB04buRdCBuZ2hp4buHcDwvYT48L2xpPjxsaT48YSBJRCA9J2xDb1RSQUNVVTA4JyAgIHN0eWxlID0nd2lkdGg6MjQwcHgnIGhyZWY9J0dfTGlzdEhvYW5Ib2NQaGkuYXNweCc+U2luaCB2acOqbiDEkcaw4bujYyBob8OjbiDEkcOzbmcgaOG7jWMgcGjDrTwvYT48L2xpPjxsaT48YSBJRCA9J2xDb1RSQUNVVTE2JyAgIHN0eWxlID0nd2lkdGg6MjQwcHgnIGhyZWY9J0dfTGlzdEhvYW5fVGhpQlMuYXNweCc+U2luaCB2acOqbiDEkcaw4bujYyBob8OjbiB0aGksIHRoaSBi4buVIHN1bmc8L2E+PC9saT48bGk+PGEgSUQgPSdsQ29UUkFDVVUwOScgICBzdHlsZSA9J3dpZHRoOjI0MHB4JyBocmVmPSdHX0xpc3RIb2NMYWkuYXNweCc+U2luaCB2acOqbiBk4buxIHR1eeG7g24gdsOgbyBo4buNYyBs4bqhaTwvYT48L2xpPjxsaT48YSBJRCA9J2xDb1RSQUNVVTEwJyAgIHN0eWxlID0nd2lkdGg6MjQwcHgnIGhyZWY9J0dfTGlzdEt5THVhdC5hc3B4Jz5TaW5oIHZpw6puIGLhu4sga+G7tyBsdeG6rXQ8L2E+PC9saT48bGk+PGEgSUQgPSdsQ29UUkFDVVUxMScgICBzdHlsZSA9J3dpZHRoOjI0MHB4JyBocmVmPSdHX0xpc3RCaUh1eUhQLmFzcHgnPlNpbmggdmnDqm4gYuG7iyBo4buneSBo4buNYyBwaOG6p248L2E+PC9saT48bGk+PGEgSUQgPSdsQ29UUkFDVVUxMicgICBzdHlsZSA9J3dpZHRoOjI0MHB4JyBocmVmPSdHX0xpc3RMb2NrV2ViLmFzcHgnPlNpbmggdmnDqm4gYuG7iyBraMOzYSB3ZWJzaXRlPC9hPjwvbGk+PGxpPjxhIElEID0nbENvVFJBQ1VVMTMnICAgc3R5bGUgPSd3aWR0aDoyNDBweCcgaHJlZj0nR19MaXN0TG9ja1dlYlRhbS5hc3B4Jz5TaW5oIHZpw6puIGLhu4sgdOG6oW0ga2jDs2Egd2Vic2l0ZTwvYT48L2xpPjxsaT48YSBJRCA9J2xDb1RSQUNVVTE0JyAgIHN0eWxlID0nd2lkdGg6MjQwcHgnIGhyZWY9J0dfTGlzdEhhbkNoZVRDLmFzcHgnPlNpbmggdmnDqm4gYuG7iyBo4bqhbiBjaOG6vyB0w61uIGNo4buJIMSRxINuZyBrw708L2E+PC9saT48bGk+PGEgSUQgPSdsQ29UUkFDVVUxNScgICBzdHlsZSA9J3dpZHRoOjI0MHB4JyBocmVmPSdHX0xpc3RDYW5oQmFvS1FIVC5hc3B4Jz5TaW5oIHZpw6puIGLhu4sgY+G6o25oIGLDoW8ga+G6v3QgcXXhuqMgaOG7jWMgdOG6rXA8L2E+PC9saT48L3VsPjwvbGk+PGxpPjxhIElEPSAnbFBhQ1VVU1YnIHN0eWxlID0nd2lkdGg6ODhweCcgaHJlZj0nJz5D4buxdSBzaW5oIHZpw6puPC9hPjx1bCBjbGFzcz0nc3VibWVudSc+PGxpPjxhIElEID0nbENvQ1VVU1YxJyAgIHN0eWxlID0nd2lkdGg6MTEwcHgnIGhyZWY9J0dfTGlzdFROZ2hpZXAuYXNweCc+xJDDoyB04buRdCBuZ2hp4buHcDwvYT48L2xpPjxsaT48YSBJRCA9J2xDb0NVVVNWMicgICBzdHlsZSA9J3dpZHRoOjExMHB4JyBocmVmPSdHX0xpc3RLaG9uZ1ROLmFzcHgnPktow7RuZyB04buRdCBuZ2hp4buHcDwvYT48L2xpPjwvdWw+PC9saT48bGk+PGEgSUQ9ICdsUGFDU1ZDJyBzdHlsZSA9J3dpZHRoOjE0NXB4JyBocmVmPScnPlBow7JuZyBo4buNYyAmIEjhu4cgdGjhu5FuZzwvYT48dWwgY2xhc3M9J3N1Ym1lbnUnPjxsaT48YSBJRCA9J2xDb0NTVkMwMScgICBzdHlsZSA9J3dpZHRoOjI0MHB4JyBocmVmPSdodHRwOi8vY2IuZHV0LnVkbi52bi9QYWdlQ05QaG9uZ0hvYy5hc3B4Jz5Uw6xuaCBow6xuaCBz4butIGThu6VuZyBwaMOybmcgaOG7jWM8L2E+PC9saT48bGk+PGEgSUQgPSdsQ29DU1ZDMDInICAgc3R5bGUgPSd3aWR0aDoyNDBweCcgaHJlZj0nR19MaXN0VGhCaUhvbmcuYXNweCc+VGjhu5FuZyBrw6ogYsOhbyB0aGnhur90IGLhu4sgcGjDsm5nIGjhu41jIGjhu49uZzwvYT48L2xpPjxsaT48YSBJRCA9J2xDb0NTVkMwOScgICBzdHlsZSA9J3dpZHRoOjI0MHB4JyBocmVmPSdHX1N5c1N0YXR1cy5hc3B4Jz5UcuG6oW5nIHRow6FpIGjhu4cgdGjhu5FuZyB0aMO0bmcgdGluIHNpbmggdmnDqm48L2E+PC9saT48L3VsPjwvbGk+PGxpPjxhIElEPSAnbFBhTElFTktFVCcgc3R5bGUgPSd3aWR0aDo1MHB4JyBocmVmPScnPkxpw6puIGvhur90PC9hPjx1bCBjbGFzcz0nc3VibWVudSc+PGxpPjxhIElEID0nbENvTElFTktFVDEnICAgc3R5bGUgPSd3aWR0aDo3MHB4JyBocmVmPSdodHRwOi8vbGliLmR1dC51ZG4udm4nPlRoxrAgdmnhu4duPC9hPjwvbGk+PGxpPjxhIElEID0nbENvTElFTktFVDInICAgc3R5bGUgPSd3aWR0aDo3MHB4JyBocmVmPSdodHRwOi8vbG1zMS5kdXQudWRuLnZuJz5EVVQtTE1TPC9hPjwvbGk+PC91bD48L2xpPjxsaT48YSBJRD0gJ2xQYUhFTFAnIHN0eWxlID0nd2lkdGg6NDVweCcgaHJlZj0nJz5I4buXIHRy4bujPC9hPjx1bCBjbGFzcz0nc3VibWVudSc+PGxpPjxhIElEID0nbENvSEVMUDEnICAgc3R5bGUgPSd3aWR0aDoyMTBweCcgaHJlZj0naHR0cDovL2ZyLmR1dC51ZG4udm4nPkPhu5VuZyBo4buXIHRy4bujIHRow7RuZyB0aW4gdHLhu7FjIHR1eeG6v248L2E+PC9saT48bGk+PGEgSUQgPSdsQ29IRUxQMicgICBzdHlsZSA9J3dpZHRoOjIxMHB4JyBocmVmPSdodHRwczovL2RyaXZlLmdvb2dsZS5jb20vZmlsZS9kLzFaMHFsYmhLYVNHbXpFWkpEMnVCNGVVV2VlSGFROUhIbC92aWV3Jz5IxrDhu5tuZyBk4bqrbiDEkMSDbmcga8O9IGjhu41jPC9hPjwvbGk+PGxpPjxhIElEID0nbENvSEVMUDMnICAgc3R5bGUgPSd3aWR0aDoyMTBweCcgaHJlZj0naHR0cDovL2Rhb3Rhby5kdXQudWRuLnZuL2Rvd25sb2FkMi9FbWFpbF9HdWlkZS5wZGYnPkjGsOG7m25nIGThuqtuIFPhu60gZOG7pW5nIEVtYWlsIERVVDwvYT48L2xpPjxsaT48YSBJRCA9J2xDb0hFTFA3JyAgIHN0eWxlID0nd2lkdGg6MjEwcHgnIGhyZWY9J2h0dHBzOi8vMWRydi5tcy91L3MhQXR3S2xEWjZWcWJ0bzEwYmhIYzBLN3NleU5Hcj9lYUNUYjh4Jz5WxINuIGLhuqNuIFF1eSDEkeG7i25oIGPhu6dhIFRyxrDhu51uZzwvYT48L2xpPjxsaT48YSBJRCA9J2xDb0hFTFA4JyAgIHN0eWxlID0nd2lkdGg6MjEwcHgnIGhyZWY9J2h0dHBzOi8vdGlueXVybC5jb20veTRrZGozc3AnPkJp4buDdSBt4bqrdSB0aMaw4budbmcgZMO5bmc8L2E+PC9saT48L3VsPjwvbGk+PGxpPjxhIGlkID0nbGlua0RhbmdOaGFwJyBocmVmPSdQYWdlRGFuZ05oYXAuYXNweCcgc3R5bGUgPSd3aWR0aDo4MHB4Oyc+IMSQxINuZyBuaOG6rXAgPC9hPjwvbGk+PGxpPjxkaXYgY2xhc3M9J0xvZ2luRnJhbWUnPjxkaXYgc3R5bGUgPSdtaW4td2lkdGg6IDEwMHB4Oyc+PC9kaXY+PC9kaXY+PC9saT48L3VsPmRkFSwwNgHSdZ2bG7X5MK3ePxjwI3ZrE7W2esgf8K/1Yqk=";

        private static FormUrlEncodedContent CreateLoginParameters(string username, string password)
        {
            Dictionary<string, string> dict = new Dictionary<string, string>
            {
                { "__VIEWSTATE", __VIEWSTATE },
                { "__VIEWSTATEGENERATOR", "20CC0D2F" },
                { "_ctl0:MainContent:DN_txtAcc", username },
                { "_ctl0:MainContent:DN_txtPass", password },
                { "_ctl0:MainContent:QLTH_btnLogin", "Đăng+nhập" }
            };
            return new FormUrlEncodedContent(dict);
        }

        public static string? GenerateNewSessionId()
        {
            HttpClient client = new HttpClient();
            client.BaseAddress = new Uri(BASE_ADDRESS);
            HttpResponseMessage response = client.GetAsync($"/PageDangNhap.aspx").Result;

            string[] cookieHeaderList = new string[2] { "Set-Cookie", "Cookie" };
            foreach (string cookieHeader in cookieHeaderList)
            {
                if (response.Headers.TryGetValues(cookieHeader, out var cookieValue))
                {
                    foreach (var d in cookieValue)
                    {
                        string[] d1 = d.Split(";");
                        foreach (string d2 in d1)
                        {
                            string[] d3 = d2.Split("=");
                            if (d3.Length != 2)
                                continue;
                            if (d3[0] == "ASP.NET_SessionId")
                                return d3[1];
                        }
                    }
                    break;
                }
            }

            return null;
        }

        public static LoginStatus Login(string sessionId, string username, string password)
        {
            HttpClient client = new HttpClient();
            client.BaseAddress = new Uri(BASE_ADDRESS);
            client.DefaultRequestHeaders.Add("Cookie", $"ASP.NET_SessionId={sessionId};");
            client.PostAsync($"/PageDangNhap.aspx", CreateLoginParameters(username, password)).Wait();
            return IsLoggedIn(sessionId);
        }

        public static LoginStatus IsLoggedIn(string sessionId)
        {
            HttpClient client = new HttpClient();
            client.BaseAddress = new Uri(BASE_ADDRESS);
            client.DefaultRequestHeaders.Add("Cookie", $"ASP.NET_SessionId={ sessionId };");
            HttpResponseMessage response = client.GetAsync($"/WebAjax/evLopHP_Load.aspx?E=TTKBLoad&Code=2120").Result;
            if (response.IsSuccessStatusCode)
                return LoginStatus.LoggedIn;
            else return LoginStatus.LoggedOut;

        }

        public static void Logout(string sessionId)
        {
            HttpClient client = new HttpClient();
            client.BaseAddress = new Uri(BASE_ADDRESS);
            client.DefaultRequestHeaders.Add("Cookie", $"ASP.NET_SessionId={sessionId};");
            client.GetAsync($"/PageLogout.aspx").Wait();
        }

        public static List<SubjectSchedule>? GetSubjectScheduleList(string sessionId, int year = 20, int semester = 1)
        {
            if (semester < 1 || semester > 3)
                throw new ArgumentException();

            List<SubjectSchedule>? result = new List<SubjectSchedule>();

            try
            {
                HttpClient client = new HttpClient();
                client.BaseAddress = new Uri(BASE_ADDRESS);
                client.DefaultRequestHeaders.Add("Cookie", $"ASP.NET_SessionId={sessionId};");
                HttpResponseMessage response = client.GetAsync($"/WebAjax/evLopHP_Load.aspx?E=TTKBLoad&Code={year}{(semester <= 2 ? semester : 2)}{(semester == 3 ? 1 : 0)}").Result;

                if (!response.IsSuccessStatusCode)
                    throw new Exception(String.Format("The request has return code {0}.", response.StatusCode));

                HtmlDocument htmlDoc = new HtmlDocument();
                htmlDoc.LoadHtml(response.Content.ReadAsStringAsync().Result);

                // TODO: Schedule Study
                HtmlDocument htmlDocSchStudy = new HtmlDocument();
                htmlDocSchStudy.LoadHtml(htmlDoc.GetElementbyId("TTKB_GridInfo").InnerHtml);
                var rowListStudy = htmlDocSchStudy.DocumentNode.SelectNodes("//tr[@class='GridRow']");

                if (rowListStudy != null && rowListStudy.Count > 0)
                {
                    foreach (HtmlNode row in rowListStudy)
                    {
                        HtmlDocument httpTempStudyItem = new HtmlDocument();
                        httpTempStudyItem.LoadHtml(row.InnerHtml);
                        var cellCollection = httpTempStudyItem.DocumentNode.SelectNodes("//td[contains(@class, 'GridCell')]");

                        SubjectSchedule item = new SubjectSchedule();
                        item.ID = cellCollection[1].InnerText;
                        item.Name = cellCollection[2].InnerText;
                        item.Credit = ConvertTo<float>(cellCollection[3].InnerText);
                        item.IsHighQuality = cellCollection[5].Attributes["class"].Value.Contains("GridCheck");
                        item.Lecturer = cellCollection[6].InnerText;
                        item.ScheduleStudy = cellCollection[7].InnerText;
                        item.Weeks = cellCollection[8].InnerText;
                        item.PointFomula = cellCollection[10].InnerText;

                        result.Add(item);
                    }
                }

                // TODO: Schedule Examination
                HtmlDocument htmlDocSchExam = new HtmlDocument();
                htmlDocSchExam.LoadHtml(htmlDoc.GetElementbyId("TTKB_GridLT").InnerHtml);
                var rowListExam = htmlDocSchExam.DocumentNode.SelectNodes("//tr[@class='GridRow']");
                if (rowListExam != null && rowListExam.Count > 0)
                    foreach (HtmlNode row in rowListExam)
                    {
                        HtmlDocument httpTempExamItem = new HtmlDocument();
                        httpTempExamItem.LoadHtml(row.InnerHtml);
                        var cellCollection = httpTempExamItem.DocumentNode.SelectNodes("//td[contains(@class, 'GridCell')]");

                        var item = result.Where(p => p.ID == cellCollection[1].InnerText).First();
                        if (item == null)
                            continue;

                        item.GroupExam = cellCollection[3].InnerText;
                        item.IsGlobalExam = cellCollection[4].Attributes["class"].Value.Contains("GridCheck");
                        item.DateExamInString = cellCollection[5].InnerText;

                        if (item.DateExamInString == null)
                            continue;

                        DateTime? dateTime = null;
                        string[] splited = item.DateExamInString.Split(new string[] { ", " }, StringSplitOptions.None);
                        string? time = null;
                        for (int i = 0; i < splited.Length; i++)
                        {
                            switch (splited[i].Split(new string[] { ": " }, StringSplitOptions.None)[0])
                            {
                                case "Phòng":
                                    item.RoomExam = splited[i].Split(new string[] { ": " }, StringSplitOptions.None)[1];
                                    break;
                                case "Ngày":
                                    dateTime = DateTime.ParseExact(splited[i].Split(new string[] { ": " }, StringSplitOptions.None)[1], "dd/MM/yyyy", CultureInfo.InvariantCulture);
                                    break;
                                case "Giờ":
                                    time = splited[i].Split(new string[] { ": " }, StringSplitOptions.None)[1];
                                    break;
                                default:
                                    break;
                            }
                        }
                        if (dateTime != null && time != null)
                        {
                            dateTime = dateTime.Value.AddHours(Convert.ToInt32(time.Split('h')[0]));
                            if (time.Split('h').Length == 2)
                            {
                                if (int.TryParse(time.Split('h')[1], out int minute))
                                    dateTime = dateTime.Value.AddMinutes(Convert.ToInt32(minute));
                            }
                            // -new DateTime(1970, 1, 1) for UnixTimeStamp.
                            // -7 because of GMT + 7.
                            item.DateExamInUnix = (long)dateTime.Value.Subtract(new DateTime(1970, 1, 1)).Add(new TimeSpan(-7, 0, 0)).TotalSeconds;
                        }
                    }
            }
            catch
            {
                result.Clear();
                result = null;
            }

            return result;
        }

        public static List<SubjectFee>? GetSubjectFeeList(string sessionId, int year = 20, int semester = 1)
        {
            if (semester < 1 || semester > 3)
                throw new ArgumentException();

            List<SubjectFee>? result = new List<SubjectFee>();

            try
            {
                HttpClient client = new HttpClient();
                client.BaseAddress = new Uri(BASE_ADDRESS);
                client.DefaultRequestHeaders.Add("Cookie", $"ASP.NET_SessionId={sessionId};");
                HttpResponseMessage response = client.GetAsync($"/WebAjax/evLopHP_Load.aspx?E=THPhiLoad&Code={year}{(semester <= 2 ? semester : 2)}{(semester == 3 ? 1 : 0)}").Result;

                if (!response.IsSuccessStatusCode)
                    throw new Exception(String.Format("The request has return code {0}.", response.StatusCode));

                HtmlDocument htmlDoc = new HtmlDocument();
                htmlDoc.LoadHtml(response.Content.ReadAsStringAsync().Result);

                HtmlDocument htmlDocFee = new HtmlDocument();
                htmlDocFee.LoadHtml(htmlDoc.GetElementbyId("THocPhi_GridInfo").InnerHtml);
                var rowListFee = htmlDocFee.DocumentNode.SelectNodes("//tr[@class='GridRow']");

                if (rowListFee != null && rowListFee.Count > 0)
                    foreach (HtmlNode row in rowListFee)
                    {
                        HtmlDocument httpTemp2 = new HtmlDocument();
                        httpTemp2.LoadHtml(row.InnerHtml);
                        var cellCollection = httpTemp2.DocumentNode.SelectNodes("//td[contains(@class, 'GridCell')]");

                        SubjectFee item = new SubjectFee();
                        item.ID = cellCollection[1].InnerText;
                        item.Name = cellCollection[2].InnerText;
                        item.Credit = ConvertTo<float>(cellCollection[3].InnerText);
                        item.IsHighQuality = cellCollection[4].Attributes["class"].Value.Contains("GridCheck");
                        item.Price = ConvertTo<double>(cellCollection[5].InnerText.Replace(",", null));
                        item.Debt = cellCollection[6].Attributes["class"].Value.Contains("GridCheck");
                        item.IsReStudy = cellCollection[7].Attributes["class"].Value.Contains("GridCheck");
                        item.VerifiedPaymentAt = cellCollection[8].InnerText;

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

        public static AccountInformation? GetAccountInformation(string sessionId)
        {
            string? GetIDFromTitleBar(string stringTitleBar)
            {
                try
                {
                    int openCase = stringTitleBar.IndexOf("(");
                    int closeCase = stringTitleBar.IndexOf(")");
                    int stringLength = (stringTitleBar.IndexOf(")")) - (stringTitleBar.IndexOf("(") + 1);
                    return stringTitleBar.Substring(openCase + 1, stringLength);
                }
                catch
                {
                    return null;
                }
            }

            AccountInformation? accInfo = new AccountInformation();

            try
            {
                HttpClient client = new HttpClient();
                client.BaseAddress = new Uri(BASE_ADDRESS);
                client.DefaultRequestHeaders.Add("Cookie", $"ASP.NET_SessionId={sessionId};");
                HttpResponseMessage response = client.GetAsync($"/PageCaNhan.aspx").Result;

                if (!response.IsSuccessStatusCode)
                    throw new Exception(String.Format("The request has return code {0}.", response.StatusCode));

                HtmlDocument htmlDoc = new HtmlDocument();
                htmlDoc.LoadHtml(response.Content.ReadAsStringAsync().Result);
                accInfo.ID = GetIDFromTitleBar(htmlDoc.GetElementbyId("Main_lblHoTen").InnerText);
                accInfo.Name = htmlDoc.GetElementbyId("CN_txtHoTen").GetAttributeValue("value", null);
                accInfo.DateOfBirth = DateTime.ParseExact(htmlDoc.GetElementbyId("CN_txtNgaySinh").GetAttributeValue("value", null), "dd/MM/yyyy", CultureInfo.InvariantCulture);
                switch (htmlDoc.GetElementbyId("CN_txtGioiTinh").GetAttributeValue("value", null).ToLower())
                {
                    case "nam":
                        accInfo.Gender = Gender.Male;
                        break;
                    case "nữ":
                        accInfo.Gender = Gender.Female;
                        break;
                    default:
                        accInfo.Gender = Gender.Unknown;
                        break;
                }
                accInfo.IdentityID = htmlDoc.GetElementbyId("CN_txtSoCMND").GetAttributeValue("value", null);
                accInfo.ClassName = htmlDoc.GetElementbyId("CN_txtLop").Attributes.First(p => p.Name.ToLower() == "value").Value;

                accInfo.BankInfo =
                    String.Format(
                        "{0} ({1})",
                        htmlDoc.GetElementbyId("CN_txtTKNHang").GetAttributeValue("value", null),
                        htmlDoc.GetElementbyId("CN_txtNgHang").GetAttributeValue("value", null)
                        );
                accInfo.HIID = htmlDoc.GetElementbyId("CN_txtSoBHYT").GetAttributeValue("value", null);
                accInfo.PersonalEmail = htmlDoc.GetElementbyId("CN_txtMail2").GetAttributeValue("value", null);
                accInfo.PhoneNumber = htmlDoc.GetElementbyId("CN_txtPhone").GetAttributeValue("value", null);
                accInfo.EducationEmail = htmlDoc.GetElementbyId("CN_txtMail1").GetAttributeValue("value", null);
            }
            catch
            {
                accInfo = null;
            }

            return accInfo;
        }

        private static T? ConvertTo<T>(string str)
        {
            T? result = default;

            Type t = typeof(T);
            try
            {
                if (t == typeof(int))
                {
                    int valueInt = Convert.ToInt32(str);
                    result = (T)Convert.ChangeType(valueInt, typeof(T));
                }
                else if (t == typeof(float))
                {
                    float valueFloat = Convert.ToSingle(str);
                    result = (T)Convert.ChangeType(valueFloat, typeof(T));
                }
                else if (t == typeof(double))
                {
                    double valueDouble = Convert.ToInt32(str);
                    result = (T)Convert.ChangeType(valueDouble, typeof(T));
                }
            }
            catch
            {

            }

            return result;
        }
    }
}
