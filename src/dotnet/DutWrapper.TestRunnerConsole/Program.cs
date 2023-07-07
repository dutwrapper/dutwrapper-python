namespace DutWrapper.TestRunnerConsole
{
    internal class Program
    {
        static void Main(string[] args)
        {
            var newsTest = new TestRunner.NewsTest();
            newsTest.GetNews_Global();
            newsTest.GetNews_Subject();

            var accountTest = new TestRunner.AccountTest();
            accountTest.TestEntireAccountFunction();
        }
    }
}