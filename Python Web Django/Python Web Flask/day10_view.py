#flask 사용
from flask import Flask, render_template, redirect, request 
import day10_model as md
app = Flask(__name__)
member = md.memberModel()
member1 = md.boardModel()

@app.route("/login", methods=['GET'])
def login_get():
    return render_template('login.html')

@app.route("/login", methods=['POST'])
def login_post():
    data = member.getlogin()
    id = request.form['id']
    pw = request.form['pw']
    # for a in data:
    return render_template('index.html')
# @app.route("/logintest", methods=['POST'])
# def logintest():

@app.route("/join", methods=['GET'])
def join():
    return render_template('join.html')

@app.route("/join", methods=['POST'])
def join_post():
    id = request.form['id'] #'id' input type="text" name="id"
    pw = request.form['pw']
    # pw1 = request.form['pw1']
    name = request.form['name']
    tel1 = request.form['tel1']
    tel2 = request.form['tel2']
    tel3 = request.form['tel3']
    email1 = request.form['email1']
    email2 = request.form['email2']
    a1 = [id,pw,name,(tel1 + "-" + tel2 + "-" + tel3), (email1+"@"+email2)]
    member.join(a1)
    #join함수는 리스트에서 문자열로 바꾸어주는 방법
    #보여주는 부분이 아니다
    #사용자가 입력한 정보를 받아서
    #DB에 넣고 다른페이지로 전환시킴
    # return ' '.join(a1)
    return redirect('join_ok')

@app.route("/join_ok", methods=['GET'])
def join_ok():
    return render_template('join_ok.html')

@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/memberlist", methods=['GET'])
def memberlist():
    data = member.memberlist()
    print(data)
    return render_template('memberlist.html', key=data)

@app.route("/boardw", methods=['GET'])
def boardw():
    return render_template('boardw.html')

@app.route("/boardw", methods=['POST'])
def boardw_post():
    a = request.form['ti']
    b = request.form['co']
    c = request.form['wr']
    #day10_model1.py파일에 boardModel 클래스 생성후 write메소드 호출
    a1 = [a,b,c]
    member1.write(a1)
    return redirect('index')

@app.route("/boardlist", methods=['GET'])
def board_get():
    data = member1.boardlist()
    print(data)
    return render_template('boardlist.html', key=data)

if __name__ == '__main__':
    app.run(debug=True)