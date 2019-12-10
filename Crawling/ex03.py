from selenium import webdriver
from bs4 import BeautifulSoup

url = 'https://pjt3591oo.github.io'

driver = webdriver.Chrome('chromedriver')
driver.get(url)

soup = BeautifulSoup(driver.page_source)
print(soup.select('div'))