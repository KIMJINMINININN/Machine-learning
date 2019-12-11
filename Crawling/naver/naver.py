import requests
from bs4 import BeautifulSoup
import time
## HTTP GET Request
req = requests.get('https://www.naver.com/')

html = req.text
soup = BeautifulSoup(html, 'html.parser')
'''
mydata = soup.find_all('ul','ah_l')
mydata2=mydata[0]
tt = mydata2.find_all('span','ah_r')
print(tt)
tp=mydata2.find_all('span','ah_k')
for a in tp:
    print(a.text)
    #find_all을 사용한방법
'''

mydata1 = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_list.PM_CL_realtimeKeyword_list_base > ul:nth-child(5)> li')
#copy selector
for li in mydata1:
    title = li.find("span", attrs={"ah_k"}).text
    print(title)

# select를 사용한방법



def time_function(f):
    def wrapper(*args, **kawrgs):
        start_time = time.time()
        result = f(*args, **kawrgs)
        end_time = time.time() - start_time
        print("{} {} time: {}".format(f.__name__, args[1], end_time))
        return result
    return wrapper
#시간을 재는 함수

@time_function
def r_selector(url,parser):
    r = requests.get(url)
    bs = BeautifulSoup(r.text, parser)
    # 뷰티풉숩의 select 함수 사용
    # li 태그의 클래스명이 ah_item인 요소 하위의 span 태그이며 클래스명이 ah_k 인 요소선택
    lists = bs.select("#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_list.PM_CL_realtimeKeyword_list_base > ul:nth-child(5)> li")
    for li in lists:
        print(li.text)

#r_selector("http://www.naver.com", "html5lib")
#r_selector("http://www.naver.com", "html.parser")
#r_selector("http://www.naver.com", "lxml")