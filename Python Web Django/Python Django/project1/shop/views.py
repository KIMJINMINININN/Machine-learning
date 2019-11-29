from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from base64 import b64encode
from django.db import connection

from .models import Item

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