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
        if not mone :
             print("로그인 실패")
        else:
             print("로그인 성공")  
             request.session['userid'] = a  # 자료형 딕셔너리 {"userid":"a"}
            #  request.session['username'] = b #{"userid":"a", "username":"이름"}
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

        return redirect("/member/index")

@csrf_exempt
def list(request):
    cursor = connection.cursor()
    sql = "SELECT * FROM MEMBER"
    cursor.execute(sql)
    key = cursor.fetchall()
    print(key)
    return render(request,'member/list.html', {"key":key})

def logout(request):
    del request.session['userid']  # 세션에 지우기
    return redirect("index")

@csrf_exempt
def delete(request):
    if request.method == "GET":
        return render(request,'member/delete.html')
    elif request.method == "POST":
        cursor = connection.cursor()
        id = request.session['userid']
        print(id)
        pw = request.POST['pw']
        pw1 = request.POST['pwtest']
        if pw == pw1:   
            sql = "DELETE FROM MEMBER WHERE MEM_ID=%s"
            cursor.execute(sql,[id])
        return redirect("list")

@csrf_exempt
def edit(request):
    if request.method == "GET":
        if request.session['userid'] :
            cursor = connection.cursor()
            id = request.session['userid']
            sql = "SELECT * FROM MEMBER WHERE MEM_ID=%s"
            cursor.execute(sql, [id])
            key = cursor.fetchone()
            print(key)
            return render(request,'member/edit.html',{"key":key})
    elif request.method == "POST":
        cursor = connection.cursor()
        id = request.POST['id']
        pw = request.POST['pw']
        # pw1 = request.POST['pw1']
        name = request.POST['name']
        phone1 = request.POST['phone1']
        phone2 = request.POST['phone2']
        phone3 = request.POST['phone3']
        email1 = request.POST['email1']
        email2 = request.POST['email2']
        a1 = [pw,name,(phone1 + "-" + phone2 + "-" + phone3), (email1+"@"+email2),id]
        sql = "UPDATE MEMBER SET MEM_PW=%s,MEM_NAME=%s,MEM_TEL=%s,MEM_EMAIL=%s WHERE MEM_ID=%s"
        cursor.execute(sql, a1)
        # key = cursor.fetchone()
        # pw = request.POST['mail']

        return redirect("list")
