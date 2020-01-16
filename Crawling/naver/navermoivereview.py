# 페이지가 변할때마다 page라는 url이 바뀌게 되는데 그부분을 바꾸어주게되면 가능.
import urllib,csv
from bs4 import BeautifulSoup
import json

def SearchMoive(page):
    params = urllib.parse.urlencode({'page':page})#쿼리 문자열로 변환
    url='https://movie.naver.com/movie/point/af/list.nhn?&%s'%params
    # url='https://movie.naver.com/movie/point/af/list.nhn?&page=3'
    #print(url)
    response = urllib.request.urlopen(url)
    navigator = BeautifulSoup(response,'html.parser')
    table=navigator.find('table',class_='list_netizen')
    #print(table)
    tablena = table.find('tbody')
    # print(tablena)
    tablena1 = tablena.find('old_content > table > tbody')
    print(tablena1)
SearchMoive(1)
#     list_records=[]

#     with open('C:/Users/admin/Desktop/PythonStudy0/Crawling/navermoive.csv', 'w', newline='', encoding='UTF-8') as csvfile:
#         fieldnames = ['번호', '평점', '영화', '140자평', '글쓴이', '날짜']
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter='|')
#         writer.writeheader()
#         for i,r in enumerate(table.find_all('tr')):
#             # print(i,':::',r)
#             for j,c in enumerate(r.find_all('td')):
#                 # print(j, ':::', c)
#                 # print(c)
#                 if j==0:
#                     record={'번호':int(c.text.strip())}
#                 #    print(record)
#                 elif j==1:
#                     record.update({'평점':str(c.text.strip())})
#                     record.update({'영화':str(c.find('a',class_='movie').text.strip())})
#                     record.update({'140자평':str(c.text).split('<br>')[0].split('\n')[5]})
#                     print({'140자평':str(c.text).split('<br>')[0].split('\n')[5]})
#                 elif j==2:
#                     record.update({'글쓴이':c.find('a',class_='author').text.strip()})
#                     record.update({'날짜':str(c.text).split('****')[1]})
#             try:
#                 list_records.append(record)
#                 writer.writerow(record)
#             except:
#                 pass
#         writer.writerows(list_records)
#         # with open('crawling/moive.json', 'wt') as f:
#         #     json.dump(list_records,f)
            
# if __name__ == "__main__":
#     page=input("몇페이지까지 크롤링?")
#     for t in page:
#         SearchMoive(t)

