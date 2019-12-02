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


