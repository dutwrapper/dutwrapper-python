from typing import Final

class DutUrlVariables(object):
    @classmethod
    def DutSvBase(self):
        return 'https://sv.dut.udn.vn'
    
    @classmethod
    def DutSvNews(self, news, page: int, tab: int):
        return '{base}/WebAjax/evLopHP_Load.aspx?E={news}&PAGETB={page}&COL=TieuDe&NAME=&TAB={tab}'.format(
            base=DutUrlVariables.DutSvBase(),
            news=news,
            page=page,
            tab=tab
        )
    
    @classmethod
    def DutSvLogin(self):
        return '{base}/PageDangNhap.aspx'.format(
            base=DutUrlVariables.DutSvBase()
        )
    
    @classmethod
    def DutSvLogout(self):
        return '{base}/PageLogout.aspx'.format(
            base=DutUrlVariables.DutSvBase()
        )
    
    @classmethod
    def DutSvCheckLogin(self):
        return '{base}/WebAjax/evLopHP_Load.aspx?E=TTKBLoad&Code=2020'.format(
            base=DutUrlVariables.DutSvBase()
        )
    
    @classmethod
    def DutSvSubjectSchedule(self, nam: int, hocKy: int, hocHe: bool):
        return '{base}/WebAjax/evLopHP_Load.aspx?E=TTKBLoad&Code={nam}{hocky}{hoche}'.format(
            base=DutUrlVariables.DutSvBase(),
            nam=nam,
            hocky=hocKy,
            hoche=1 if hocHe == True else 0
        )
    
    @classmethod
    def DutSvSubjectFee(self, nam: int, hocKy: int, hocHe: bool):
        return '{base}/WebAjax/evLopHP_Load.aspx?E=THPhiLoad&Code={nam}{hocky}{hoche}'.format(
            base=DutUrlVariables.DutSvBase(),
            nam=nam,
            hocky=hocKy,
            hoche=1 if hocHe == True else 0
        )
    
    @classmethod
    def DutSvStudentInfo(self):
        return '{base}/PageCaNhan.aspx'.format(
            base=DutUrlVariables.DutSvBase()
        )
    
    @classmethod
    def DutSvStudentInfo(self):
        return '{base}/PageKQRL.aspx'.format(
            base=DutUrlVariables.DutSvBase()
        )
    pass

BASEURL_SV: Final = 'https://sv.dut.udn.vn'
URL_ACCOUNTLOGIN2: Final = 'https://sv.dut.udn.vn/PageDangNhap.aspx'
URL_NEWS: Final = 'https://sv.dut.udn.vn/WebAjax/evLopHP_Load.aspx?E={news}&PAGETB={page}&COL=TieuDe&NAME=&TAB={tab}'
URL_ACCOUNTLOGIN: Final = 'https://sv.dut.udn.vn/PageDangNhap.aspx'
URL_ACCOUNTLOGOUT: Final = 'https://sv.dut.udn.vn/PageLogout.aspx'
URL_ACCOUNTCHECKLOGIN: Final = 'https://sv.dut.udn.vn/WebAjax/evLopHP_Load.aspx?E=TTKBLoad&Code=2020'
URL_ACCOUNTSCHEDULE: Final = 'https://sv.dut.udn.vn/WebAjax/evLopHP_Load.aspx?E=TTKBLoad&Code={nam}{hocky}{hoche}'
URL_ACCOUNTFEE: Final = 'https://sv.dut.udn.vn/WebAjax/evLopHP_Load.aspx?E=THPhiLoad&Code={nam}{hocky}{hoche}'
URL_ACCOUNTINFORMATION: Final = 'https://sv.dut.udn.vn/PageCaNhan.aspx'
URL_ACCOUNTTRAININGSTATUS: Final = 'https://sv.dut.udn.vn/PageKQRL.aspx'

URL_TEST_INTERNET: Final = 'https://example.com'
URL_DUT_SCHEDULE: Final = 'https://lichtuan.dut.udn.vn/'

DEBUG_LOG = True