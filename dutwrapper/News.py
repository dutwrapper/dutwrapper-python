
from bs4 import BeautifulSoup, ResultSet
import enum
import requests

# Import configured variables
import dutwrapper.__Variables__ as Variables
from dutwrapper import Utils

class NewsType(enum.Enum):
    Global = 0
    Subject = 1
    StudentAffairs = 2
    Examination = 3
    TuitionFee = 4
    StatuteRegulation = 5

def __get_newstype_data__(newsType: NewsType) -> dict:
    if (newsType == NewsType.Global):
        return {
            'type': 'Global',
            'news_obj_value': 'global',
            'url_value': 'CTRTBSV',
            'tab': 0,
        }
    elif (newsType == NewsType.Subject):
        return {
            'type': 'Subject',
            'news_obj_value': 'subject',
            'url_value': 'CTRTBGV',
            'tab': 1,
        }
    elif (newsType == NewsType.StudentAffairs):
        return {
            'type': 'Student Affairs',
            'news_obj_value': 'student_affairs',
            'url_value': 'CTRTBSV',
            'tab': 2,
        }
    elif (newsType == NewsType.Examination):
        return {
            'type': 'Examination',
            'news_obj_value': 'examination',
            'url_value': 'CTRTBSV',
            'tab': 3,
        }
    elif (newsType == NewsType.TuitionFee):
        return {
            'type': 'Tuition Fee',
            'news_obj_value': 'tuition_fee',
            'url_value': 'CTRTBSV',
            'tab': 4,
        }
    elif (newsType == NewsType.StatuteRegulation):
        return {
            'type': 'Statute and Regulation',
            'news_obj_value': 'statute_regulation',
            'url_value': 'CTRTBSV',
            'tab': 5,
        }
    else:
        return {}

# Get news from sv.dut.udn.vn with page you selected.
def get_news(newsType: NewsType = NewsType.Global, page: int = 1):
    """
    Get news from sv.dut.udn.vn.
    For latest news, leave 'page' to default.
    type (NewsType): Type of news want to load.
    page (int): News page. If less than 1, will be reset to 1.
    """

    def __findList__(txt: str, lst: ResultSet):
        index: int = 0
        try:
            for item in lst:
                if txt == item.text:
                    break
                else:
                    index += 1
            if index >= len(lst):
                raise Exception()
        except Exception as ex:
            if (Variables.DEBUG_LOG):
                print(ex)
            index = -1
        return index
    
    def __getLinks__(src: ResultSet):
        result = []
        # Temporary variables here
        linkResultSet = src.find_all(name='a') # type: ignore
        textLength = 0
        navStringResultSet = src.find_all(text=True) # type: ignore
        for node in navStringResultSet:
            index = __findList__(node, linkResultSet)
            if (index > -1):
                item = {}
                item['text'] = linkResultSet[index].text
                item['content'] = linkResultSet[index].attrs['href'] if 'href' in linkResultSet[index].attrs.keys() else None
                item['type'] = 'link'
                item['position'] = textLength
                result.append(item)
                linkResultSet.pop(index)
            d1 = len(node.text)
            textLength += d1
        return result

    # Prepare a result data    
    jsonReturn = []
    type: dict = __get_newstype_data__(newsType=newsType)
    if (page < 1):
        page = 1
    try:
        # Get elements from sv.dut.dut.vn
        webHTML = requests.get(Variables.URL_NEWS.format(
            news=type['url_value'],
            page=page,
            tab=type['tab']
        ))
        # Convert to BeautifulSoup
        soup = BeautifulSoup(webHTML.content, 'lxml')
        # Find all element groups in html.
        news = soup.find_all('div', {'class': 'tbBox'})
        for i in range(0, len(news), 1):
            # Get news date and title
            webElement = news[i].find('div', class_='tbBoxCaption')
            dateText = webElement.find_all('span')[0].text.replace(':', '')
            dateTextSplit = dateText.split('/')
            date = Utils.DateTimeUtils.FromUTC(int(dateTextSplit[2]), int(dateTextSplit[1]), int(dateTextSplit[0]))
            title = webElement.find_all('span')[1].text
            # Get news content
            content = news[i].find('div', class_='tbBoxContent')
            # Add to jsonReturn
            jsonReturn.append({
                'news_type': type['news_obj_value'],
                'title': title,
                'content_html': content.encode_contents().decode('utf-8'),
                'content': content.text,
                'date_published': date,
                'date_fetched': Utils.DateTimeUtils.CurrentTimeAsUnix(),
                'resources': __getLinks__(content)
            })
    except Exception as ex:
        # If something went wrong, delete all items in news list.
        if (Variables.DEBUG_LOG):
            print(ex)
        jsonReturn.clear()
        jsonReturn = []
    finally:
        # Return result
        return jsonReturn
