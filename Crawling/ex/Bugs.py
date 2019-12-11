from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup

url = 'https://music.bugs.co.kr/'

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome('chromedriver', options=chrome_options)
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'lxml')
mydata = soup.select('th > p > a')
print(mydata)
mynum = soup.select('tbody > td.ranking')

for i in mydata:
    print(i.attrs['title'])
    #어떠한 클래스가아닌 단어? 구분자를 사용할때는 attrs['']를 사용하면 가능하다
