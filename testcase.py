
import json
import unittest
import os

import dutwrapper.News as News
from dutwrapper.News import NewsType
import dutwrapper.Account as Account
from dutwrapper.Utils import Utils

def pretty_print_dict(item: dict):
    print(json.dumps(item, indent=4, ensure_ascii=False))

def Test_NewsGlobal():
    print()
    MAX_NEWS = 3
    for i in range(1, MAX_NEWS + 1, 1):
        data = News.get_news(NewsType.Global, i)
        pretty_print_dict(data)
        print("News Global in page {page}: {count}".format(page=i, count=len(data)))
    pass

def Test_NewsSubject():
    print()
    MAX_NEWS = 3
    for i in range(1, MAX_NEWS + 1, 1):
        data = News.get_news(NewsType.Subject, i)
        pretty_print_dict(data)
        print("News Subject in page {page}: {count}".format(page=i, count=len(data)))
    pass

def Test_NewsStudentAffairs():
    print()
    MAX_NEWS = 3
    for i in range(1, MAX_NEWS + 1, 1):
        data = News.get_news(NewsType.StudentAffairs, i)
        pretty_print_dict(data)
        print("News Student affairs in page {page}: {count}".format(page=i, count=len(data)))
    pass

def Test_NewsExamination():
    print()
    MAX_NEWS = 3
    for i in range(1, MAX_NEWS + 1, 1):
        data = News.get_news(NewsType.Examination, i)
        pretty_print_dict(data)
        print("News Examination in page {page}: {count}".format(page=i, count=len(data)))
    pass

def Test_NewsTuitionFee():
    print()
    MAX_NEWS = 3
    for i in range(1, MAX_NEWS + 1, 1):
        data = News.get_news(NewsType.TuitionFee, i)
        pretty_print_dict(data)
        print("News Tuition Fee in page {page}: {count}".format(page=i, count=len(data)))
    pass

def Test_NewsStatuteRegulation():
    print()
    MAX_NEWS = 3
    for i in range(1, MAX_NEWS + 1, 1):
        data = News.get_news(NewsType.StatuteRegulation, i)
        pretty_print_dict(data)
        print("News Statute and Regulation in page {page}: {count}".format(page=i, count=len(data)))
    pass

def Test_Account():
    year = 20
    semester = 2
    study_at_summer = False

    if (os.getenv('DUT_ACCOUNT') == None):
        raise Exception("[Error] No \'DUT_ACCOUNT\' environment variable found! This test will be ignored...")
    username = os.getenv('DUT_ACCOUNT').split('|')[0]
    password = os.getenv('DUT_ACCOUNT').split('|')[1]

    if (os.getenv('school_year') == None):
        raise Exception("[Error] No school_year environment variable found. This test will be ignored...")        
    year = os.getenv('school_year').split('|')[0]
    semester = os.getenv('school_year').split('|')[1]
    study_at_summer = True if (os.getenv('school_year').split('|')[2] == 1) else False

    session = Account.generate_new_session()
    if (session == None):
        raise Exception("[Error] Can't get new Session! Try again later.")

    print('[Test] Login')
    Account.login(session=session, username=username, password=password)
    print('Done!')
    print()
    print('[Test] Check if logged in')
    print(Account.is_logged_in(session=session))
    print()
    print('[Test] Get subject schedule')
    pretty_print_dict(Account.fetch_subject_information(session=session, year=year, semester=semester, studyAtSummer=study_at_summer))
    print()
    print('[Test] Get subject fee')
    pretty_print_dict(Account.fetch_subject_fee(session=session, year=year, semester=semester, studyAtSummer=study_at_summer))
    print()
    print('[Test] Get account information')
    pretty_print_dict(Account.fetch_student_information(session=session))
    print()
    print('[Test] Get account training status')
    pretty_print_dict(Account.fetch_training_result(session=session))
    print()
    print('[Test] Logout')
    Account.logout(session=session)
    print('Done!')
    print()
    print('[Test] Check if this session has logged out')
    print(Account.is_logged_in(session=session))
    print()
    pass

class TestEntirePackage(unittest.TestCase):
    def test_news(self):
        Test_NewsGlobal()
        Test_NewsSubject()
        Test_NewsStudentAffairs()
        Test_NewsExamination()
        Test_NewsTuitionFee()
        Test_NewsStatuteRegulation()
        pass

    def test_accounts(self):
        Test_Account()
        pass

    def test_utils(self):
        Utils.EnsureDutSvOnline()
        print('Done!')
        Utils.EnsureHaveInternetAccess()
        print('Done!')
        print(Utils.GetCurrentSchoolYear())
        print('Done!')
        pass