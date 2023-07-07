import dutwrapper
import dutwrapper.Session as Session
from dutwrapper.Enums import NewsType
import unittest
import os

def Test_NewsGlobal():
    MAX_NEWS = 5
    for i in range(1, MAX_NEWS + 1, 1):
        data = dutwrapper.GetNews(NewsType.Global, i)
        print("News Global in page {page}: {count}".format(page=i, count=len(data['news_list'])))
    pass

def Test_NewsSubject():
    MAX_NEWS = 5
    for i in range(1, MAX_NEWS + 1, 1):
        data = dutwrapper.GetNews(NewsType.Subjects, i)
        print("News Subject in page {page}: {count}".format(page=i, count=len(data['news_list'])))
    pass

def Test_Account():
    year = 22
    semester = 1
    study_at_summer = False

    data = os.getenv('dut_account')
    if (data == None):
        print("Warning: No username/password found in environment variable. This test will be ignored...")
        data = ""
        return

    username = data.split('|')[0]
    password = data.split('|')[1]
    sId = Session.GenerateSessionID()
    if (sId == None):
        print("Warning: Invalid username/password. This test will be ignored...")
        sId = ""
        return

    Session.Login(sessionID=sId, username=username, password=password)
    print(Session.IsLoggedIn(sessionID=sId))
    Session.GetSubjectSchedule(sessionID=sId, year=year, semester=semester, studyAtSummer=study_at_summer)
    Session.GetSubjectFee(sessionID=sId, year=year, semester=semester, studyAtSummer=study_at_summer)
    Session.GetAccountInformation(sessionID=sId)
    Session.Logout(sessionID=sId)
    print(Session.IsLoggedIn(sessionID=sId))
    pass

class TestEntirePackage(unittest.TestCase):
    def test_news(self):
        Test_NewsGlobal()
        Test_NewsSubject()
        pass

    def test_accounts(self):
        Test_Account()
        pass
