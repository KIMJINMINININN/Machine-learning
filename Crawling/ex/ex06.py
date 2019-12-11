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
items = soup.select('#mArticle > div.cmain_tmp > div.section_media > div.hotissue_builtin > div.realtime_part > ol > li')
print(items)
for item in items:
    title = item.find('span', class_='ir_wa').text
    descrpition = item.find('span', attrs={"class" : "txt_issue"}).text
    print("t:" +title)
    print("d:" +descrpition)
# 검색어 입력
# element.send_keys('테스트 검색')
# # 검색
# element.submit()
# # 스크린샷 저장1
# browser.save_screenshot("c:/website_ch2.png")
# # 스크린샷 저장2
# browser.get_screenshot_as_file("c:/website_ch2.png")
# # 브라우저 종료


