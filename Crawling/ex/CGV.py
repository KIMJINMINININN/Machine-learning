from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup

url = 'https://www.daum.net/'

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome('chromedriver', options=chrome_options)
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'lxml')
mydata = soup.select('#contents > div.wrap-movie-chart > div.sect-movie-chart')
print(mydata)