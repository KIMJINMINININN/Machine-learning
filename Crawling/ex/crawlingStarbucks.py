from bs4 import BeautifulSoup
from selenium import webdriver
import time,requests

driver = webdriver.Chrome('./chromedriver.exe')
driver.get('https://www.istarbucks.co.kr/store/store_map.do')
time.sleep(3)

loca = driver.find_element_by_class_name('loca_search')
loca.click()
time.sleep(1)

sido = driver.find_element_by_class_name('sido_arae_box')
li = sido.find_elements_by_tag_name('li')
li[5].click()
time.sleep(1)

sido = driver.find_element_by_class_name('gugun_arae_box')
li = sido.find_elements_by_tag_name('li')
li[-1].click()
time.sleep(1)

source = driver.page_source
#selenium으로 들어간 나의 목표 페이지의 source를 입력
bs=BeautifulSoup(source,'lxml')
#source 긁어오기
entire = bs.find('ul', class_='quickSearchResultBoxSidoGugun')

li_list = entire.find_all('li')

for li in li_list:
    print(li.find('p').text)
driver.close()
