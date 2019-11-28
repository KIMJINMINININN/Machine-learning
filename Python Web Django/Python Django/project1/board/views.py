# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from base64 import b64encode
from django.db import connection

def index(request):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM board")
    row = cursor.fetchall()
    return render(request,'board/index.html', {'data': row})

def list(request):
    cursor = connection.cursor()
    sql = "SELECT * FROM board ORDER BY BRD_NO DESC"
    cursor.execute(sql)
    rows = cursor.fetchall()
    return render(request,'board/list.html', {"data":rows})

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

@csrf_exempt
def content(request):
    cursor = connection.cursor()
    no = request.GET.get("no", 0)
    sql = "SELECT * FROM BOARD WHERE BRD_NO = %s"
    cursor.execute(sql, [no])
    one = cursor.fetchone()
    if one[6]:
        data = one[6].read()
        image = b64encode(data).decode("utf-8")
    else :
        file = open("./static/img/default.png", "rb")
        data = file.read()
        image = b64encode(data).decode("utf-8")
    return render(request,'board/content.html', {"one":one, "image":image})

@csrf_exempt
def edit(request):
    if request.method == "GET":
        no = request.GET.get("no",0)
        print(no)
        cursor = connection.cursor()
        sql = "SELECT * FROM BOARD WHERE BRD_NO = %s"
        cursor.execute(sql, [no])
        one = cursor.fetchone()
        print(one)
        return render(request,'board/edit.html',{"one":one})

    elif request.method == "POST":
        no = request.POST['no']
        ti = request.POST['ti']
        co = request.POST['co']
        a1 = [ti, co, no]
        cursor = connection.cursor()
        sql = "UPDATE BOARD SET BRD_TITLE=%s, BRD_CONTENT=%s WHERE BRD_NO =%s"
        cursor.execute(sql, a1)
        return redirect("/board/list")

@csrf_exempt
def delete(request):
    print('aaa')
    if request.method == "POST":
        no = request.POST.get("no", 0)
        print(no)
        cursor = connection.cursor()
        sql = "DELETE FROM BOARD WHERE BRD_NO=%s"
        cursor.execute(sql, [no])
        return redirect('/board/list')