# 네이버 영화페이지 평점리뷰 크롤링 연습 
# 내용을 크로링해서 보기만 하고 끄는게 아닌 엑셀로 저장해보자.
import urllib.request, csv
from bs4 import BeautifulSoup
import time

# 이 로직 전체를 함수로 만들어줘라.
params = urllib.parse.urlencode({'page':1})
def pageConfig(params):
    url='https://movie.naver.com/movie/point/af/list.nhn?{}'.format(params)
    parserType = 'lxml'
    #print(url)
    response = urllib.request.urlopen(url)
    navigator = BeautifulSoup(response, parserType)
    return navigator

def jumpInTarget(navigator):
    table = navigator.find('table', class_='list_netizen')
    return table

with open('navermovie1.csv', 'a', newline='', encoding='UTF-8') as csvfile: # 뭔가 저장하려고 시작하는 작업. w면 새로작성하고 덮어쓰기, a면 write,append까지가능.
    fieldnames = ['번호','평점', '영화', '140자평', '글쓴이', '날짜']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter='|') # 구분자가 다음과 같다고 하는듯?
    writer.writeheader()
    for page in range(801):
        # time.sleep(2)
        print("page : ",page)
        params = urllib.parse.urlencode({'page':page})
        navigator=pageConfig(params)
        table = jumpInTarget(navigator)
        # print(table)
        list_records = []
        for iIdx, r in enumerate(table.find_all('tr')): # tr만큼 루프돌고
            # print(iIdx, ':::', r)
            for jIdx, c in enumerate(r.find_all('td')): # td만큼 루프돌고
                # print(iIdx, ':::', c)
                if jIdx==0:
                    num = int(c.text.strip())
                    record ={'번호': num }
                elif jIdx==1:
                    score = str(c.find('em').text)
                    movieName = str(c.find('a',class_='movie').text.strip() )
                    review = str(c.text.split('\n')[5]) 
                    # print("score",score)
                    # print("movieName",movieName)
                    # print("review",review)
                    record.update({'평점':score})
                    record.update({'140자평':review})
                elif jIdx==2:
                    author = c.find('a',class_='author').text.strip()
                    date = str(c.text).split('****')[1]
                    # print('author',author)
                    # print('date',date)
                    # pass
                elif jIdx==3:
                    pass
                    # record.update({'영화':str(c.find('a',class_='movie').text.strip() )})
                    # record.update({'140자평':str(c.text).split('\n')[2]})
                elif jIdx==4:
                    #  record.update({'글쓴이':c.find('a',class_='author').text.strip()})
                    #  record.update({'날짜':str(c.text).split('****')[1]})
                    pass
            try:
                if review != '': list_records.append(record)
                 # 정상적으로 안들어감 들어가게끔 만들자
                #writer.writerow(record)
            except:
                pass
        writer.writerows(list_records)

# print()



