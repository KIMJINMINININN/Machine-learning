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

    def getlogin(self):
        sql = "SELECT MEM_ID, MEM_PW FROM MEMBER"
        self.cursor.execute(sql)
        mlist = self.cursor.fetchall()
        return mlist
class boardModel:
    def __init__(self):
        self.conn = oci.connect('admin/1234@192.168.99.100:32764/xe', encoding="utf-8")
        self.cursor = self.conn.cursor()

    def write(self, data):
        sql = "INSERT INTO BOARD(BRD_NO, BRD_CONTENT, BRD_TITLE, BRD_WRITER, BRD_HIT, BRD_DATE) VALUES(SEQ_BOARD_NO.NEXTVAL,:1,:2,:3,999,SYSDATE)"
        self.cursor.execute(sql, data)
        self.conn.commit()

    def boardlist(self):
        sql = "SELECT * FROM BOARD ORDER BY BRD_NO ASC"
        self.cursor.execute(sql)
        mlist1 = self.cursor.fetchall()
        return mlist1