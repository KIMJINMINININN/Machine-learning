from selenium import webdriver
from selenium.webdriver.common.keys import Keys

usr = "아이디"
pwd = "패스워드"

path = "./chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("http://www.facebook.org")

'''
assert "Facebook" in driver.title
elem = driver.find_element_by_id("email")
elem.send_keys(usr)
elem = driver.find_element_by_id("pass")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)
'''