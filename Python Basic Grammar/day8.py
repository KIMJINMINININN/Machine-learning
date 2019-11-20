import pandas as pd 
import cx_Oracle as oci

a = [0,1,2,3,4,5,6]

conn=oci.connect("admin/1234@192.168.99.100:32764/xe", encoding="utf-8")

df = pd.read_sql('SELECT * FROM ITEM', con=conn)
cursor=conn.cursor()
# print(df)
num = 10
# 1:추가, 2:삭제, 3:수정, 4:목록, 5:검색, 0:종료
while True:
    menu = int(input("메뉴를 입력하세요 1:추가, 2:삭제, 3:수정, 4:목록, 5:검색, 0:종료"))
    if menu == 1:
        input1 = input("추가할 항목 입력?index,이름,이름설명,가격,??,분류")
        arr1 = input1.split(",")
        print(arr1)
        # input2 = input("음식설명을 입력하세요")
        # input3 = input("가격을 입력하세요")
        # input4 = input("을 입력하세요")
        # input5 = input("CATE을 입력하세요")
        
        #형식을변환 
        sql = "INSERT INTO ITEM VALUES(:1,:2,:3,:4,:5,:6,SYSDATE)"
        cursor.execute(sql,arr1)
        conn.commit()
        # data = cursor.fetchall()
        # print(type(data))
        # print(data)
    elif menu == 2:
        input1 = input("삭제할 항목 입력:")
        sql = "DELETE FROM ITEM WHERE ITM_NAME = :id"
        cursor.execute(sql,id=input1)
        conn.commit()
        pass
    elif menu == 3:
        input1 = input("수정할 항목 입력:")
        input2 = input("이름,내용, 가격, 재고수량,분류")
        arr2 = input2.split(",")
        arr2.append(input1)
        #리스트
        sql = "UPDATE ITEM SET ITM_NAME=:1,ITM_CONTENT=:2, ITM_PRICE=:3, ITM_QTY=:4, ITM_CATE=:5 WHERE ITM_NO = :6"
        cursor.execute(sql,arr2)
        conn.commit()
        pass
    elif menu == 4:
        df = pd.read_sql('SELECT * FROM ITEM ORDER BY ITM_NO ASC', con=conn)
        print(df)
    elif menu == 5:
        # SELECT * FROM ITEM WHERE ITM_PRICE >= 2000;
        # SELECT * FROM ITEM WHERE ITM_QTY >= 10;
        # SELECT * FROM ITEM WHERE ITM_NAME = :1;
        menu1 = int(input("어떠한 정보를 검색하고싶으십니까 1.이름, 2.가격이상 3.재고이상"))
        if menu1 == 1:
            name = input("이름이 무엇입니까?")
            sql = "SELECT * FROM ITEM WHERE ITM_NAME = :h"
            cursor.execute(sql,h=name)
            data = cursor.fetchall()
            print(data)
        elif menu1 == 2 :
            charge = input("가격이얼마이상을 찾고싶습니까?")
            sql = "SELECT * FROM ITEM WHERE ITM_PRICE >= :h"
            cursor.execute(sql,h=charge)
            data = cursor.fetchall()
            print(data)
        elif menu1 == 3 :
            qty = input("재고가얼마이상을 찾고싶습니까?")
            sql = "SELECT * FROM ITEM WHERE ITM_PRICE >= :h"
            cursor.execute(sql,h=qty)
            data = cursor.fetchall()
            print(data)
    elif menu == 0:
        break


'''
conn=oci.connect("admin/1234@192.168.99.100:32764/xe", encoding="utf-8")
cursor=conn.cursor()
sql = "SELECT * FROM ITEM"
cursor.execute(sql)
data = cursor.fetchall()
print(type(data))
print(data)

a = []
for i in data:
    a.append(list(i))
print(a)
'''