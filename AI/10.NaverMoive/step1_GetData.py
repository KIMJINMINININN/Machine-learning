import requests
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd 

def step1_GetData():
    code_list = [167638, 109906]
    #현재 크롤링인 영화가 몇번째?
    chk = False 
    #영화의 갯수만큼 반복

    for code in code_list :
        #1단계: 해당영화의 평점 페이지수 계산
        #접속
        site1 = "https://movie.naver.com/movie/point/af/list.nhn?&page=3"
        res1 = requests.get(site1)
        print(site1)
        if res1.status_code == requests.codes.ok :
            #html code 분석한다
            bs1 = BeautifulSoup(res1.text, "html.parser")

            score_total = bs1.find(class_="c_88")
            #ems - score_total.find.all("em")
            score_total = int(score_total.text)
            #페이지수계산
            pageCnt =  score_total // 10
            if score_total % 10 > 0 :
                pageCnt +=1
            
            print(pageCnt)

            #현재 페이지 번호 
            now_page = 1
            # pageCnt = 5

            while now_page <=pageCnt :
                # sleep(0.5)
                #요청할 페이지의 주소
                site2 = \
                    'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=%d&typeafter&osActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page=%d'%(code,now_page)
                        
                res2 = requests.get(site2)
                if res2.status_code == requests.codes.ok :
                    bs2 = BeautifulSoup(res2.text,'html.parser')

                    score_result = bs2.find(class_='score_result')
                    lis = score_result.find_all('li')

                    df = pd.DataFrame()

                    for obj in lis:
                        star_score = obj.find(class_='star_score')  
                        star_em = star_score.find('em')
                        star_score = int(star_em.text)
                        score_reple = obj.find(class_='score_reple')
                        reple_p = score_reple.find('p')
                        score_reple = reple_p.text.strip()

                        df = df.append([[score_reple,star_score]],ignore_index=True)

                    if chk == False:
                        df.columns = ['text','star']
                        df.to_csv('naver_star_data.csv',index=False,encoding='utf-8-sig')
                        chk = True
                    else:
                        df.to_csv('naver_star_data.csv',index=False,encoding='utf-8-sig',mode='a',header=False)

                    print('%d / %d'%(now_page,pageCnt))
                    now_page += 1
