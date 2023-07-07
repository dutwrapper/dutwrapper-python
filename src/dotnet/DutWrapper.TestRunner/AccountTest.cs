namespace DutWrapper.TestRunner
{
    [TestClass]
    public class AccountTest
    {
        public string? SESSION_ID = null;

        [TestMethod]
        public void TestEntireAccountFunction()
        {
            string? data_env = Environment.GetEnvironmentVariable("dut_account");
            if (data_env == null)
                throw new ArgumentException("dut_account environment variable not found. Please, add or modify this environment in format \"username|password\"");
            string[] data = data_env.Split("|");
            if (data.Length != 2)
                throw new ArgumentException("Something wrong with your dut_account environment variable. Please, add or modify this environment in format \"username|password\"");

            SESSION_ID = DutWrapper.Account.GenerateNewSessionId();
            if (SESSION_ID == null)
                throw new HttpRequestException("Failed while getting new Session ID! This test cannot continue.");

            DutWrapper.Account.Login(SESSION_ID, data[0], data[1]);

            var result = DutWrapper.Account.IsLoggedIn(SESSION_ID);
            Console.WriteLine($"IsLoggedIn: {result} (Session ID: {SESSION_ID})");
            if (result != Model.LoginStatus.LoggedIn)
                throw new HttpRequestException("Failed while logging you in! This test cannot continue.");

            var result3 = DutWrapper.Account.GetSubjectScheduleList(SESSION_ID, 22, 1);
            Console.WriteLine($"Subject schedule count: {(result3 == null ? null : result3.Count)} (Session ID: {SESSION_ID})");
            var result4 = DutWrapper.Account.GetSubjectFeeList(SESSION_ID, 22, 1);
            Console.WriteLine($"Subject fee count: {(result4 == null ? null : result4.Count)} (Session ID: {SESSION_ID})");
            var result5 = DutWrapper.Account.GetAccountInformation(SESSION_ID);
            Console.WriteLine($"Is account information null: {result5 == null} (Session ID: {SESSION_ID})");

            DutWrapper.Account.Logout(SESSION_ID);
            Console.WriteLine($"Logged out (Session ID: {SESSION_ID})");

            var result2 = DutWrapper.Account.IsLoggedIn(SESSION_ID);
            Console.WriteLine($"IsLoggedIn: {result2} (Session ID: {SESSION_ID})");
        }
    }
}