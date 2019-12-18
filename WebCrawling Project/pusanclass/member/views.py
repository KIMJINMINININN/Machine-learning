from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.db import connection
from base64 import b64encode
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from .models import Join

import re



@csrf_exempt
def join(request):
    if request.method =="GET":
        return render(request, 'member/join.html')
    if request.method == "POST":
        id = request.POST['id']  
        pw1 = request.POST['pw1']
        pw2 = request.POST['pw2']
        name = request.POST['name'] 
        tel = request.POST['tel']
        email = request.POST['email']
        obj = Join(id = id, pw = pw1, name=name, tel =tel, email=email)
        if pw1 == pw2:
            regex = re.compile(r'([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,4}))')
            gol = regex.search(email)
            if  gol:
                regex1 = re.compile(r'(\w{3})-(\w{3}|\w{4})?-(\w{4})')
                te = regex1.search(tel)
                if te:
                    pass
                else:
                    return render(request, "member/alert.html",{"msg":"전화번호 형식이 잘못되었습니다.",'url':'/member/join'})
            else:
                return render(request, "member/alert.html",{"msg":"@를 포함하여 이메일을 써주세요.",'url':'/member/join'})
        else:
            return render(request, "member/alert.html",{"msg":"암호가 동일하지 않습니다.",'url':'/member/join'})
        obj.save()
        return render(request, "member/alert.html",{"msg":"회원가입이 완료되었습니다..",'url':'/home/index'})



@csrf_exempt
def login(request):
    if request.method =='GET':
        return render(request, "member/login.html")
    elif request.method == 'POST':
        a = request.POST['id']
        b = request.POST['pw1']
        a1= [a,b]
        cursor = connection.cursor()
        sql = "SELECT * FROM member_join WHERE id = %s AND pw = %s"
        cursor.execute(sql, a1) 
        ip = cursor.fetchone()
        if not ip:
            return render(request, "member/alert.html",{"msg":"입력이 틀렸습니다.",'url':'/home/index'})
        else:
            request.session['userid'] = ip[0]
            request.session['userpw'] = ip[1]    # 세션에 값 넣기
            request.session['username'] = ip[2] #자료형 딕셔너리 {"userid":"a"}
            return render(request, "member/alert.html",{"msg":"로그인되었습니다..",'url':'/home/index'})

def logout(request):
    del request.session['userid']
    del request.session['userpw']
    del request.session['username']  # 세션에 값 지우기
    return redirect("/home/index")

@csrf_exempt    
def delete(request):
    if request.method == 'GET':
        return render(request, 'member/delete.html')
    elif request.method == "POST":
        a = request.session["userpw"]
        b = request.session["userid"]
        c = request.POST['pw1']
        if a == c :
            Join.objects.get(id=b).delete()
            del request.session["userid"]
            del request.session["userpw"]
            return render(request, "member/alert.html",{"msg":"회원 삭제되었습니다..",'url':'/home/index'})
        else :
            return render(request, "member/alert.html",{"msg":"암호가 동일하지 않습니다.",'url':'/member/delete'})

@csrf_exempt 
def edit(request):
    if request.method =='GET':
        a = [request.session["userid"]]
        cursor =connection.cursor()
        sql = 'SELECT * FROM member_join WHERE id = %s'
        cursor.execute(sql,a)
        b = cursor.fetchone()
        return render(request, "member/edit.html", {'data':b})
    elif request.method == 'POST':
        id = request.session["userid"]
        pw1 = request.POST['pw1']
        pw2 = request.POST['pw2']
        name = request.POST['name']
        tel = request.POST['tel']
        email =request.POST['email']
        if pw1 == pw2:
            regex = re.compile(r'([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,4}))')
            gol = regex.search(email)
            if  gol:
                regex1 = re.compile(r'(\w{3})-(\w{3}|\w{4})?-(\w{4})')
                te = regex1.search(tel)
                if te:
                    pass
                else:
                    return render(request, "member/alert.html",{"msg":"전화번호 형식이 잘못되었습니다.",'url':'/member/join'})
            else:
                return render(request, "member/alert.html",{"msg":"@를 포함하여 이메일을 써주세요.",'url':'/member/join'})
        else:
            return render(request, "member/alert.html",{"msg":"암호가 동일하지 않습니다.",'url':'/member/join'})
        a1 = [pw1, name, tel, email, id]
        cursor =connection.cursor()
        sql = 'UPDATE member_join SET pw = %s, name = %s, tel = %s, email =%s WHERE id = %s'
        cursor.execute(sql,a1)
        del request.session['userid']
        del request.session['userpw']
        del request.session['username']
        return render(request, "member/alert.html",{"msg":"수정이 완료되었습니다.",'url':'/home/index'})
    return render(request, "member/edit.html")