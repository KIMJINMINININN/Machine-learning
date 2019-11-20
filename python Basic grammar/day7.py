import requests
import json
import pandas as pd
from pandasql import sqldf
pysqldf = lambda q: sqldf(q, globals())
from matplotlib import pyplot as plt
import re

url="http://ihongss.com/json/exam20.json"
strl = requests.get(url).text
dic1 = json.loads(strl)
b = []
for i, t in enumerate(dic1):
    a1 = t["cost"].split(",") #"10000,200,3000" -> ["10000","200","3000"]
    for i1, t1 in enumerate(a1):
        a1[i1] = int(t1)
    a1.insert(0,t['code'])
    a1.insert(1,t['name'])
    b.append(a1)

df = pd.DataFrame(b, columns = ['code', 'name', 'a01', 'a02','a03','a04','a05','a06','a07','a08','a09','a10','a11','a12'])
# print(df.shape)
# print(df[['code', 'name', 'a01', 'a02','a03','a04','a05','a06','a07','a08','a09','a10','a11','a12']] )
# print(pysqldf("SELECT * FROM df WHERE a12 >= 10000"))

tot = [0,0,0,0,0,0,0,0,0,0,0,0]
# print(b)
for i, m in enumerate(b):
    for j in range(2,14,1):
        tot[j-2] = tot[j-2] + m[j]

tot1 = [1,1,1,1,1,1,1,1,1,1,1,1]
for i in range(0,12,1):
    for j in range(0,12,1):
        if tot[i] < tot[j]:
            tot1[i] = tot1[i]+1
for i, t in enumerate(tot):
    if tot1[i]<=3:
        print(tot[i])
# 그래프 그려주기
# aa = list(range(1,13,1)) 
# plt.plot(aa,tot)
# plt.show()
    # for j in range(2,len(m)):
        # a[j] = a[j] m[j]

# a.sort(reverse=True)
# print(a[:3])
'''
aaa = [1,4,5,2,7]
bbb = [1,1,1,1,1]

for i in range(0,5,1):
    for j in range(0,5,1):
        if aaa[i] < aaa[j]:
            bbb[i] = bbb[i]+1
print(bbb)
for i, t in enumerate(aaa):
    if bbb[i]<=3:
        print(aaa[i])
        '''
#오름차순
'''        
a = [3,56,7,89,23]
max = a[0]
for i in range(0,5):
    for j in range(0,5):
        if a[i] > a[j]:
            max = a[j]
            a[j] = a[i]
            a[i] = max
        else:
            pass
print(a)
'''
###최대값 구하기
# a = [3,56,7,89,23]
# max = a[0]
# for i, t in enumerate(a):
#     if max < t:
#         max = t
#         maxi = i
# print(max, maxi)
###


'''
for i, t in enumerate(dic1):
    a1 = t["cost"].split(",") #"10000,200,3000" -> ["10000","200","3000"]
    for i1, t1 in enumerate(a1):
        a1[i1] = int(t1)
########
# enumerate를 사용한것과 아닌것
for i in range(0,len(dic1)):
    a.append(dic1[i]["cost"])
for i in range(0,len(a)):
    c.append(a[i].split(','))

for t in range(0,len(c)):
    for h in range(0,len(c[t]):
        b[t] = int(c[t][h])
########
'''
    
# print(s)

# for j in range(0,len(a)):
#     a = a[j].split(',')
# for s in range(0,len(a)):
#     a[s]

# for s, t in enumerate(a):
#     a[s] = int(t)
# print(a)


# for i in range(1,):

# pandas 사용해서 data 정렬

str = "1234abc"
a = re.match('[0-9]+', str)
print(a.span())
print(a.group())

a = re.match('[0-9]{3}-[0-9]{4}-[0-9]{4}$', '010-0000-0000')
print(a)

    