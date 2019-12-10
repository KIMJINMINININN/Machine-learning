from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup

url = 'https://store.naver.com/attractions/list?query=%EA%B3%B5%EB%B0%A9&region=%EB%B6%80%EC%82%B0%EA%B4%91%EC%97%AD%EC%8B%9C&sessionid=k7c5powyTDiE4qpnwDaWxg%3D%3D&sortingOrder=precision'

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome('chromedriver', options=chrome_options)
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'lxml')
items = soup.select('#container > div.placemap_area > div.list_wrapper > div > div.list_area > ul > li > div.list_item_inner ')
# print(items)
for item in items:
    title = item.find('a', class_='name').text
    titlemake = title[2:]
    explain = item.find('div', class_='txt ellp').text
    print(explain)
#     descrpition = item.find('span', attrs={"class" : "txt_issue"}).text
    # print("t:" +title)
#     print("d:" +descrpition)
# 검색어 입력
# element.send_keys('테스트 검색')
# # 검색
# element.submit()
# # 스크린샷 저장1
# browser.save_screenshot("c:/website_ch2.png")
# # 스크린샷 저장2
# browser.get_screenshot_as_file("c:/website_ch2.png")
# # 브라우저 종료


