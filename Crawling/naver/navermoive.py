import requests
from bs4 import BeautifulSoup

## HTTP GET Request
req = requests.get('https://movie.naver.com/movie/point/af/list.nhn')

html = req.text
soup = BeautifulSoup(html, 'html.parser')
mydata = soup.find_all('tbody')
for i in mydata:
    i.find_all('')
print(mydata)
# mydata2=mydata[0]
# print(mydata)
# tp=mydata2.find_all('span','title')
# for a in tp:
#     print(a.text)

# mydata = soup.find_all('ul','ah_1').children