#flask 사용
from flask import Flask, render_template, redirect, request 
import cx_Oracle as oci

app = Flask(__name__)

#127.0.0.1:5000/
@app.route("/")
def home():
    a1=[1,2,3,4,5,6,7,8,9,10]
    return render_template('home.html',title="홈화면", num=8, a1=a1)
#{{이안에 title, num이라는 값들을 넣어서 보내어주면 그것들을 화면에 출력시킨다}}
#render_template를 사용하여서 어떠한 파일을 직접 불러와준다
#127.0.0.1:5000/index
@app.route("/index")
def index():
    return render_template('index.html')

#주소창으로 들어갈때에
@app.route("/join", methods=['GET'])
def join():
    return render_template('join.html')

@app.route("/join", methods=['POST'])
def join_post():
    conn=oci.connect("admin/1234@192.168.99.100:32764/xe", encoding="utf-8")
    cursor=conn.cursor()

    id = request.form['id'] #'id' input type="text" name="id"
    pw = request.form['pw']
    pw1 = request.form['pw1']
    name = request.form['name']
    tel1 = request.form['tel1']
    tel2 = request.form['tel2']
    tel3 = request.form['tel3']
    email1 = request.form['email1']
    email2 = request.form['email2']
    a1 = [id,pw,pw1,name,tel1,tel2,tel3,email1,email2]

    sql = "INSERT INTO INFO VALUES(:1,:2,:3,:4,:5,:6,:7,:8,:9)"
    cursor.execute(sql,a1)
    conn.commit()
    print(a1)
    #보여주는 부분이 아니다
    #사용자가 입력한 정보를 받아서
    #DB에 넣고 다른페이지로 전환시킴
    return redirect('index')

@app.route("/login", methods=['GET'])
def login_get():
    return render_template('login.html')

@app.route("/login", methods=['POST'])
def login_post():
    return "페이지 이동"

@app.route("/ex01", methods=['GET'])
def ex01():
    return render_template('ex01.html')
#정보를 숨겨서 보낼땐 POST, 숨기지 않아도되면 GET으로 가능
@app.route("/ex01_1", methods=['GET'])
def ex01_1():
    n1 = int(request.args.get('n1',0))
    n2 = int(request.args.get('n2',0))
    n3 = int(request.args.get('n3',0))
    a2 = [n1, n2, n3, (n1+n2+n3)]
    return render_template('ex01_1.html',a2=a2)

@app.route("/ex02", methods=['GET'])
def ex02():
    return render_template('ex02.html')

@app.route("/ex02_1", methods=['GET'])
def ex02_1():
    n1 = int(request.args.get('n1',0))
    n2 = []
    n3 = []
    for i in range(1,10):
        n2.append(i*n1)
        n3.append("{}*{}={}".format(n1,i,n2[i-1]))
    return render_template('ex02_1.html',n3=n3)
if __name__ == '__main__':
    app.run(debug=True)

#크롬에서 127.0.0.1:5000 
#1.flask 사용해보기
#2.