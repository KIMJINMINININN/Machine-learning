# import func as fc 
'''
#fc.add()
# from func import add, sub #add()

# a = fc.sum(7,8)
# b = fc.sub(7,8)
# c = fc.mul()
# d = fc.mul(a=4, b=5)

# print(a,b,c,d)

# def sum2(*args):
#     result = 0 
#     for i in args: 
#         result = result + i 
#     return result 

# fc.tot(10)
# fc.avg(10)

#dictionary
'''
'''
a = {"key1":10,"key2":20,"key3":30}
b = dict(ket1=10, key2=20, key3=30)

a["key4"] = 50

print(a["key4"])
print(a.get("key5",0))
#키가없을경우에 0으로 반환
'''
'''
f = open("C:/Users/admin/Desktop/JIN/data/word.txt", 'r')

while True:
    line = f.readline()
    if not line:
        break
    # print(line)
    a = line.split(" ")
    # print(type(a))
    # b.get("aaa",0)
    # b["aaa"] = 1
    b = dict()
    for tmp in a:
        b[tmp]=b.get(tmp,0)+1
    print(b)
    #dictionary안에 aaa가있는지 확인한후에 없으면 0으로
    #key와 value를 같이 가져오는 형식
    for k, v in b.items():      
        print(k,"-",v,"개")
'''
import requests
import json
import csv

# url="http://ihongss.com/json/exam2.json"
# url="http://ihongss.com/json/exam4.json"

'''
a = dic1[0]
b = dic1[1]
c = dic1[2]

print(a['foods']['dislikes'], b['name'], c['name'])
'''

# url="http://ihongss.com/json/exam6.json"
'''
a = dic1['ret']
b = dic1['data']

test = b[1]["name"]
print(test)
'''
url="http://ihongss.com/json/exam7.json"
strl = requests.get(url).text
dic1 = json.loads(strl)

#{"data":[1,2,3,4,5]}
a = dic1['data']

# print(type(a[0]).__name__)
# print(type(a).__name__)
# b = []
# for i in a:
#     b.append( [i['id'],i['name'],i['age'],i['height'],i['weight']] )

# print(b[0][0])

while True:
    menu = int(input("(1.추가, 2:수정, 3:삭제, 4:목록, 5:저장, 6:읽기, 0:종료)"))
    if menu == 0:
        break
    elif menu == 1:
        # a["id"]= input("id: ")
        # a['name']= input("name: ")
        # a['age']= input("age:")
        # a['height']= input("height:")
        # a['weight'] = input("weight: ")
        # a.append([a['id'],a['name'],a['age'],a['height'],a['weight']])
        id = input("id: ")
        name = input("name: ")
        age = input("age:")
        height = input("height:")
        weight = input("weight: ")
        a.append([id, name , age, height ,weight])
        # print(a)
    elif menu == 2:
        chid = input("수정할 id를 입력해주세요")
        info = input("id의 어떤 정보를 수정할지 정하세요")
        whatinfo = input("정보를 어떻게 수정할지 정하세요")
        for i in a :
            if "dic" == type(i).__name__:
                if i['id'] == chid:
                    i[info] = whatinfo
            elif "list" == type(i).__name__:
                for j in range(0,len(i)):
                    if i[j] == chid:
                        print(i)
                        for k in range(0,len(i)):
                            if i[k] == info:
                                i[k] = info
        # for t in a :
        #     print(t)
    elif menu == 3:
        delete = input("삭제할 id를 입력해주세요")
        info = input("id의 어떤 정보를 지울지 정하세요")
        
        for i in a :
            if i['id'] == delete:
                i[info] = 0
        for t in a :
            print(t)
    elif menu == 4:
        for list in range(0,len(a)):
            print(a[list])
    elif menu == 5:
        f = open('C:/Users/admin/Desktop/JIN/data/20191115.csv', 'w', encoding='utf-8', newline='')
        wr = csv.writer(f)
        #wr = csv.DictWriter(f, fieldnames=['id','name', 'age', 'height', 'weight'])
        #wr.writeheader()

        for tmp in a:
            wr.writerow(tmp)
        print("저장이 완료되었습니다")
        f.close()
    elif menu == 6:
        a.clear()
        f = open('C:/Users/admin/Desktop/JIN/data/20191115.csv', 'r', encoding='utf-8')
        rdr = csv.reader(f)
        #next(rdr, None)

        #print(type(rdr))
        for line in rdr:
            print(line)
            a.append(line)
        print(a)
        f.close()
        # for a in a.items():  
        #     print(t)
'''
b = []
for i in range(5):
    b.append([i,"가나다",34])
print(b)
del b[0]

*****
for a1,a2,a3 in b:
    print(a1,a2,a3)
print()

*****
twolist = [[0]*5 for i in range(5)]

for i in range(0,len(b), 1):
    x,y,z = b[i]
    print(x,y,z)
b = []
Matrix = [[0]*5 for i in range(5)]

for i in range(0,len(a)):
    for x in a[i]:
    for t in range (0,len(a[i])):
        for j in range(0,len(a[i])):
            Matrix[t][j] = a[i]

'''

# url="http://ihongss.com/json/exam10.json"
'''
a = dic1['ret']
b = dic1['data']

test = b[3]['score']['math']
print(test)
'''


#url="http://ihongss.com/json/exam16.json"
'''
def Rank():  
    Rank = input("몇번째 Rank의 정보를 알고싶습니까?")
    for i in range(0,len(a)):
        if Rank == a[i]['rank']:
            print(a[i])

def Name():
    Name = input("어떤 영화의 정보를 얻고싶습니까?")
    for i in range(0,len(a)):
        if Name == a[i]['movieNm']:
            print(a[i]['movieNm'],"의정보는\n",a[i])
        else:
            pass


strl = requests.get(url).text
dic1 = json.loads(strl)
a = dic1['boxOfficeResult']['dailyBoxOfficeList']
while True:    
    print("----목록차트----")
    print("1. Rank별 정보 ")
    print("2. 영화이름별 정보")
    list = input("무엇을 원하십니까")
    # print("")
    if list == '1':
        Rank()
    elif list == '2':
        Name()
    else:
        print("목록에 없는 기능 입니다")
        break
'''
# print(a[0])
# high = len(a)
# high > int(a[i]['rank']):
# high = int(a[i]['rank'])

    # for j in range(0,len(a)):
        # a[i]['rank']

# print(dic1)
'''
for i in range(1,10):
    a = dic1['boxOfficeResult']['dailyBoxOfficeList'][i]['movieNm']
    print(a)
'''
# print(type(dic1))
# dic1 = dic1.split("'ret1'")
# print(dic1)
# a = dic1["ret"]
# b = dic1["ret1"]

# print(dic1['ret'],dic1['data'])
'''
id = []
name = []
age = []
for key in dic1:
    print(dic1[key]["id"])
    id.append(dic1[key]["id"])
    name.append(dic1[key]["name"])
    age.append(dic1[key]["age"])
print(id)
print(name)
print(age)
'''
# for i in range(0, len(id), 1):
#     print("{},{},{}".format(id[i], name[i], age[i]))

# print(dic1['ret'])
# print(dic1[key])

# print(a["id"], a["name"], a["age"])
# print(b["id"], b["name"], b["age"])


