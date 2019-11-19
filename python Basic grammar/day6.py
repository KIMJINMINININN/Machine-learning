import requests
import json
import csv

url="http://ihongss.com/json/exam7.json"    # 서버주소
str1 = requests.get(url).text               # 문자열
dic = json.loads(str1) 

a = dic['data']

b = []
for i in a:
    b.append([ i['id'], i['name'], i['age'], i['height'], i['weight'] ])

while True:
    menu = int(input("1:추가, 2:수정, 3:삭제, 4:목록, 5:저장, 6:읽기, 0:종료?"))
    if menu == 0: # 종료
        break

    elif menu == 1:
        a1,a2,a3,a4,a5 = map(str, input("아이디, 이름, 나이, 키, 몸무게 입력?").split(","))
        b.append( [a1,a2,int(a3),float(a4),float(a5)] )

    elif menu == 2: #수정
        a1 = input("수정 할 아이디 입력?")
        a2 = input("이름?")
        a3 = int(input("나이?"))
        a4 = float(input("키?"))
        a5 = float(input("몸무게?"))

        for i, t in enumerate(b): #[ [],[],[],[],[] ]
            if t[0] == a1:
                b[i] = [a1, a2, a3, a4, a5]
                break


    elif menu == 3: #삭제
        #n = int(input("삭제할 위치 입력?"))
        #del b[n]

        s = input("삭제할 아이디 입력?")
        for i, t in enumerate(b): #[ [],[],[],[],[] ]
            if t[0] == s:
                del b[i]
                break
        
    elif menu == 4: #목록
        print(b)

    elif menu == 5: #저장
        # 엑셀에서 한글 깨짐 방지 => 엔코딩을 cp949로 설정
        f = open('c:/Users/admin/Desktop/JIN/data/20191115.csv', 'w', encoding='utf-8', newline='') 
        wr = csv.writer(f)
        
        for tmp in b:
            wr.writerow(tmp) #wr.writerow( ['a','가나다',34, 165.7, 56.6] )
        f.close()

    elif menu == 6:
        f = open('c:/Users/admin/Desktop/JIN/data/20191115.csv', 'r', encoding='utf-8')
        rd = csv.reader(f)
        b.clear()
        for idx, tmp in enumerate(rd):
            b[idx] = [tmp[0], tmp[1], int(tmp[2]), float(tmp[3]), float(tmp[4]) ]
            print(idx, tmp)
        