from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

from django.db import connection

def index(request):
    return render(request,'member/index.html')

@csrf_exempt
def login(request):
    if request.method == "GET":
        return render(request,'member/login.html')
    elif request.method == "POST":
        cursor = connection.cursor()
        a = request.POST['id']  
        b = request.POST['pw']

        a1 = [a, b] # 아이디와 암호 값을 a1리스트에 추가
        sql = "SELECT * FROM MEMBER WHERE MEM_ID=%s AND MEM_PW=%s"
        cursor.execute(sql, a1)
        mone = cursor.fetchone()
        print(mone)
        # if not mone :
        #     print("로그인 실패")
        # else:
        #     print("로그인 성공")  
        #     session['userid'] = mone[0]  # 자료형 딕셔너리 {"userid":"a"}
        #     session['username'] = mone[1] #{"userid":"a", "username":"이름"}
        return redirect('/member/index')

@csrf_exempt
def join(request):
    if request.method == "GET":
        return render(request,'member/join.html')
    elif request.method == "POST":
        cursor = connection.cursor()
        id = request.POST['id'] #'id' input type="text" name="id"
        pw = request.POST['pw']
        # pw1 = request.form['pw1']
        name = request.POST['name']
        tel1 = request.POST['tel1']
        tel2 = request.POST['tel2']
        tel3 = request.POST['tel3']
        email1 = request.POST['email1']
        email2 = request.POST['email2']
        a1 = [id,pw,name,(tel1 + "-" + tel2 + "-" + tel3), (email1+"@"+email2)]
        sql = "INSERT INTO MEMBER(MEM_ID, MEM_PW, MEM_NAME, MEM_TEL, MEM_EMAIL, MEM_DATE) VALUES(%s,%s,%s,%s,%s,SYSDATE)"
        cursor.execute(sql, a1)
        # cursor.commit()
        return redirect("/member/join")