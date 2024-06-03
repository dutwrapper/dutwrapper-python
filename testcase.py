import dutwrapper
import dutwrapper.Account as Account
from dutwrapper.Enums import NewsType
import unittest
import os

def Test_NewsGlobal():
    print()
    MAX_NEWS = 5
    for i in range(1, MAX_NEWS + 1, 1):
        data = dutwrapper.get_news(NewsType.Global, i)
        print(data)
        print("News Global in page {page}: {count}".format(page=i, count=len(data['news_list'])))
    pass

def Test_NewsSubject():
    print()
    MAX_NEWS = 5
    for i in range(1, MAX_NEWS + 1, 1):
        data = dutwrapper.get_news(NewsType.Subjects, i)
        print(data)
        print("News Subject in page {page}: {count}".format(page=i, count=len(data['news_list'])))
    pass

def Test_Account():
    year = 20
    semester = 2
    study_at_summer = False

    if (os.getenv('dut_account') == None):
        raise Exception("[Error] No dut_account environment variable found! This test will be ignored...")
    username = os.getenv('dut_account').split('|')[0]
    password = os.getenv('dut_account').split('|')[1]

    if (os.getenv('school_year') == None):
        raise Exception("[Error] No school_year environment variable found. This test will be ignored...")        
    year = os.getenv('school_year').split('|')[0]
    semester = os.getenv('school_year').split('|')[1]
    study_at_summer = True if (os.getenv('school_year').split('|')[2] == 1) else False

    sId = Account.generate_session_id()
    if (sId == None):
        raise Exception("[Error] Can't get new Session ID. Try again later. This test will be ignored...")

    print('[Test] Login')
    print(Account.login(sessionID=sId, username=username, password=password))
    print()
    print('[Test] Check if logged in')
    print(Account.is_logged_in(sessionID=sId))
    print()
    print('[Test] Get subject schedule')
    print(Account.fetch_subject_schedule(sessionID=sId, year=year, semester=semester, studyAtSummer=study_at_summer))
    print()
    print('[Test] Get subject fee')
    print(Account.fetch_subject_fee(sessionID=sId, year=year, semester=semester, studyAtSummer=study_at_summer))
    print()
    print('[Test] Get account information')
    print(Account.fetch_account_information(sessionID=sId))
    print()
    print('[Test] Get account training status')
    print(Account.fetch_account_training_status(sessionID=sId))
    print()
    print('[Test] Logout')
    print(Account.logout(sessionID=sId))
    print()
    print('[Test] Check if this session has logged out')
    print(Account.is_logged_in(sessionID=sId))
    print()
    pass

class TestEntirePackage(unittest.TestCase):
    def test_news(self):
        Test_NewsGlobal()
        Test_NewsSubject()
        pass

    def test_accounts(self):
        Test_Account()
        pass
