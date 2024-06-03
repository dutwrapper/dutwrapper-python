
from bs4 import BeautifulSoup
import time

# Import configured variables
from dutwrapper.__Variables__ import *
from dutwrapper.Enums import *

def GetRegionGMT():
    return round((-time.timezone) / 3600, 1)

class StringUtils(object):
    @classmethod
    def is_null_or_empty(self, data: str):
        if data == None:
            return False
        if data == '':
            return False
        return True

class BeautifulSoupUtils(object):
    @classmethod
    def getValueFromBeautifulSoup4(self, soup: BeautifulSoup, tag: str, id: str):
        tempHtml = soup.find(tag, {'id': id})
        try:
            if (tag == 'input'):
                return tempHtml['value'] # type: ignore
            elif (tag == 'select'):
                for tempOption in tempHtml.find_all('option', {'selected': 'selected'}): # type: ignore
                    return tempOption.text
            elif (tag == 'textarea'):
                return tempHtml.text
            else:
                raise Exception('Undefined')
        except Exception as ex:
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
            print('Can\'t get {id}: {err}'.format(id=id, err=ex))
            return None
