from bs4 import BeautifulSoup
from selenium import webdriver
import time,requests,urllib
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

def Selenium():
    count=0
    # html
    # chrome_options = Options()
    # chrome_options.add_argument("--headless")
    driver = webdriver.Chrome('./chromedriver.exe')
    # driver = webdriver.Chrome('./chromedriver.exe',options=chrome_options)

    driver.get('https://www.naver.com/')
    elem = driver.find_element_by_name("query")
    elem.send_keys("부산공방")
    elem.submit()
    time.sleep(1)
    last_tab = driver.window_handles[-1]
    driver.switch_to.window(window_name=last_tab)
    gongbang = driver.find_element_by_class_name("go_more")
    gongbang.click()
    time.sleep(2)
    last_tab1 = driver.window_handles[-1]
    driver.switch_to.window(window_name=last_tab1)
    #페이지 들어와서 list 받는것 시작
    #페이지, 화살표부분
    switchnum = driver.find_elements_by_class_name('pagination_inner')
    switcharrow = switchnum[0].find_elements_by_class_name('btn_next')
    # switcharrow[0].click()
    switchnum1 = switchnum[0].find_elements_by_class_name('num') #숫자 넘기기
    while(True):
        classtext = switcharrow[0].get_attribute('class')
        if 'disable' in classtext:
            loca = driver.find_element_by_class_name('list_place_col1')
            for a in range(4,5): #0~4 0,5
                print('test입니다')
                switchnum1[a].click()
                time.sleep(2)
                craw(loca,driver)
                time.sleep(2)
                if a == 4:
                    count = a
            if count == 4:
                print("------끝났씁니다------")
                break
            #->가 없다
            #page가 끝나고 break
        else:
        #->가있다
        #page가 끝나고 click
            loca = driver.find_element_by_class_name('list_place_col1')
            for a in range(4,5):#0~4 0,5
                    switchnum1[a].click()
                    time.sleep(3)
                    craw(loca,driver)
                    time.sleep(3)
            switcharrow[0].click()
            time.sleep(5)

def craw(loca,driver):
    # driver = webdriver.Chrome('./chromedriver.exe')
    # driver.get('https://store.naver.com/attractions/detail?id=1384863408&query=%EB%B2%A0%EB%A6%B0%EB%94%94%EA%B3%B5%EB%B0%A9')
    # loca = driver.find_element_by_class_name('list_place_col1')
    li = loca.find_elements_by_tag_name('li')
    label = []
    labelid = ""
    for i,e in enumerate(li):
        title=" "
        number=" "
        addressroad =" "
        addressgi = " "
        opentime= " "
        pageaddress= " "
        info=" "
        ellipsis_area=" "
        a = li[i].find_element_by_tag_name('a')
        a.click()
        time.sleep(2)

        last_tab = driver.window_handles[-1]
        driver.switch_to.window(window_name=last_tab)
        source = driver.page_source
        bs=BeautifulSoup(source,'html.parser')
        time.sleep(2)
        if(bs.find('div','biz_name_area').find('strong','name')):
            title = bs.find('div','biz_name_area').find('strong','name').text
        else:
            pass
        # img2 = img1[0].get_attribute('src')
        # img = labeldr[0].find_elements_by_xpath('//*[@id="panel04"]/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div/img')
        # print(labeldr[0].get(img[0].get_attribute('img')))
        
        

        # img[0].screenshot(title+str(i)+".png")
        # test1 = test[0].get('aria-controls')
        entire = bs.find('div', class_='bizinfo_area')
        number = entire.find('div', class_='txt').text
        if(entire.find('ul', class_='list_address')):
            address = entire.find('ul', class_='list_address').find_all('li')
            adlen = len(address)
        else:
            pass
        # print(address[0].text)
        if(adlen == 2):
            if(address[0]):
                addressroad = address[0].text
            elif(address[1]):
                addressgi = address[1].text
            else:
                pass
        elif(adlen == 1):
            if(address[0]):
                addressroad = address[0].text
                addressgi = address[0].text
        else:
            pass

        # if(address.find('span', class_='addr')):
        #     addressgi = address.find('span', class_='addr').text
        # else:
        #     pass
        if(entire.find('div', class_='biztime')):
            opentime = entire.find('div', class_='biztime').text
        else:
            pass
        if(entire.find('a', class_='biz_url')):
            pageaddress = entire.find('a', class_='biz_url').text
        else:
            pass
        if(entire.find('div', 'convenience')):
            info = entire.find('div', 'convenience').text
        else: 
            pass
        # if(bs.find('div', 'ellipsis_area')):
        #     try:
        #     ea = driver.find_elements_by_class_name('ellipsis_area')
        #     if(ea[0].find_elements_by_class_name('btn_more')):
        #         bn = ea[0].find_elements_by_class_name('btn_more')
        #         print(bn)
        #         print(bn[0])
        #         bn[0].click()
        #         time.sleep(4)
        #         source = driver.page_source
        #         bs=BeautifulSoup(source,'html.parser')
        #         ellipsis_area = bs.find('div', 'ellipsis_area').text
        #     else:
        #         pass
        #     Exception:
        #         ellipsis_area = "error ?????"
        # else:
        #     pass
        if(bs.find('div', 'ellipsis_area')):
            ea = driver.find_elements_by_class_name('ellipsis_area')
            if(ea[0].find_elements_by_class_name('btn_more')):
                element = ea[0].find_element_by_class_name('btn_more')
                driver.execute_script("arguments[0].click();", element)
                time.sleep(4)
                source = driver.page_source
                bs=BeautifulSoup(source,'html.parser')
                ellipsis_area = bs.find('div', 'ellipsis_area').text
            else:
                pass
        else:
            pass
        test = bs.select('#tabs')
        for i in test[0]:
            label = i.get('aria-label')
            controls = i.get('aria-controls')
            if '사진요약' in label:#labelid=""
                labelid = i.get('id')
            else:
                pass
        if driver.find_elements_by_id(labelid):
            labeldr = driver.find_elements_by_id(labelid)
            # print(labeldr)
            # labeldr[0].click()
            # topics_xpath = driver.find_element_by_xpath('//*[@id='+labelid+'"]"')
            # element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, labeldr)))
            element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, labelid)))
            element.click()
            time.sleep(3)
            source = driver.page_source
            bs=BeautifulSoup(source,'html.parser')
            if len(bs.select('#'+controls+'> div > div > div.view_area > div.select_photo_area > div.list_photo > div > div:nth-child(1) > div > div')) == 0:
                imgsrc = bs.select('#'+controls+'> div > div > div.view_area > div.select_photo_area > div.list_photo > div > div:nth-child(1) > a > div')
                #panel02 > div > div > div.view_area > div.select_photo_area > div.list_photo > div > div:nth-child(1) > a > div                           
                # print(imgsrc)
                print(len(imgsrc))
                # if len(imgsrc) == 1:
                try:
                    img1 = imgsrc[0].select('img')
                except:
                    img1 = None
                if img1 is not None:
                    imgurl = img1[0].attrs['src']
                    img10 = urllib.request.urlopen(imgurl).read()
                else:
                    pass
                # urllib.request.urlretrieve(imgurl, './img/'+title+'.jpg')
            else: 
                imgsrc = bs.select('#'+controls+'> div > div > div.view_area > div.select_photo_area > div.list_photo > div > div:nth-child(1) > div > div')                                
                # print(imgsrc)
                print(len(imgsrc))
                try:
                    img1 = imgsrc[0].select('img')
                except:
                    img1 = None
                if img1 is not None:
                    imgurl = img1[0].attrs['src']
                    img10 = urllib.request.urlopen(imgurl).read()
                else:
                    pass
                # urllib.request.urlretrieve(imgurl, './img/'+title+'.jpg')
        else:
            pass
        # print(btn_more1)

        print(title)
        print(number)
        print(addressroad)
        print(addressgi)
        print(opentime)
        print(pageaddress)
        print(info)
        print(ellipsis_area)
        driver.close()
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(1)
# 로딩 기다리기

    # urlblog = ' '
    # urlgram = ' '
    # if(entire.find('ul', 'list_homepage')):
    #     urltag = entire.find('ul', 'list_homepage')
    #     url1 = urltag.find_all('li')
    #     urlsize = len(url1)
    #     if(urlsize == '1'):
    #         if(url1[0].find('a').text == '블로그'):
    #             urlblog = url1[0].find('a').get('href')
    #         else:
    #             urlgram = url1[0].find('a').get('href')
    #     else:
    #         pass
    # else:
    #     pass
    # urltag = entire.find('ul', 'list_homepage')
    # url1 = urltag.find_all('li')
    # urlblog = url1[0].find('a').get('href')
    # urlgram = url1[1].find('a').get('href')

    # print(urlblog)
    # print(urlgram)

Selenium()
# craw()