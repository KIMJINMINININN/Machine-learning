import requests
from bs4 import BeautifulSoup
serviceKey = "2vTBhKfL%2BdsMkdn7fEQMVdn%2FpsJpAtFs8%2FBz%2BWz6WS4mIT%2FEAIvbd%2FK%2BusR7lzUPaE%2B5NBpetw%2FkOAI0YzmJWQ%3D%3D"
open_api = 'http://apis.data.go.kr/B553077/api/open/sdsc/storeListInDong?divId=ctprvnCd&key=11&ServiceKey='+serviceKey

res = requests.get(open_api)
print(res.text)
soup = BeautifulSoup(res.content, 'html.parser')
data = soup.find_all('item')
for item in data:
    bizeId = item.find('bizesid')
    bizeNm = item.find('bizesnm')
    print (bizeId.get_text(), bizeNm.get_text())

