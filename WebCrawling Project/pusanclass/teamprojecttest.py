from bs4 import BeautifulSoup
from selenium import webdriver
import time,requests,urllib
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

def Selenium():
    count=0
    driver = webdriver.Chrome('./chromedriver.exe')
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
            for a in range(0,5): #0~4 0,5
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
            for a in range(0,5):#0~4 0,5
                    switchnum1[a].click()
                    time.sleep(1)
                    craw(loca,driver)
                    time.sleep(3)
            switcharrow[0].click()
            time.sleep(5)
# print(label)
#         print(labellist)
#         print(title)
#         print(number)
#         print(addressroad)
#         print(addressgi)
#         print(opentime)
#         print(pageaddress)
#         print(info)
#         print(ellipsis_area)

def craw(loca,driver):
    # loca = driver.find_element_by_class_name('list_place_col1')
    li = loca.find_elements_by_tag_name('li')
    label = {'title':'','number':'','addressroad':'','addressgi':'','opentime':'','pageaddress':'','info':'','ellipsis_area':''}
    labellist = []
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
        time.sleep(1)

        last_tab = driver.window_handles[-1]
        driver.switch_to.window(window_name=last_tab)
        source = driver.page_source
        bs=BeautifulSoup(source,'html.parser')
        '''
        if(bs.find('div','biz_name_area').find('strong','name')):
            title = bs.find('div','biz_name_area').find('strong','name').text
        else:
            pass
        test = bs.select('#tabs')
        for i in test[0]:
            label = i.get('aria-label')
            if '사진요약' in label:
                labelid = i.get('id')
        labeldr = driver.find_elements_by_id(labelid)
        labeldr[0].click()
        time.sleep(3) 
        img = labeldr[0].find_elements_by_xpath('//*[@id="panel04"]/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div')
        img[0].screenshot(title+str(i)+".png")
        # test1 = test[0].get('aria-controls')
        '''
        
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
        if(bs.find('div', 'ellipsis_area')):
            if(driver.find_elements_by_class_name('btn_more')):
                bn = driver.find_elements_by_class_name('btn_more')
                bn[0].click()
                time.sleep(2)
                source = driver.page_source
                bs=BeautifulSoup(source,'html.parser')
                ellipsis_area = bs.find('div', 'ellipsis_area').text
            else:
                pass
        else:
            pass
        # print(btn_more1)
        label = {'title':'','number':'','addressroad':'','addressgi':'','opentime':'','pageaddress':'','info':'','ellipsis_area':''}
        label['title'] = title
        label['number'] =number 
        label['addressroad'] = addressroad
        label['addressgi'] = addressgi
        label['opentime']= opentime
        label['pageaddress'] = pageaddress
        label['info'] = info
        label['ellipsis_area'] = ellipsis_area
        labellist.append(label)
        
        print(labellist)
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
    print(labellist)
    # for i in labellist:
    #     ti = i['title']
    #     nu = i['number']
    #     adroad =i['addressroad']
    #     adgi = i['addressgi']
    #     opentime = i['opentime']
    #     pagead = i['pageaddress']
    #     info = i['info']
    #     area = i['ellipsis_area']
        # al = [ti, nu, adroad, adgi, opentime, pagead, info, area]
        # cursor = connection.cursor()
        # sql = 'INSERT INTO bo_1_b_list SET title= 'ti', number='nu', addressroad= 'adroad', addressgi='adgi', opentime='opentime', pageaddress='pagead', info='info', ellipsis_area= 'area' '
           
        # all = B_list(title= ti, number=nu, addressroad= adroad, addressgi=adgi, opentime=opentime, pageaddress=pagead, info=info, ellipsis_area= area )
        # all.save()


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
