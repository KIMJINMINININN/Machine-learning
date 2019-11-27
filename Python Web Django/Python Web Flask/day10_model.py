import cx_Oracle as oci

class memberModel:
    def __init__(self):
        self.conn = oci.connect('admin/1234@192.168.99.100:32764/xe', encoding="utf-8")
        self.cursor = self.conn.cursor()

    def join(self, data):
        sql = "INSERT INTO MEMBER(MEM_ID, MEM_PW, MEM_NAME, MEM_TEL, MEM_EMAIL, MEM_DATE) VALUES(:1,:2,:3,:4,:5,SYSDATE)"
        self.cursor.execute(sql, data)
        self.conn.commit()

    def memberlist(self):
        sql = "SELECT * FROM MEMBER ORDER BY MEM_ID ASC"
        self.cursor.execute(sql)
        mlist = self.cursor.fetchall()
        return mlist
    #**
    def login(self, data):
        sql = "SELECT * FROM MEMBER WHERE MEM_ID=:1 AND MEM_PW=:2"
        self.cursor.execute(sql, data)
        mone = self.cursor.fetchone() #결과값 받기 :  튜플 (   )
        return mone
    
    def delete(self, data):
        sql = "SELECT * FROM MEMBER WHERE MEM_ID=:1 AND MEM_PW=:2"
        self.cursor.execute(sql, data)
        mone = self.cursor.fetchone() #결과값 받기 :  튜플 (  )
        if mone :
            sql = "DELETE FROM MEMBER WHERE MEM_ID=:id"
            self.cursor.execute(sql, id=data[0])
            self.conn.commit()
            return 1
        else:
            return 0 

class boardModel:
    def __init__(self):
        self.conn = oci.connect('admin/1234@192.168.99.100:32764/xe', encoding="utf-8")
        self.cursor = self.conn.cursor()

    def write(self, data):
        sql = "INSERT INTO BOARD(BRD_NO, BRD_CONTENT, BRD_TITLE, BRD_WRITER, BRD_HIT, BRD_DATE) VALUES(SEQ_BOARD_NO.NEXTVAL,:1,:2,:3,999,SYSDATE)"
        self.cursor.execute(sql, data)
        self.conn.commit()

    def boardlist(self, data):
        if data[0] == 'brd_title':
            sql = "SELECT * FROM BOARD WHERE BRD_TITLE LIKE '%'|| :text ||'%' ORDER BY BRD_NO DESC"
        elif data[0] == 'brd_content' :
            sql = "SELECT * FROM BOARD WHERE BRD_CONTENT LIKE '%'|| :text ||'%' ORDER BY BRD_NO DESC"
        elif data[0] == 'brd_writer' :
            sql = "SELECT * FROM BOARD WHERE BRD_WRITER LIKE '%'|| :text ||'%' ORDER BY BRD_NO DESC"    
        self.cursor.execute(sql, text=data[1])  # SQL 문장 실행
        mlist = self.cursor.fetchall() #결과값 받기 : [(),(),()]
        return mlist
    #**
    def boardone(self, data):
        sql = "SELECT * FROM BOARD WHERE BRD_NO=:1"
        self.cursor.execute(sql, data)  # SQL 문장 실행
        one = self.cursor.fetchone() #결과값 받기 : (a,a,a,a,a,a)
        return one

    def boardhit(self, data):
        sql = "UPDATE BOARD SET BRD_HIT=BRD_HIT+1 WHERE BRD_NO=:1"
        self.cursor.execute(sql, data)
        self.conn.commit()

    def boardnext(self, data):
        sql = "SELECT NVL(MIN(BRD_NO),0) FROM BOARD WHERE BRD_NO < :1"
        self.cursor.execute(sql, data)  # SQL 문장 실행
        one = self.cursor.fetchone() #결과값 받기 : (7)
        return one

    def boarddelete(self, data):
        sql = "DELETE FROM BOARD WHERE BRD_NO=:1" 
        self.cursor.execute(sql, data)    
        self.conn.commit()
    
    def boardprev(self, data) :
        sql = "SELECT NVL(MIN(BRD_NO),0) FROM BOARD WHERE BRD_NO > :1"
        self.cursor.execute(sql, data)  # SQL 문장 실행
        one = self.cursor.fetchone() #결과값 받기 : (7)
        return one

    def boardupdate(self, data) :
        sql = "UPDATE BOARD SET BRD_TITLE=:t, BRD_CONTENT=:c WHERE BRD_NO=:n"
        self.cursor.execute(sql, n=data[0], t=data[1], c=data[2])  # SQL 문장 실행
        self.conn.commit()
    


