from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from base64 import b64encode
from django.db import connection

from .models import Item
from .models import Student  #model 추가

import pandas as pd

import matplotlib.pyplot as plt #그래프 그리기
from matplotlib import font_manager, rc #한글 적용 폰트 설정
import io   # 그래프를 byte로 변경
import base64

def index(request):
    return render(request,'shop/index.html')

@csrf_exempt
def insert(request):
    if request.method == "GET":
        return render(request,'shop/insert.html')
    elif request.method == "POST":
        na = request.POST['na']
        co = request.POST['co']
        pr = request.POST['pr']
        qt = request.POST['qt']
        obj = Item(itm_name=na, itm_content=co, itm_price=pr, itm_qty=qt)
        obj.save()
        return redirect('/shop/index')

@csrf_exempt
def update(request):
    if request.method == "GET":
        no = request.GET.get("no", 0)
        obj = Item.objects.get(itm_no=no)
        return render(request, 'shop/update.html', {"one":obj})
    elif request.method == "POST":
        no = request.POST['no']
        obj = Item.objects.get(itm_no=no)
        obj.itm_no = request.POST['no']
        obj.itm_name = request.POST['na']
        obj.itm_content = request.POST['co']
        obj.itm_price = request.POST['pr']
        obj.itm_qty = request.POST['qt']
        obj.save()
        return redirect('/shop/select')

def delete(request):
    if request.method == "GET":
        no = request.GET.get("no", 0)
        print(no)
        obj = Item.objects.get(itm_no=no)
        obj.delete()
        #print(obj.query)
        return render(request, 'shop/select.html')

def select(request):
    if request.method == "GET":
        # rows = Item.objects.raw("SELECT * FROM SHOP_ITEM ORDER BY ITM_NO DESC")
        rows = Item.objects.all()
        for tmp in rows:
            print(tmp.itm_no, tmp.itm_name, tmp.itm_content, tmp.itm_price)
        return render(request,'shop/select.html',{"rows":rows})
# @csrf_exempt
# def login(request):
#     if request.method == "GET":
#         return render(request,'member/login.html')
from django.db.models import Max, Min, Avg, Count, Sum

def select1(request) :
    # SELECT SUM(age) FROM SHOP_STUDENT
    a = Student.objects.aggregate(Sum('age')) #나이 합
    print(a["age__sum"]) # 딕셔너리 키를 바꿀수 없음.

    # SELECT MAX(age) FROM SHOP_STUDENT
    obj = Student.objects.aggregate(max1=Max('age'))
    print(obj['max1']) #딕셔너리 키를 max1로 바꿈

    # obj1 = Student.objects.raw("SELECT * FROM SHOP_STUDENT WHERE age <= 20")
    obj1 = Student.objects.filter(age__lte=20) 
    print(obj1)

    # SELECT * FROM SHOP_STUDENT 
    rows1 = Student.objects.all().values_list() #타입을 list로

    # html파일을 만들지 않고 출력
    return HttpResponse("select1 page")

def graph(request) :

    x = [10,20,30,40,50,60,70]
    y = [ 0, 0, 0, 0, 0, 0, 0]

    rows = Student.objects.all() #QuerySet
    for t in rows : 
        print("{},{},{}".format(t.id, t.name, t.age))
        if 0<= t.age <=19 :
            y[0] += 1
        elif 20<= t.age <=29 :
            y[1] += 1   
        elif 30<= t.age <=39 :
            y[2] += 1  
        # 생략함.
        
    #한글 폰트 사용하기
    font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
    rc('font', family=font_name)

    plt.bar(x, y)
    plt.title('AGES % PERSON')
    plt.xlabel('AGES')
    plt.ylabel('PERSON')

    plt.draw() # 그래프 그리기
    img = io.BytesIO() # 그린 그래프를 byte로 변경
    plt.savefig(img, format="png") # png포멧으로 변경
    graph_url = base64.b64encode(img.getvalue()).decode()
    plt.close() #그래프 종료
    return render(request, 'shop/graph.html', {"graph1":'data:image/png;base64,{}'.format(graph_url)})

def dataframe(request):
    obj = Student()
    obj.id='a'
    obj.age=10
    obj.name ='b'
    obj.save()

    obj1 = Student(id='c',age=30, name='홍길동')
    obj1.save()

    data = list(Student.objects.all().values())
    # print(data)
    df = pd.DataFrame(data)
    print(df)

    data1 = df.values.tolist() #df to list로 변경 [[],[],[]]
    # print(data1)
    return render(request, 'shop/dataframe.html',{"key":df.to_html(classes='table'), "key1":data1})

def dataframe_item(request):
    ord = int(request.GET.get("order", 1))
    if ord == 1:
        a = Item.objects.all().order_by('itm_no')
    elif ord == 2:
        a = Item.objects.all().order_by('-itm_no')
    # print(a)
    data = list(a)
    print(data)
    df = pd.DataFrame(data)
    # print(data)
    print(df)
    # return render(request, 'shop/dataframe_item.html',{"data":data})
    return render(request, 'shop/dataframe_item.html',{"key":df.to_html(classes='table'), "data":data})

@csrf_exempt
def insert_multi(request) :
    if request.method == "GET" :
        return render(request, 'shop/insert_multi.html')        
    elif request.method == "POST" :
        id1 = request.POST.getlist("id[]") # 중복된 name값 
        na1 = request.POST.getlist("na[]")
        ag1 = request.POST.getlist("ag[]")

        objs = []
        for i in range(0, len(id1), 1) : 
            print(id1[i], na1[i], ag1[i])
            obj = Student(id=id1[i], name=na1[i], age=ag1[i])
            objs.append(obj)
            #obj.save() #권장 방법이 아님.

        Student.objects.bulk_create(objs) # batch commit
        return redirect("/shop/insert_multi")

@csrf_exempt
def update_multi(request) :
    if request.method == "GET" :
        # [ (한줄),(한줄),(한줄) ]
        rows = Student.objects.all().order_by('id')[:10] #10개만
        print(type(rows[0]))  #첫번째 것 꺼내서 type확인
        # ['a','b',34]    => one.0  one.1  one.2
        # ('a','b',45)    => one.0  one.1  one.2
        # {"id":"a", "name":"b", "age":34} => one.id
        # Student object타입 => one.id one.name
        return render(request, 'shop/update_multi.html',{"abc":rows})        

    elif request.method == "POST" :
        id = request.POST.getlist("a[]")
        na = request.POST.getlist("b[]")
        ag = request.POST.getlist("c[]")

        objs = []
        for i in range(0, len(id), 1):
            obj = Student.objects.get(id = id[i])
            obj.name = na[i]
            obj.age = ag[i]
            #obj.save()  #권장 방법이 아님.
            objs.append(obj)

        Student.objects.bulk_update(objs, ["name","age"])

        return redirect("/shop/update_multi")  

@csrf_exempt
def delete_multi(request) :
    if request.method == "GET" :
        rows = Student.objects.all()
        print(type(rows[0])) #one.id, one.name

        rows1 = Student.objects.raw("SELECT * FROM SHOP_STUDENT")
        print(type(rows1[0]))
        return render(request, 'shop/delete_multi.html', {"abc":rows1})

    elif request.method == "POST" :
        chk = request.POST.getlist("chk[]")
        print(chk)
        Student.objects.filter(id__in=chk).delete()
        return redirect("/shop/delete_multi")
        
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

@csrf_exempt
def auth_join(request) :
    if request.method == "GET":
        return render(request, 'shop/auth_join.html')
    elif request.method == "POST":
        obj = User.objects.create_user(
            username = request.POST['username'],
            first_name = request.POST['password'],
            password = request.POST['first_name'],
            email = request.POST['email'])
        obj.save()
        return redirect("/shop/index")

@csrf_exempt
def auth_index(request) :
    if request.method == "GET":
        return render(request, 'shop/auth_index.html')

@csrf_exempt
def auth_login(request) :
    if request.method == "GET":
        return render(request, 'shop/auth_login.html')
    elif request.method == "POST":
        id = request.POST['username']
        pw = request.POST['password']

        user = authenticate(request, username=id, password=pw)
        if user is not None:
            login(request,user)
            return render(request, 'shop/alert.html', {"msg":"로그인성공", "url":"/shop/auth_index",'chk':'2'})
            # return redirect("/shop/auth_index")
        else:
            return redirect("/shop/auth_login")

@csrf_exempt
def auth_logout(request):
    logout(request)
    return render(request, 'shop/alert.html', {"msg":"로그아웃", "url":"/shop/auth_index",'chk':'1'})
    # return redirect("/shop/auth_index")

@csrf_exempt
def auth_edit(request): #html을 게시판으로 사용
    # logout(request)
    if request.method == "GET":
        if not request.user.is_authenticated :
            return redirect("/shop/auth_login")
        else:
            print(request.user)
            user = User.objects.get(username=request.user)
            return render(request, 'shop/auth_edit.html', {"user":user})
    elif request.method == "POST":
        id = request.POST['username']
        first_name = request.POST['first_name']
        email = request.POST['email']
        
        user = User.objects.get(username=id)
        user.first_name = first_name
        user.email = email
        user.save()
    return redirect("/shop/auth_index")

@csrf_exempt
def auth_pw(request):
    if request.method == "GET":
        if not request.user.is_authenticated :
            return redirect("/shop/auth_login")
        else:
            return render(request, 'shop/auth_pw.html')
    elif request.method == "POST":
        passwd = request.POST['passwd']
        passwdch1 = request.POST['passwdch1']
        passwdch2 = request.POST['passwdch2']
        name = request.user
        user = authenticate(request, username=name, password=passwd)
        if passwdch1 == passwdch2:
            user.set_password(passwdch1)
            user.save()
        else:
            return redirect("/shop/auth_pw")
    return redirect("/shop/auth_index")