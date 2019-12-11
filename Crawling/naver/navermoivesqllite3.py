# 페이지가 변할때마다 page라는 url이 바뀌게 되는데 그부분을 바꾸어주게되면 가능.
import urllib,csv
from bs4 import BeautifulSoup
import sqlite3
import json


params = urllib.parse.urlencode({'page':1})#쿼리 문자열로 변환
url='https://movie.naver.com/movie/point/af/list.nhn?&%s' %params
#print(url)

response = urllib.request.urlopen(url)
navigator = BeautifulSoup(response,'html.parser')
table=navigator.find('table',class_='list_netizen')
#print(table)

list_records=[]

with open('C:/Users/admin/Documents/PythonStudy0/Crawling/naver/navermoive.csv', 'w', newline='', encoding='UTF-8') as csvfile:
    fieldnames = ['번호', '평점', '영화', '140자평', '글쓴이', '날짜']
    # writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter='|')
    # writer.writeheader()
    for i,r in enumerate(table.find_all('tr')):
        # print(i,':::',r)
        for j,c in enumerate(r.find_all('td')):
            # print(j, ':::', c)
            # print(c)
            if j==0:
                record=int(c.text.strip())
            #    print(record)
            elif j==1:
                record1=str(c.text.strip())
                record2=str(c.find('a',class_='movie').text.strip())
                record3=str(c.text.split('<br>')[0].split('\n')[5])
            elif j==2:
                record4=str(c.find('a',class_='author').text.strip())
                record5=str(c.text).split('****')[1]
        try:
            record_t=tuple([record,record1,record2,record3,record4,record5])
            list_records.append(record_t)
        except:
            pass
    # writer.writerows(list_records)
# print(list_records)
conn=sqlite3.connect('./example.db')
with conn:
    c=conn.cursor()
    sql='CREATE TABLE if not exists moive (no integer, grade integer, title text, content text, writer text, date text)'
    c.execute(sql)
    conn.commit()
    sql='INSERT INTO movie VALUES(?,?,?,?,?,?)'
    c.executemany(sql, list_records)
    conn.commit()
    sql = 'select * from moive'
    c.execute(sql)
    rows = c.fetchall()
    for row in rows:
        print(row)