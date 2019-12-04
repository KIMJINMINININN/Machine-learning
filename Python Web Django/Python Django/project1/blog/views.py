from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from base64 import b64encode
from django.db import connection
import pandas as pd
import matplotlib.pyplot as plt #그래프 그리기
from matplotlib import font_manager, rc #한글 적용 폰트 설정
import io   # 그래프를 byte로 변경
import base64
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

@csrf_exempt
def auth_index(request) :
    if request.method == "GET":
        return render(request, 'blog/auth_index.html')

@csrf_exempt
def auth_join(request) :
    if request.method == "GET":
        return render(request, 'blog/auth_join.html')
    elif request.method == "POST":
        obj = User.objects.create_user(
            username = request.POST['username'],
            first_name = request.POST['password'],
            password = request.POST['first_name'],
            email = request.POST['email'])
        obj.save()
        return redirect("/blog/auth_index")

@csrf_exempt
def auth_login(request) :
    if request.method == "GET":
        return render(request, 'blog/auth_login.html')
    elif request.method == "POST":
        
        id = request.POST['username']
        pw = request.POST['password']

        user = authenticate(request, username=id, password=pw)
        if user is not None:
            login(request,user)
            return render(request, 'blog/alert.html', {"msg":"로그인성공", "url":"/blog/auth_index",'chk':'2'})
            # return redirect("/shop/auth_index")
        else:
            return redirect("/blog/auth_login")

@csrf_exempt
def auth_logout(request):
    logout(request)
    return render(request, 'blog/alert.html', {"msg":"로그아웃", "url":"/blog/auth_index",'chk':'1'})
    # return redirect("/shop/auth_index")

@csrf_exempt
def auth_edit(request): #html을 게시판으로 사용
    # logout(request)
    if request.method == "GET":
        if not request.user.is_authenticated :
            return redirect("/blog/auth_login")
        else:
            print(request.user)
            user = User.objects.get(username=request.user)
            return render(request, 'blog/auth_edit.html', {"user":user})
    elif request.method == "POST":
        id = request.POST['username']
        first_name = request.POST['first_name']
        email = request.POST['email']
        
        user = User.objects.get(username=id)
        user.first_name = first_name
        user.email = email
        user.save()
    return redirect("/blog/auth_index")

@csrf_exempt
def auth_pw(request):
    if request.method == "GET":
        if not request.user.is_authenticated :
            return redirect("/blog/auth_login")
        else:
            return render(request, 'blog/auth_pw.html')
    elif request.method == "POST":
        # reqeust.user.id의 값을 가지고올수있다 ####****
        passwd = request.POST['passwd']
        passwdch1 = request.POST['passwdch1']
        passwdch2 = request.POST['passwdch2']
        name = request.user
        user = authenticate(request, username=name, password=passwd)
        if passwdch1 == passwdch2:
            user.set_password(passwdch1)
            user.save()
        else:
            return redirect("/blog/auth_pw")
    return redirect("/blog/auth_index")