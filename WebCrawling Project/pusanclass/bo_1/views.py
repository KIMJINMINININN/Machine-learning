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

#Selenium 시작 함수
def Selenium(request):
    count=0
    driver = webdriver.Chrome('./chromedriver.exe')
    driver.get('https://www.naver.com/')
    #naver driver의 내용을 가져온다
    elem = driver.find_element_by_name("query")
    elem.send_keys("부산공방")
    #부산공방이라고 네이버 검색창에 입력
    elem.submit()
    time.sleep(1)
    last_tab = driver.window_handles[-1]
    driver.switch_to.window(window_name=last_tab)
    #last_tab에 가장 최근에 열린 탭에 handles를 입력
    gongbang = driver.find_element_by_class_name("go_more")
    gongbang.click()
    #더보기 클릭
    time.sleep(2)
    last_tab1 = driver.window_handles[-1]
    driver.switch_to.window(window_name=last_tab1)
    #페이지 들어와서 list 받는것 시작
    #페이지, 화살표부분
    switchnum = driver.find_elements_by_class_name('pagination_inner')
    switcharrow = switchnum[0].find_elements_by_class_name('btn_next')#화살표 부분
    switchnum1 = switchnum[0].find_elements_by_class_name('num') #숫자 넘기기
    while(True):
        classtext = switcharrow[0].get_attribute('class') #화살표부분 클래스의 이름을 받아와서
        if 'disable' in classtext:#만약 disable이라면 화살표를 사용할수없다면
            loca = driver.find_element_by_class_name('list_place_col1')
            for a in range(0,5):
                print('test입니다')
                #다음번호를 클릭
                switchnum1[a].click()
                time.sleep(2)
                craw(loca,driver)
                #list에서 크롤링을 시작 하는 부분
                time.sleep(2)
                if a == 4:
                    count = a
            if count == 4:
                print("------끝났씁니다------")
                break
            #->가 없다
            #page가 끝나고 break
        else:
        #클래스 이름을 받아와서 화살표를 사용할수있다면
        #->가있다
        #page가 끝나고 click
            loca = driver.find_element_by_class_name('list_place_col1')
            for a in range(0,5):#0~4 0,5
                    #다음번호를 클릭
                    switchnum1[a].click()
                    time.sleep(1)
                    craw(loca,driver)
                    #list에서 크롤링을 시작 하는 부분
                    time.sleep(3)
            switcharrow[0].click()
            #화살표 클릭
            time.sleep(5)
    return render(request,'home/index.html')


def craw(loca,driver):
    li = loca.find_elements_by_tag_name('li')
    #공방 리스트에 대해서 가져오기
    label_1 = {'title':'','number':'','addressroad':'','addressgi':'','opentime':'','pageaddress':'','info':'','ellipsis_area':''}
    labellist = []
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
        #현재 페이지의 내용을 가져오고
        bs=BeautifulSoup(source,'html.parser')
        time.sleep(2)
        if(bs.find('div','biz_name_area').find('strong','name')):
            title = bs.find('div','biz_name_area').find('strong','name').text
            #현재 페이지에서 Title에 대해서 가져오기
        else:
            pass
        entire = bs.find('div', class_='bizinfo_area')
        number = entire.find('div', class_='txt').text
        if(entire.find('ul', class_='list_address')):
            address = entire.find('ul', class_='list_address').find_all('li')
            #주소 가져오기
            adlen = len(address)
        else:
            pass
        # print(address[0].text)
        if(adlen == 2): # 주소 내용이 두개라면
            if(address[0]):
                addressroad = address[0].text #도로명주소
            elif(address[1]):
                addressgi = address[1].text #기본주소
            else:
                pass
        elif(adlen == 1): # 주소 내용이 한개라면
            if(address[0]):
                addressroad = address[0].text
                addressgi = address[0].text
        else:
            pass
        if(entire.find('div', class_='biztime')):#오픈시간
            opentime = entire.find('div', class_='biztime').text
        else:
            pass
        if(entire.find('a', class_='biz_url')):#페이지 주소
            pageaddress = entire.find('a', class_='biz_url').text
        else:
            pass
        if(entire.find('div', 'convenience')):#관련정보
            info = entire.find('div', 'convenience').text
        else: 
            pass
        if(bs.find('div', 'ellipsis_area')):#설명
            ea = driver.find_elements_by_class_name('ellipsis_area')#태그를 찾고
            if(ea[0].find_elements_by_class_name('btn_more')): 
                element = ea[0].find_element_by_class_name('btn_more') 
                driver.execute_script("arguments[0].click();", element) #강제로 click하게 javascrpit를 클릭
                time.sleep(4)
                source = driver.page_source
                bs=BeautifulSoup(source,'html.parser')
                ellipsis_area = bs.find('div', 'ellipsis_area').text # 내용을 받아서 내용을 text로 변환
            else:
                pass
        else:
            pass
        test = bs.select('#tabs') #id가 tabs인 것을 찾아서
        for i in test[0]:
            label = i.get('aria-label') #라벨
            controls = i.get('aria-controls') #컨트롤할 부분
            if '사진요약' in label: #라벨안에 사진요약이라는 부분이 있다면
                labelid = i.get('id') # i안에 id를 저장
            else:
                pass
        if driver.find_elements_by_id(labelid):
            labeldr = driver.find_elements_by_id(labelid)
            element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, labelid)))
            #WebDriver에게 만약 늦게 id를 받아오더라도 3초동안 기다리라고 지시후 저장
            element.click()
            time.sleep(3)
            source = driver.page_source
            bs=BeautifulSoup(source,'html.parser')
            if len(bs.select('#'+controls+'> div > div > div.view_area > div.select_photo_area > div.list_photo > div > div:nth-child(1) > div > div')) == 0:
                imgsrc = bs.select('#'+controls+'> div > div > div.view_area > div.select_photo_area > div.list_photo > div > div:nth-child(1) > a > div')
                try: #img 태그가 가끔 없기때문에 예외처리
                    img1 = imgsrc[0].select('img')
                except:
                    img1 = None
                if img1 is not None: #만약 img1가 있다면
                    imgurl = img1[0].attrs['src']
                    img10 = urllib.request.urlopen(imgurl).read()
                else:
                    pass
            else: 
                imgsrc = bs.select('#'+controls+'> div > div > div.view_area > div.select_photo_area > div.list_photo > div > div:nth-child(1) > div > div')                                
                try: #img 태그가 가끔 없기때문에 예외처리
                    img1 = imgsrc[0].select('img')
                except:
                    img1 = None
                if img1 is not None: #만약 img1가 있다면
                    imgurl = img1[0].attrs['src']
                    img10 = urllib.request.urlopen(imgurl).read()
                else:
                    pass
                
            print(img10)
            print(type(img10))
        else:
            pass
        #라벨 dictionary에 crawling한 내용들을 저장
        label_1 = {'title':'','number':'','addressroad':'','addressgi':'','opentime':'','pageaddress':'','info':'','ellipsis_area':'','image':''}
        label_1['title']         = title
        label_1['number']        = number 
        label_1['addressroad']   = addressroad
        label_1['addressgi']     = addressgi
        label_1['opentime']      = opentime
        label_1['pageaddress']   = pageaddress
        label_1['info']          = info
        label_1['ellipsis_area'] = ellipsis_area
        label_1['image']         = img10
        # image.append(img10)
        #list에 append label_1의 내용을 추가
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
        all = B_list(title= ti, number=nu, addressroad= adroad, addressgi=adgi, opentime=opentime, pageaddress=pagead, info=info, ellipsis_area= area, image=image)
        #model에 저장한후 save
        all.save()
