https://github.com/docker/toolbox/releases

호스트 이름 : 211.110.165.201
포트번호 : 1521
SID  : xe
사용자이름 : bnk01 ~ bnk10
암호 : 1234

java 다운로드 후 설치
http://ihongss.com/zip/java8.zip

sqldeveloper다운로드 후 압축풀기
http://ihongss.com/zip/sqldeveloper.zip

c:/program files/java/jdk8_XXXX 선택 후 확인버튼

오라클 접속 클라이언트 프로그램 다운로드 후 c:/instantclient폴더로 복사
http://ihongss.com/zip/instantclient.zip



import cx_Oracle as oci 
 
#아이디/암호@서버주소:포트번호/SID
conn = oci.connect('bnk01/1234@211.110.165.201:1521/xe')

cursor = conn.cursor()  # cursor 객체 얻기
cursor.execute('SELECT * FROM TBL_BOARD')
data =  cursor.fetchall()

print (type(data))
print(data)