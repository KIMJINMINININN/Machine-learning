# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

from django.db import connection

def index(request):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM board")
    row = cursor.fetchall()
    print(row)
    return render(request,'board/index.html', {'data': row})

def list(request):
    return render(request,'board/list.html')

@csrf_exempt
def write(request):
    if request.method == "GET":
        return render(request,'board/write.html')

    elif request.method == "POST":
        ti = request.POST['ti']
        co = request.POST['co']
        img = request.FILES['img'] #파일을 첨부하여서 받는방법
        wr = request.POST['wr']
        a1 = [ti, co, img.read(), wr]
        cursor = connection.cursor()
        sql = "INSERT INTO BOARD(BRD_NO, BRD_TITLE, BRD_CONTENT, BRD_IMG, BRD_WRITER, BRD_HIT, BRD_DATE) VALUES(SEQ_BOARD_NO.NEXTVAL,%s,%s,%s,%s,1,SYSDATE)"
        # cursor.execute(sql,ti=a1[0], co=a1[1], img=a1[2], wr=a1[3])
        cursor.execute(sql, a1)

        # iwant = 5
        # sql1 = "SELECT * FROM BOARD WHERE > %d"
        # t = cursor.execute(sql1, iwant)
        # print(t)
        return redirect("/board/index")

def edit(request):
    return render(request,'board/edit.html')

def delete(request):
    return render(request,'board/delete.html')