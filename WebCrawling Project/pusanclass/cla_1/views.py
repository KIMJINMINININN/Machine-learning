from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.db import connection
from base64 import b64encode
from django.core.paginator import Paginator
from .models import List


@csrf_exempt
def submit(request):
    if request.method == 'GET':
        ti = request.GET.get('title',0)
        request.session["bo_title"] = ti
        return render(request, "cla_1/submit.html", {'title':ti})    
    elif request.method =='POST':
        id = request.session["userid"]
        da = request.POST.get('date',0)
        co = request.POST.get('content',0)
        na = request.session["bo_title"] 
        #수강처확인을 위한 세션등록
        obj = List(id=id, title=na, date=da, content=co)
        obj.save() #INSERT
        # print(id, da, co)
        return render(request, "member/alert.html",{"msg":"수강신청이 완료되었습니다.",'url':'/home/index'})


def submit_ch(request):
    if request.method == 'GET':
        a = request.session["userid"]
        try:
            b = List.objects.get(id=a)
        except:  
            b = None
        # cursor = connection.cursor()
        # sql = "SELECT * FROM cla_1_list WHERE id = a"
        # cursor.execute(sql) 
        # b = cursor.fetchone()
        return render(request, "cla_1/submit_ch.html",{'data':b})
   
def submit_de(request):
    if request.method == 'GET':
        a = request.session["userid"]
        List.objects.get(id=a).delete()
        del request.session['bo_title']
        return render(request, "member/alert.html",{"msg":"수강이 삭제되었습니다.",'url':'/home/index'})

@csrf_exempt 
def submit_ed(request):
    if request.method =='GET':
        a = request.session["userid"]
        print(a)
        b = List.objects.get(id=a)
        return render(request, "cla_1/submit_ed.html", {'data':b})
    elif request.method == 'POST':
        i = request.session["userid"]
        da = request.POST.get('date_1',0)
        co = request.POST.get('content',0)
        a1 = [da, co, id]
        print(a1)
        edit = List.objects.get(id=i)
        edit.date = da
        edit.save()
        edit.content = co
        edit.save()
        # cursor =connection.cursor()
        # sql = 'UPDATE cla_1_list SET date = %s, content = %s WHERE id = %s'
        # cursor.execute(sql,a1)
        return render(request, "member/alert.html",{"msg":"수강이 변경되었습니다.",'url':'/home/index'})
    

