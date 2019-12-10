from selenium import webdriver

browser = webdriver.Chrome('./chromedriver.exe')

#5초동안 대기
browser.implicitly_wait(5)

# print(dir(browser))

browser.set_window_size(1920, 1280)# 최대, 최소

browser.get('https://www.daum.net')
# Page 내용 확인
print('Page Contents : {}'.format(browser.page_source))
# Session 정보 확인
print('Session ID : {}'.format(browser.session_id))
# Title 정보 확인
print('Title : {}'.format(browser.title))
# URL 정보 확인
print('URL : {}'.format(browser.current_url))
# 쿠키 정보 확인
print('Cookies : {}'.format(browser.get_cookies))
# 검색창 input 선택
element = browser.find_element_by_css_selector('div.inner_search > input.tf_keyword')
# 검색어 입력
element.send_keys('테스트 검색')
# 검색
element.submit()
# 스크린샷 저장1
browser.save_screenshot("c:/website_ch2.png")
# 스크린샷 저장2
browser.get_screenshot_as_file("c:/website_ch2.png")
# 브라우저 종료
browser.quit()


