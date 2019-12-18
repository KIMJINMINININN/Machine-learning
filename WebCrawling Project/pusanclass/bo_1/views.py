from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.db import connection
from base64 import b64encode
from django.core.paginator import Paginator
from .models import B_list
from PIL import Image
import base64

def list(request):
    if request.method == 'GET':
        #DB에서 데이터 들고오기
        a = B_list.objects.all().order_by('-id_no')
        page = request.GET.get('page')
        #keyword로 Search하기 
        searchtype = request.GET.get('type','') #종류
        searchkeyword = request.GET.get('text','') #키워드
        if searchtype == 'title':
            a = B_list.objects.filter(title__icontains=searchkeyword)
        elif searchtype == 'ellipsis_area':
            a = B_list.objects.filter(ellipsis_area__icontains=searchkeyword)    
        elif searchtype == 'opentime':
            a = B_list.objects.filter(opentime__icontains=searchkeyword)
        elif searchtype == 'addressroad':
            a = B_list.objects.filter(addressroad__icontains=searchkeyword)
        
        rows = a.values()
        posts =[]          
        for i in rows:
            if i['image'] :
                img = i['image']                      #(  )
                image = b64encode(img).decode("utf-8")    
            else :
                file = open("./static/image/aa.jpg","rb") #이미지 없을때 대체방법 
                data =file.read()
                image = b64encode(data).decode("utf-8")
            dic = {'id_no':'','title':'','number':'','addressroad':'','opentime':'','pageaddress':'','info':'','ellipsis_area':'','image':''}
            dic['id_no']         = i['id_no']
            dic['title']         = i['title']
            dic['number']        = i['number']
            dic['addressroad']   = i['addressroad']
            dic['opentime']      = i['opentime']
            dic['pageaddress']   = i['pageaddress']
            dic['info']          = i['info']
            dic['ellipsis_area'] = i['ellipsis_area']
            dic['image']         = image
            posts.append(dic)   
        page = request.GET.get('page')
        p = Paginator(posts, 8)
        posts = p.get_page(page)
        total = posts.index
        b = []
        for a in range(1, p.num_pages+1, 1):
            b.append(a)
    return render(request, "bo_1/list.html",{'posts':posts, 'total': total, 'b':b , 'searchtype':searchtype, 'searchkeyword':searchkeyword})

# def list_ca(request):
#     if request.method == 'GET':
#         a = B_list.objects.all().order_by('-id_no')
#         road = request.GET.get('addressroad',0)
#         if road == '해운대구':
#             a = B_list.objects.filter(addressroad__icontains=road)
#         rows = a.values()

#         page = request.GET.get('page',1)
#         p = Paginator(rows, 10)
#         posts = p.get_page(page)
#         for i in rows:
#             if i['image'] :                      #(  )
#                 data = i['image'].read()     #이미지 파일
#                 image = b64encode(data).decode("utf-8")
#             else :
#                 file = open("./static/image/aa.jpg","rb") #이미지 없을때 대체방법 
#                 data =file.read()
#                 image =b64encode(data).decode("utf-8")
#     return render(request, "bo_1/list_ca.html",{'image':image, 'data':rows, 'posts':posts})


def list_c(request):
    no = [request.GET['no']]
    cursor = connection.cursor()
    sql= "SELECT * FROM bo_1_B_list WHERE id_no = %s"
    cursor.execute(sql, no)       #SQL문 수행
    rows =cursor.fetchone()         # 결과값받기    
    #이미지 로드
    if rows[9] :                      #(  )
        data = rows[9]     #이미지 파일
        image = b64encode(data).decode("utf-8")    
    else :
        file = open("./static/image/aa.jpg","rb") #이미지 없을때 대체방법 
        data =file.read()
        image =b64encode(data).decode("utf-8")
    dic = {'id_no':'','title':'','number':'','addressroad':'','opentime':'','pageaddress':'','info':'','ellipsis_area':'','image':''}
    dic['id_no']         = rows[0]
    dic['title']         = rows[1]
    dic['number']        = rows[2]
    dic['addressroad']   = rows[3]
    dic['opentime']      = rows[5]
    dic['pageaddress']   = rows[6]
    dic['info']          = rows[7]
    dic['ellipsis_area'] = rows[8]
    dic['image']         = image
    # return render(request, 'bo_1/list_c.html', {'data': row, 'image':image})
    return render(request, 'bo_1/list_c.html', {'data': dic})

##################################################################################
from bs4 import BeautifulSoup
from selenium import webdriver
import time,requests,urllib
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By




def Selenium(request):
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
    return render(request,'home/index.html')


def craw(loca,driver):
    # loca = driver.find_element_by_class_name('list_place_col1')

    li = loca.find_elements_by_tag_name('li')
    label_1 = {'title':'','number':'','addressroad':'','addressgi':'','opentime':'','pageaddress':'','info':'','ellipsis_area':''}
    labellist = []
    label = []
    # image=[]
    labelid = ""
    for i,e in enumerate(li):
    # for i in range(1, 6, 1):
        title=" "
        number=" "
        addressroad =" "
        addressgi = " "
        opentime= " "
        pageaddress= " "
        info=" "
        ellipsis_area=" "
        a = li[i].find_element_by_tag_name('a')
        url1 = a.get_attribute("src")
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
            if '사진요약' in label:
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
                try:
                    img1 = imgsrc[0].select('img')
                except:
                    img1 = None
                if img1 is not None:
                    imgurl = img1[0].attrs['src']
                    img10 = urllib.request.urlopen(imgurl).read()
                else:
                    pass
                
                # image_64_encode = base64.encodebytes(img10)
                # urllib.request.urlretrieve(imgurl, './img/'+title+'.jpg')
               
            else: 
                imgsrc = bs.select('#'+controls+'> div > div > div.view_area > div.select_photo_area > div.list_photo > div > div:nth-child(1) > div > div')                                
                # print(imgsrc)
                try:
                    img1 = imgsrc[0].select('img')
                except:
                    img1 = None
                if img1 is not None:
                    imgurl = img1[0].attrs['src']
                    img10 = urllib.request.urlopen(imgurl).read()
                else:
                    pass
                
            print(img10)
            print(type(img10))
                # image_64_encode = base64.encodebytes(img10)
                # urllib.request.urlretrieve(imgurl, './img/'+title+'.jpg')
        else:
            pass

        label_1 = {'title':'','number':'','addressroad':'','addressgi':'','opentime':'','pageaddress':'','info':'','ellipsis_area':'','image':''}
        label_1['title']         = title
        label_1['number']        =number 
        label_1['addressroad']   = addressroad
        label_1['addressgi']     = addressgi
        label_1['opentime']      = opentime
        label_1['pageaddress']   = pageaddress
        label_1['info']          = info
        label_1['ellipsis_area'] = ellipsis_area
        label_1['image']         = img10
        # image.append(img10)
        labellist.append(label_1)  
        
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
    for i in labellist:
        ti       = i['title']
        nu       = i['number']
        adroad   = i['addressroad']
        adgi     = i['addressgi']
        opentime = i['opentime']
        pagead   = i['pageaddress']
        info     = i['info']
        area     = i['ellipsis_area']
        image    = i['image']
        
        # al = [ti, nu, adroad, adgi, opentime, pagead, info, area, image.read()]
        # cursor = connection.cursor()
        # sql = 'INSERT INTO bo_1_b_list SET title= 'ti', number='nu', addressroad= 'adroad', addressgi='adgi', opentime='opentime', pageaddress='pagead', info='info', ellipsis_area= 'area' '
           
        all = B_list(title= ti, number=nu, addressroad= adroad, addressgi=adgi, opentime=opentime, pageaddress=pagead, info=info, ellipsis_area= area, image=image)
        all.save()
    # for a in image:    
    #     cursor = connection.cursor()
    #     sql= f"INSERT INTO bo_1_B_list SET image={a}"
    #     cursor.execute(sql)
    # # INSERT INTO web_site SET name='뉴스타파';
    # INSERT INTO 테이블명(컬럼명) VALUES(내용들);
    # label_1['image']         = img10
    # image    = i['image']
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
# Selenium()