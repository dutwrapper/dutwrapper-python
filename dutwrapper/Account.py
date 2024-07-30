
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import requests
from requests.structures import CaseInsensitiveDict
	
import dutwrapper.__Variables__ as Variables
from dutwrapper.Utils import *

class Session:
    def __init__(self, session_id: str = None, view_state: str = None, view_state_generator: str = None):
        self.session_id = session_id
        self.view_state = view_state
        self.view_state_generator = view_state_generator

    def export_session_id_to_cookie(self) -> str:
        return "ASP.NET_SessionId={id};".format(id=self.session_id)
    
    def ensure_logged_in(self):
        self.ensure_valid_session_id()
        if (is_logged_in(session=self) != 0):
            raise Exception('You are not logged in.')
        return
    
    def ensure_valid_session_id(self):
        if (self.session_id == None):
            raise Exception('SessionID not found!')
        return
    
    def ensure_valid_login_form(self):
        self.ensure_valid_session_id()
        if (self.view_state == None):
            raise Exception('ViewState not found! This is required when login.')
        if (self.view_state_generator == None):
            raise Exception('ViewStateGenerator not found! This is required when login.')
        return
    
def generate_new_session() -> Session:
    WEB_SESSION = requests.Session()
    response = WEB_SESSION.get(Variables.URL_ACCOUNTLOGIN)
    if (response.status_code in [200, 204]):
        session = Session(None, None, None)
        # Get Session ID
        temp = WEB_SESSION.cookies.get_dict()
        if ('ASP.NET_SessionId' in temp.keys()):
            session.session_id = temp['ASP.NET_SessionId']
        # Get ViewState and ViewStateGenerator
        soup = BeautifulSoup(response.content, 'lxml')
        session.view_state = BeautifulSoupUtils.getValueFromBeautifulSoup4(soup=soup, tag='input', id='__VIEWSTATE')
        session.view_state_generator = BeautifulSoupUtils.getValueFromBeautifulSoup4(soup=soup, tag='input', id='__VIEWSTATEGENERATOR')
        return session
    else:
        return Session(None, None, None)

def is_logged_in(session: Session) -> int:
    """
    Check if your account is logged in from sv.dut.udn.vn.

    Returns:
    - 0: `Logged in`
    - 1: `Not logged in - Logged out`
    """
    session.ensure_valid_session_id()
    
    try:
        headers = CaseInsensitiveDict()
        # headers["Cookie"] = "ASP.NET_SessionId={id};".format(id=session.session_id)
        headers["Cookie"] = session.export_session_id_to_cookie()
        response = requests.get(Variables.URL_ACCOUNTCHECKLOGIN, headers=headers) 
        # If returned code 2xx, return LoggedIn (0)
        if (response.status_code in [200, 204]):
            return 0
        # TODO: We need to seperate login status here, but we don't have any document about this. So, just return NotLoggedIn (1)
        else:
            return 1
    except Exception as ex:
        # If something went wrong, return anything to NotLoggedIn (1)
        if (Variables.DEBUG_LOG):
            print(ex)
        return 1

def login(session: Session, username: str, password: str):
    """
    Login to sv.dut.udn.vn using your account provided by DUT school.
    session (Dict): Session you got from `generate_session()`
    username (string): Username (i.e. Student ID).
    password (string): Password
    """
    session.ensure_valid_login_form()

    # 
    dataRequest = {}
    dataRequest['__VIEWSTATE'] = session.view_state
    dataRequest['__VIEWSTATEGENERATOR'] = session.view_state_generator
    dataRequest['_ctl0:MainContent:DN_txtAcc'] = username
    dataRequest['_ctl0:MainContent:DN_txtPass'] = password
    dataRequest['_ctl0:MainContent:QLTH_btnLogin'] = 'Đăng+nhập'
    # print(self.SessionID)
    headers = CaseInsensitiveDict()
    # headers["Cookie"] = "ASP.NET_SessionId={id};".format(id=session.session_id)
    headers["Cookie"] = session.export_session_id_to_cookie()
    requests.post(Variables.URL_ACCOUNTLOGIN, data=dataRequest, headers=headers)
    #
    return

def logout(session: Session):
    """
    Logout your account from sv.dut.udn.vn.
    """
    session.ensure_valid_session_id()

    headers = CaseInsensitiveDict()
    # headers["Cookie"] = "ASP.NET_SessionId={id};".format(id=session.session_id)
    headers["Cookie"] = session.export_session_id_to_cookie()
    requests.get(Variables.URL_ACCOUNTLOGOUT, headers=headers)
    return

def __string2ExamSchedule__(src: str):
    # If string is empty, return {}
    if (len(src.replace(' ', '')) == 0):
        return {
            'examDate': None,
            'examRoom': None
        }
    # Split string.
    dateSplitted = src.split(', ')
    dataList = []
    for item in dateSplitted:
        dataList.append({
            'type': item.split(': ')[0],
            'value': item.split(': ')[1]
        })
    # Preprocessing
    date = datetime(2000, 1, 1)
    room = None
    for item in dataList:
        if item['type'] == 'Ngày':
            splitted = item['value'].split('/')
            if len(splitted) == 3:
                date = date.replace(year=int(splitted[2]), month=int(splitted[1]), day=int(splitted[0]))
        elif item['type'] == 'Phòng':
            room = item['value']
        elif item['type'] == 'Giờ':
            splitted = item['value'].split('h')
            if len(splitted) > 0:
                date = date.replace(hour=int(splitted[0]))
            if len(splitted) > 1:
                date = date.replace(minute=int(splitted[1]))
    date = date - timedelta(hours=7) + timedelta(hours=GetRegionGMT())
    # Return
    result = {}
    result['examDate'] = round(datetime.timestamp(date) * 1000, 0)
    result['examRoom'] = room
    return result

def fetch_subject_information(session: Session, year: int = 20, semester: int = 1, studyAtSummer: bool = False):
    """
    Get all subject schedule (study and examination) from a year you choosed.
    year (int): 2-digit year.
    semester (int): 1 or 2
    studyAtSummer (bool): Show schedule if you has studied in summer. 'semester' must be 2, otherwise will getting exception.
    """
    session.ensure_logged_in()

    result = []
    try:
        url = Variables.URL_ACCOUNTSCHEDULE.format(nam = year, hocky = semester, hoche = 1 if studyAtSummer else 0)
        headers = CaseInsensitiveDict()
        # headers["Cookie"] = "ASP.NET_SessionId={id};".format(id=session.session_id)
        headers["Cookie"] = session.export_session_id_to_cookie()
        webHTML = requests.get(url, headers=headers)
        soup = BeautifulSoup(webHTML.content, 'lxml')  # type: ignore
        # Find all subjects schedule
        schStudyTable = soup.find('table', {'id': 'TTKB_GridInfo'})
        schStudyRow = schStudyTable.find_all('tr', {'class': 'GridRow'})  # type: ignore
    
        for i in range(0, len(schStudyRow) - 1, 1):
            cell = schStudyRow[i].find_all('td', {'class':'GridCell'})
            resultRow = {}
            # ID
            resultRow['id'] = cell[1].text
            # Name
            resultRow['name'] = cell[2].text
            # Credit
            resultRow['credit'] = float(cell[3].text)
            # Is High Quality
            resultRow['is_high_quality'] = True if ('GridCheck' in cell[5].attrs.get('class')) else False
            # Lecturer name
            resultRow['lecturer'] = cell[6].text
            # Schedule study area
            resultRow['schedule_study'] = {}
            # Schedule study
            if (cell[7].text != None and len(cell[7].text) > 0):
                resultRow['schedule_study']['schedule_list'] = []
                cellSplit = cell[7].text.split('; ') if ('; ' in cell[7].text) else [cell[7].text]
                for cellSplitItem in cellSplit:
                    item = {}
                    item['day_of_week'] = 0 if ('CN' in cellSplitItem.upper()) else (int(cellSplitItem.split(',')[0].split(' ')[1]) - 1)
                    item['lesson_affected'] = {}
                    item['lesson_affected']['start'] = cellSplitItem.split(',')[1].split('-')[0]
                    item['lesson_affected']['end'] = cellSplitItem.split(',')[1].split('-')[1]
                    item['room'] = cellSplitItem.split(',')[2]
                    resultRow['schedule_study']['schedule_list'].append(item)
            else:
                resultRow['schedule_study']['schedule_list'] = []
            # Weeks
            if (cell[8].text != None and len(cell[8].text) > 0):
                resultRow['schedule_study']['week_affected'] = []
                cellSplit = cell[8].text.split(';') if (';' in cell[8].text) else [cell[8].text]
                for cellSplitItem in cellSplit:
                    item = {}
                    item['start'] = cellSplitItem.split('-')[0]
                    item['end'] = cellSplitItem.split('-')[1]
                    resultRow['schedule_study']['week_affected'].append(item)
            else:
                resultRow['schedule_study']['week_affected'] = []
            # Point formula
            resultRow['point_formula'] = cell[10].text
            # Append to schedule list
            result.append(resultRow)
        
        # Find all subjects schedule examination
        schExamTable = soup.find('table', {'id': 'TTKB_GridLT'})
        schExamRow = schExamTable.find_all('tr', {'class': 'GridRow'})  # type: ignore

        for i in range(0, len(schExamRow), 1):
            cell = schExamRow[i].find_all('td', {'class':'GridCell'})
            for j in range(0, len(result), 1):
                if (result[j]['id'] == cell[1].text):
                    result[j]['schedule_exam'] = {}
                    result[j]['schedule_exam']['group'] = cell[3].text
                    result[j]['schedule_exam']['is_global'] = True if ('GridCheck' in cell[4].attrs.get('class')) else False
                    result[j]['schedule_exam']['date'] = __string2ExamSchedule__(cell[5].text)['examDate']
                    result[j]['schedule_exam']['room'] = __string2ExamSchedule__(cell[5].text)['examRoom']
    except Exception as ex:
        if (Variables.DEBUG_LOG):
            print(ex)
        result.clear()
    finally:
        return result

def fetch_subject_fee(session: Session, year: int = 20, semester: int = 1, studyAtSummer: bool = False):
    """
    Get all subject fee from a year you choosed.
    year (int): 2-digit year.
    semester (int): 1 or 2
    studyAtSummer (bool): Show schedule if you has studied in summer. 'semester' must be 2, otherwise will getting exception.
    """
    session.ensure_logged_in()
    
    result = []
    try:
        headers = CaseInsensitiveDict()
        # headers["Cookie"] = "ASP.NET_SessionId={id};".format(id=session.session_id)
        headers["Cookie"] = session.export_session_id_to_cookie()
        webHTML = requests.get(Variables.URL_ACCOUNTFEE.format(nam = year, hocky = semester, hoche = 1 if (studyAtSummer) else 0), headers=headers)
        soup = BeautifulSoup(webHTML.content, 'lxml')
        # Find all subjects fees
        feeTable = soup.find('table', {'id': 'THocPhi_GridInfo'})
        feeRow = feeTable.find_all('tr', {'class': 'GridRow'})  # type: ignore
        for i in range (0, len(feeRow) - 1, 1):
            cell = feeRow[i].find_all('td', {'class':'GridCell'})
            item = {}
            item['id'] = cell[1].text
            item['name'] = cell[2].text
            item['credit'] = float(cell[3].text)  # type: ignore
            item['is_high_quality'] = True if ('GridCheck' in cell[4].attrs.get('class')) else False
            item['price'] = 0 if (cell[5].text == None or len(cell[5].text) == 0) else float(cell[5].text.replace(',', ''))
            item['is_debt'] = True if ('GridCheck' in cell[6].attrs.get('class')) else False
            item['is_restudy'] = True if ('GridCheck' in cell[7].attrs.get('class')) else False
            item['verified_payment_at'] = cell[8].text
            result.append(item)
    except Exception as ex:
        if (Variables.DEBUG_LOG):
            print(ex)
        result = []
    finally:
        return result

def __getStudentID__(soup: BeautifulSoup):
    baseTxt = soup.find('span', {'id': 'Main_lblHoTen'}).text
    return baseTxt[baseTxt.index('(') + 1:baseTxt.index(')')]

def fetch_student_information(session: Session):
    session.ensure_logged_in()

    result = {}
    try:
        headers = CaseInsensitiveDict()
        # headers["Cookie"] = "ASP.NET_SessionId={id};".format(id=session.session_id)
        headers["Cookie"] = session.export_session_id_to_cookie()
        webHTML = requests.get(Variables.URL_ACCOUNTINFORMATION, headers=headers)

        soup = BeautifulSoup(webHTML.content, 'lxml')
        result['name'] = BeautifulSoupUtils.getValueFromBeautifulSoup4(soup, 'input', 'CN_txtHoTen')
        result['date_of_birth'] = BeautifulSoupUtils.getValueFromBeautifulSoup4(soup, 'input', 'CN_txtNgaySinh')
        result['birth_pace'] = BeautifulSoupUtils.getValueFromBeautifulSoup4(soup, 'select', 'CN_cboNoiSinh')
        result['gender'] = BeautifulSoupUtils.getValueFromBeautifulSoup4(soup, 'input', 'CN_txtGioiTinh')
        result['ethnicity'] = BeautifulSoupUtils.getValueFromBeautifulSoup4(soup, 'select', 'CN_cboDanToc')
        result['nationality'] = BeautifulSoupUtils.getValueFromBeautifulSoup4(soup, 'select', 'CN_cboQuocTich')
        result['national_id_card'] = BeautifulSoupUtils.getValueFromBeautifulSoup4(soup, 'input', 'CN_txtSoCMND')
        result['national_id_card_issue_date'] = BeautifulSoupUtils.getValueFromBeautifulSoup4(soup, 'input', 'CN_txtNgayCap')
        result['national_id_card_issue_place'] = BeautifulSoupUtils.getValueFromBeautifulSoup4(soup, 'select', 'CN_cboNoiCap')
        result['citizen_id_card'] = BeautifulSoupUtils.getValueFromBeautifulSoup4(soup, 'input', 'CN_txtSoCCCD')
        result['citizen_id_card_issue_date'] = BeautifulSoupUtils.getValueFromBeautifulSoup4(soup, 'input', 'CN_txtNcCCCD')
        result['religion'] = BeautifulSoupUtils.getValueFromBeautifulSoup4(soup, 'select', 'CN_cboTonGiao')
        result['account_bank_id'] = BeautifulSoupUtils.getValueFromBeautifulSoup4(soup, 'input', 'CN_txtTKNHang')
        result['account_bank_name'] = BeautifulSoupUtils.getValueFromBeautifulSoup4(soup, 'input', 'CN_txtNgHang')
        result['hi_id'] = BeautifulSoupUtils.getValueFromBeautifulSoup4(soup, 'input', 'CN_txtSoBHYT')
        result['hi_expire_date'] = BeautifulSoupUtils.getValueFromBeautifulSoup4(soup, 'input', 'CN_txtHanBHYT')
        result['specialization'] = BeautifulSoupUtils.getValueFromBeautifulSoup4(soup, 'input', 'MainContent_CN_txtNganh')
        result['school_class'] = BeautifulSoupUtils.getValueFromBeautifulSoup4(soup, 'input', 'CN_txtLop')
        result['training_program_plan'] = BeautifulSoupUtils.getValueFromBeautifulSoup4(soup, 'input', 'MainContent_CN_txtCTDT')
        result['training_program_plan_2'] = BeautifulSoupUtils.getValueFromBeautifulSoup4(soup, 'input', 'MainContent_CN_txtCT2')
        result['school_email'] = BeautifulSoupUtils.getValueFromBeautifulSoup4(soup, 'input', 'CN_txtMail1')
        result['personal_email'] = BeautifulSoupUtils.getValueFromBeautifulSoup4(soup, 'input', 'CN_txtMail2')
        result['school_email_init_pass'] = BeautifulSoupUtils.getValueFromBeautifulSoup4(soup, 'input', 'CN_txtMK365')
        result['facebook_url'] = BeautifulSoupUtils.getValueFromBeautifulSoup4(soup, 'input', 'CN_txtFace')
        result['phone_number'] = BeautifulSoupUtils.getValueFromBeautifulSoup4(soup, 'input', 'CN_txtPhone')
        result['address'] = BeautifulSoupUtils.getValueFromBeautifulSoup4(soup, 'input', 'CN_txtCuTru')
        result['address_from'] = BeautifulSoupUtils.getValueFromBeautifulSoup4(soup, 'select', 'CN_cboDCCua')
        result['address_city'] = BeautifulSoupUtils.getValueFromBeautifulSoup4(soup, 'select', 'CN_cboTinhCTru')
        result['address_district'] = BeautifulSoupUtils.getValueFromBeautifulSoup4(soup, 'select', 'CN_cboQuanCTru')
        result['address_sub_district'] = BeautifulSoupUtils.getValueFromBeautifulSoup4(soup, 'select', 'CN_cboPhuongCTru')
        result['student_id'] = __getStudentID__(soup)
    except Exception as ex:
        if (Variables.DEBUG_LOG):
            print(ex)
    finally:
        return result

def __fetch_training_status_summary__(soup: BeautifulSoup):
    result = None
    try:
        t1 = soup.find('table', {'id': 'KQRLGridTH'})
        t1Row = t1.find_all('tr', {'class': 'GridRow'})
        t1Result = {
            'school_year_start': None,
            'school_year_current': None,
            'credit_collected': 0,
            'avg_train_score_4': 0.0,
            'avg_social': 0
        }
        for i in range (0, len(t1Row) - 1, 1):
            cell = t1Row[i].find_all('td', {'class': 'GridCell'})
            cell_len = len(cell)
            if (t1Result['school_year_start'] == None):
                t1Result['school_year_start'] = cell[0].text
                t1Result['school_year_current'] = cell[0].text
            if (StringUtils.is_null_or_empty(cell[cell_len - 1]) and StringUtils.is_null_or_empty(cell[cell_len - 2]) and StringUtils.is_null_or_empty(cell[cell_len - 3])):
                t1Result['school_year_current'] = cell[0].text
                t1Result['credit_collected'] = cell[cell_len - 3].text
                t1Result['avg_train_score_4'] = float(cell[cell_len - 2].text.strip())
                t1Result['avg_social'] = int(cell[cell_len - 1].text.strip())
        result = t1Result  
    except Exception as ex:
        if (Variables.DEBUG_LOG):
            print(ex)
        result = {}
    finally:
        return result
    
def __fetch_training_status_graduate__(soup: BeautifulSoup):
    result = {}
    try:
        result['has_sig_physical_education'] = BeautifulSoupUtils.getIsCheckedFromBeautifulSoup4(soup, 'input', 'KQRL_chkGDTC')
        result['has_sig_national_defense_education'] = BeautifulSoupUtils.getIsCheckedFromBeautifulSoup4(soup, 'input', 'KQRL_chkQP')
        result['has_sig_english'] = BeautifulSoupUtils.getIsCheckedFromBeautifulSoup4(soup, 'input', 'KQRL_chkCCNN')
        result['has_sig_it'] = BeautifulSoupUtils.getIsCheckedFromBeautifulSoup4(soup, 'input', 'KQRL_chkCCTH')
        result['has_qualified_graduate'] = BeautifulSoupUtils.getIsCheckedFromBeautifulSoup4(soup, 'input', 'KQRL_chkCNTN')
        result['rewards_info'] = BeautifulSoupUtils.getValueFromBeautifulSoup4(soup, 'input', 'KQRL_txtKT')
        result['discipline_info'] = BeautifulSoupUtils.getValueFromBeautifulSoup4(soup, 'input', 'KQRL_txtKL')
        result['eligible_graduation_thesis_status'] = BeautifulSoupUtils.getValueFromBeautifulSoup4(soup, 'textarea', 'KQRL_txtInfo')
        result['eligible_graduation_status'] = BeautifulSoupUtils.getValueFromBeautifulSoup4(soup, 'textarea', 'KQRL_txtCNTN')
    except Exception as ex:
        result = {}
        print(ex)
    finally:
        return result

def __fetch_training_status_subject_result__(soup: BeautifulSoup):
    result = []
    try:
        t1 = soup.find('table', {'id': 'KQRLGridKQHT'})
        t1Row = t1.find_all('tr', {'class': 'GridRow'})
        for i in range(len(t1Row) - 1, 0, -1):
            cellData = {}
            cell = t1Row[i].find_all('td', {'class': 'GridCell'})
            cellData['index'] = int(cell[0].text)
            cellData['school_year'] = cell[1].text
            cellData['is_extended_summer'] = True if ('GridCheck' in cell[2].attrs.get('class')) else False
            cellData['id'] = cell[3].text
            cellData['name'] = cell[4].text
            cellData['credit'] = int(cell[5].text)
            cellData['point_formula'] = cell[6].text
            cellData['point_bt'] = float(cell[7].text) if (StringUtils.is_null_or_empty(cell[7].text)) else None
            cellData['point_bv'] = float(cell[8].text) if (StringUtils.is_null_or_empty(cell[8].text)) else None
            cellData['point_cc'] = float(cell[9].text) if (StringUtils.is_null_or_empty(cell[9].text)) else None
            cellData['point_ck'] = float(cell[10].text) if (StringUtils.is_null_or_empty(cell[10].text)) else None
            cellData['point_gk'] = float(cell[11].text) if (StringUtils.is_null_or_empty(cell[11].text)) else None
            cellData['point_qt'] = float(cell[12].text) if (StringUtils.is_null_or_empty(cell[12].text)) else None
            cellData['point_th'] = float(cell[13].text) if (StringUtils.is_null_or_empty(cell[13].text)) else None
            cellData['point_tt'] = float(cell[14].text) if (StringUtils.is_null_or_empty(cell[14].text)) else None
            cellData['result_t10'] = float(cell[15].text) if (StringUtils.is_null_or_empty(cell[15].text)) else None
            cellData['result_t4'] = float(cell[16].text) if (StringUtils.is_null_or_empty(cell[16].text)) else None
            cellData['result_by_char'] = cell[17].text
            result.append(cellData)
    except Exception as ex:
        if (Variables.DEBUG_LOG):
            print(ex)
        result = []
    finally:
        return result
    

def fetch_training_result(session: Session):
    session.ensure_logged_in()

    result = {}
    result['training_summary'] = {}
    result['graduate_status'] = {}
    result['subject_result'] = []
    
    try:
        headers = CaseInsensitiveDict()
        # headers["Cookie"] = "ASP.NET_SessionId={id};".format(id=session.session_id)
        headers["Cookie"] = session.export_session_id_to_cookie()
        webHTML = requests.get(Variables.URL_ACCOUNTTRAININGSTATUS, headers=headers)
        soup = BeautifulSoup(webHTML.content, 'lxml')
        
        result['training_summary'] = __fetch_training_status_summary__(soup)
        result['graduate_status'] = __fetch_training_status_graduate__(soup)
        result['subject_result'] = __fetch_training_status_subject_result__(soup)
    except Exception as ex:
        if (Variables.DEBUG_LOG):
            print(ex)
        result['training_summary'] = {}
        result['graduate_status'] = {}
        result['subject_result'] = []
    finally:
        return result