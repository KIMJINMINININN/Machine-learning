'''
a = [1,2,3,4,5] # 값 변경 가능 -> List() 
b = [1,2,3,3,4] # 값 변경 불가 -> Tuple()
c = (2,2,3,4,5) # 값 변경 불가 -> Set()
d = {'aaa':1, 'bbb':2, 'ccc':3} #dictionary key:value 값으로 나누어져있는 자료구조

for i in a:
    print(i, end=" ")
print()

for i in b:
    print(i, end=" ")
print()

for i in c:
    print(i, end=" ")
print()

for i,j in d.items(): 
    print("{}:{}".format(i,j), end=" ")
print()

e = [   ['id1', 'name1', '010-0000-0000', 25], 
        ['id2', 'name2', '010-0000-0000', 35],
        ['id3', 'name3', '010-0000-0000', 45] ]
#리스트 형태로 한곳에 넣기위해서는 이러한 형태로 넣어주어야한다

for i in e:
    print(i[0])
#print(i[0])의결과는-> 인덱스 이용
#id1
#id2
#id3
'''

import csv
# import pandas as pd
import cx_Oracle as oci #conda install oracle

conn = oci.connect('admin/1234@192.168.99.100:32764/xe', encoding="utf-8")
# df_ora = pd.read_sql('SELECT * FROM SCORE', con=conn)
# print(type(df_ora))
# print(df_ora)
# print(sum(df_ora['JAVA'])) # pandas를 이용하여 JAVA의 값을 출력하기

cursor = conn.cursor()  # cursor 객체 얻기
cursor.execute('SELECT * FROM SCORE')  # SQL 문장 실행
data = cursor.fetchall()


# javg = 0
# cavg = 0
# pavg = 0

# # print(type(data))
check = True
while True:
    id = input("id를 입력하세요 : ")
    for i in data:
        if id == i[0]:
            print("id", i[0], "의 정보는", i,"입니다")
            check = True
            break
        else:
            check = False
    if check == False:
        print("Waring :: 존재하지않는 id입니다")
    # print(data)

# for i in data:
#     javg = javg + i[3]
#     cavg = cavg + i[4]
#     pavg = pavg + i[5]
# javg = javg / 3
# cavg = cavg / 3
# pavg = pavg / 3

# print("java의 평균 : ",javg, " c의 평균 : ",cavg, " python의 평균", pavg)
# blog_list = cursor.fetchall() #[(),(),()] 포멧
# print(blog_list)
# #print(blog_list[2][4])
'''
while True:
    id = input("id ? ")
    if id == "exit":
        break
    name = input("name ? ")
    tel = input("tel ?")
    java = int(input("java ?"))
    c = int(input("c ?"))
    python = int(input("python ?"))
    print("{}-{}-{}-{}-{}-{}".format(id, name, tel, java, c, python))

    insert_sql = "INSERT INTO SCORE VALUES(:a, :b, :c, :d, :e, :f, SYSDATE)"
    cursor = conn.cursor()
    cursor.execute(insert_sql, a=id, b=name, c=tel, d=java, e=c, f=python)
    conn.commit() #commit 하여주어서 DB에 저장

conn.close() # DB 연결 종료
'''
# conn.close()

def add(a, b): 
    result = a + b 
    return result


print("life"+"is"+"too short")
print(i, end=' ') 