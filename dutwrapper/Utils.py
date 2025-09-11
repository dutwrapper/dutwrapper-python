from bs4 import BeautifulSoup, ResultSet
from datetime import datetime, timezone, timedelta
import time

# Import configured variables
import dutwrapper.__Variables__ as Variables
import requests

class Utils(object):
    def EnsureHaveInternetAccess():
        response = requests.get(Variables.URL_TEST_INTERNET)
        if not response.ok:
            raise ConnectionError()
        pass
    def EnsureDutSvOnline():
        response = requests.get(Variables.BASEURL_SV)
        if not response.ok:
            raise ConnectionError()
        pass
    def GetCurrentSchoolYear() -> dict:
        try:
            # Get elements from web
            webHTML = requests.get(Variables.URL_DUT_SCHEDULE)
            # Convert to BeautifulSoup
            soup = BeautifulSoup(webHTML.content, 'lxml')
            # Find
            cbbYear = BeautifulSoupUtils.GetValueInBeautifulSoup(soup, 'select', 'year-select')
            cbbWeekSelect = soup.find('select', {'id': 'week-container'})
            cbbWeekText = None
            cbbWeek = None
            
            for weekItem in cbbWeekSelect.find_all('option'):
                if 'tuần 1 :' in weekItem.getText().lower():
                    cbbWeekText = weekItem.getText()
            
            if (cbbWeekText != None):
                stringFirstDate = cbbWeekText.split(':')[1].strip().split('-')
                if (len(stringFirstDate) == 3):
                    currentDateUnix = DateTimeUtils.CurrentTimeAsUnix()
                    firstDateWeekUnix = DateTimeUtils.FromUTCp7(
                        int(stringFirstDate[2]),
                        int(stringFirstDate[1]),
                        int(stringFirstDate[0]),
                        0,0,0,0
                    )
                    cbbWeek = ((currentDateUnix - firstDateWeekUnix) / (1000 * 60 * 60 * 24 * 7) + 1)

            return {
                'schoolYear': str(cbbYear).strip(),
                'schoolYearVal': int(str(cbbYear).strip().split('-')[0][2:].strip()),
                'week': int(cbbWeek),
                'firstWeekDate': firstDateWeekUnix
            }
        except Exception as ex:
            print(ex)
            return None

class DateTimeUtils(object):
    def CurrentGMT() -> int:
        return round((-time.timezone) / 3600, 1)
    def CurrentTimeAsUnix() -> int:
        return int(time.time_ns() // 1_000_000)
    def FromUTC(year: int, month: int = 1, day: int = 1, hour: int = 0, minute: int = 0, second: int = 0, millisecond: int = 0) -> int:
        utc = timezone(timedelta())
        return int(datetime.timestamp(datetime(year, month, day, hour, minute, second, millisecond, tzinfo=utc)) * 1000)
    def FromUTCp7(year: int, month: int = 1, day: int = 1, hour: int = 0, minute: int = 0, second: int = 0, millisecond: int = 0) -> int:
        utc_p7 = timezone(timedelta(hours=7))
        return int(datetime.timestamp(datetime(year, month, day, hour, minute, second, millisecond, tzinfo=utc_p7)) * 1000)

class StringUtils(object):
    @classmethod
    def IsNullOrEmpty(self, data: str):
        try:
            if data == None:
                return False
            elif data == '':
                return False
            else:
                return True
        except:
            return True

class BeautifulSoupUtils(object):
    @classmethod
    def HasGridCheckAttributeInResultSet(self, rs: ResultSet) -> bool:
        return BeautifulSoupUtils.HasAttributeInResultSet(rs=rs, attr='GridCheck')

    @classmethod
    def HasAttributeInResultSet(self, rs: ResultSet, attr: str) -> bool:
        return True if (attr in rs.attrs.get('class')) else False

    @classmethod
    def GetValueInBeautifulSoup(self, soup: BeautifulSoup, tag: str, id: str):
        tempHtml = soup.find(tag, {'id': id})
        try:
            if (tag == 'input'):
                return tempHtml['value']
            elif (tag == 'select'):
                for tempOption in tempHtml.find_all('option'):
                    if (tempOption.has_attr('selected')):
                        return tempOption.text
                return None
            elif (tag == 'textarea'):
                return tempHtml.text
            else:
                raise Exception('Undefined')
        except Exception as ex:
            if (Variables.DEBUG_LOG):
                print('Can\'t get {id}: {err}'.format(id=id, err=ex))
            return None
        
    @classmethod
    def getIsCheckedFromBeautifulSoup4(self, soup: BeautifulSoup, tag: str, id: str):
        tempHtml = soup.find(tag, {'id': id})
        try:
            if (tempHtml['checked'] != None):
                return True
            return False
        except Exception as ex:
            if (Variables.DEBUG_LOG):
                print('Can\'t get {id}: {err}'.format(id=id, err=ex))
            return None

def setDebugLog(enabled: bool):
    Variables.DEBUG_LOG = enabled