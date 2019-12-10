import requests
from bs4 import BeautifulSoup

## HTTP GET Request
req = requests.get('https://datalab.naver.com/')

html = req.text
soup = BeautifulSoup(html, 'html.parser')
mydata = soup.select('#content > div.spot.section_keyword > div.home_section.active > div > div.keyword_carousel > div > div > div:nth-child(1) > div')
mydata2=mydata[0]
# print(mydata)
tp=mydata2.find_all('span','title')
for a in tp:
    print(a.text)

# mydata = soup.find_all('ul','ah_1').children
# mydata1 = mydata.find_all('li','ah_item')
# print(mydata1)