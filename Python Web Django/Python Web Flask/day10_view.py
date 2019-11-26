#flask 사용
from datetime import timedelta
from flask import Flask, render_template, redirect, request, session
import day10_model as md
#**
app = Flask(__name__)
app.secret_key = b'fefe#$$%4_F#f3f33fA'
#**
@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=5)

member = md.memberModel()
board = md.boardModel()
#member1 대신에 board를 넣어줬다

## 게시판 내용 - GET
## http://127.0.0.1:5000/boardc?no=5
## http://127.0.0.1:5000/boardc

#**


@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/login", methods=['GET'])
def login_get():
    return render_template('login.html')

@app.route("/login", methods=['POST'])
def login_post():
    a = request.form['id']  
    b = request.form['pw']

    a1 = [a, b] # 아이디와 암호 값을 a1리스트에 추가
    mone = member.login(a1)
    # print(mone)
    if not mone :
        print("로그인 실패")
    else:
        print("로그인 성공")  
        session['userid'] = mone[0]  # 자료형 딕셔너리 {"userid":"a"}
        session['username'] = mone[1] #{"userid":"a", "username":"이름"}
    return redirect("index")

@app.route('/logout', methods=['GET'])
def logout():
   session.pop('userid', None)
   session.pop('username', None)
   return redirect('index')     

@app.route("/delete", methods=['GET'])
def member_delete():
    return render_template('memberout.html')

@app.route("/delete", methods=['POST'])
def member1_delete():
    id = session['userid'] 
    pw = request.form['pw']
    pw1 = request.form['pwtest']
    if pw == pw1:   
        send1 = [id, pw]
        member.delete(send1)
    return redirect('logout')

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
    board.write(a1)
    return redirect('index')

@app.route("/board", methods=['GET'])#board라고 보면되겠다
def board_get():
    no = [ request.args.get('type', 'brd_title'), request.args.get('text', '') ]
    data = board.boardlist(no)
    session['boardhit'] = 1
    return render_template('board.html', key=data)

@app.route("/boardc", methods=['GET'])
def boardc_get():
    no = [ request.args.get('no', 0) ] # 리스트로 만듬 => [7]

    if 'boardhit' in session:
        if session['boardhit'] == 1:
            board.boardhit(no) #조회수 1증가시키기
            session['boardhit'] = 0

    one = board.boardone(no)   # 상세내용 (1,2,3,4,..)
    prev = board.boardprev(no) # 이전글 (1) prev[0]
    next = board.boardnext(no) # 다음글 (5) next[0]
    return render_template('boardc.html', key=one, prev=prev, next=next)

@app.route("/boardd", methods=['GET'])
def boarddelete_get():
    no = [ request.args.get('no', 0) ]
    board.boarddelete(no)
    return redirect('board') #127.0.0.1:5000/board
    #render_template('board.html', key=data)

@app.route("/boarde", methods=['GET'])#board라고 보면되겠다
def boarde_get():
    no = [ request.args.get('no', 0) ] # 리스트로 만듬 => [7]
    one = board.boardone(no)
    render_template('boarde.html', key=one)
    return render_template('boarde.html', key=one)

@app.route("/boarde", methods=['POST'])#board라고 보면되겠다
def boarde_post():
    a = request.form['no']
    b = request.form['ti']
    c = request.form['co']
    a1 = [a,b,c]
    board.boardupdate(a1)
    return redirect("boardc?no=" + str(a))



if __name__ == '__main__':
    app.run(debug=True)