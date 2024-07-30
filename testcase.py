
import json
import unittest
import os

import dutwrapper.News as News
from dutwrapper.News import NewsType
import dutwrapper.Account as Account

def pretty_print_dict(item: dict):
    print(json.dumps(item, indent=4, ensure_ascii=False))

def Test_NewsGlobal():
    print()
    MAX_NEWS = 5
    for i in range(1, MAX_NEWS + 1, 1):
        data = News.get_news(NewsType.Global, i)
        pretty_print_dict(data)
        print("News Global in page {page}: {count}".format(page=i, count=len(data)))
    pass

def Test_NewsSubject():
    print()
    MAX_NEWS = 5
    for i in range(1, MAX_NEWS + 1, 1):
        data = News.get_news(NewsType.Subjects, i)
        pretty_print_dict(data)
        print("News Subject in page {page}: {count}".format(page=i, count=len(data)))
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
        pass

    def test_accounts(self):
        Test_Account()
        pass
