----------------------------------------------------------------------------------------------------------------------------------------------
20191205
- docker 명령어
docker images : 이미지 확인

docker pull 이미지 : 다운로드

docker rmi 이미지아이디 : 이미지삭제

docker rm 컨테이너아이디 : 컨테이너삭제

docker run --name ~

docker start 컨테이너이름
docker attach 컨테이너이름

docker cp 파일이름 컨테이너이름:경로 : 피시에 있는 파일을 docker안으로 복사하기

docker commit CONTAINER_name docker_id/images_NAME : 도커 컨테이너 로컬 이미지 저장

docker push docker_id/images_NAME

-컨테이너 삭제 하기
docker stop crawling : 멈추고
docker rm crawling : 컨테이너 삭제
docker run --rm --name crwaling -itd -u vscode -p 8888:8888 -p 8088:8088 -p 6006-6015:6006-6015 -e JUPYTER_RUN=yes mrsono0/devremotecontainers:anaconda3
-컨테이너실행 및 저장
docker run --rm --name crawling -itd -u vscode -p 8888:8888 -p 8088:8088 -p 6006-6015:6006-6015 -e JUPYTER_RUN=yes vmelove/crawling
docker commit crawling vmelove/crawling
192.168.99.100:8088 -> vs code 실행

ㅇdocker logs --tail 30 crawling
-> http://192.168.99.100:8888/?token=6776947941134d4dfcbb40968c52e8c84bbb6acafda2bd93 -> 192.168.99.100넣어서 실행 하면 쥬피터 노트북 실행

ㅇjupyter lab --port 8898 -> jupyter lab을 실행시키기(이것은 내 PC안에 잇는것)

ㅇ프로토콜: 컴퓨터가 사용하는 언어를 사용하여서 소통하는것
HTTP 프로토콜
FTP 프로토콜

ㅇDOM
-> 브라우저에서 데이터를 읽어들이는 구조를 의미한다. 이진트리알고리즘을 보통 사용한다.
-> 브라우저에 있는데이터

ㅇmaven
https://jeong-pro.tistory.com/168(java 갑자기 생각나서)

ㅇcookies
-> 브라우저에 저장되는 cookies, 서버 메모리에 저장됨 session

ㅇdocker push vmelove/crawling
-> push 하기
ㅇdocker push vmelove/crawling
-> pull 하기
----------------------------------------------------------------------------------------------------------------------------------------------
20191206 메모
ㅇcss는 DOM을 사용하는데 이진트리알고리즘을 사용한다

ㅇ분석을 하기위해서는 분석알고리즘뿐만아니라, 컴퓨터를 사용하여 대화해야하기때문에 컴퓨터언어에 익숙해져야한다

ㅇpython class, def
----------------------------------------------------------------------------------------------------------------------------------------------
20191209 crawling
ㅇdocker와 컴퓨터의 환경을 mount시켜줄수있다
ㅇcss selector (id, tag, class 방식 3가지)

ㅇsoup.find() 함수로 원하는 부분 지정
-> get.text()는 태그안의 값을 가져오게된다

ㅇcss의 스타일에서 .은 클래스를 의미한다

ㅇrequests VS urllib
-객체를 만드는 방법의 차이
--requests : 딕셔너리 urllib : 바이너리 형태
--requests 요청 메소드를 명시하지만 urllib는 데이텅 여부에 따라 GET요청과 POST요청 구분된다
--requests는 에러를 띄우지만 urllib는 에러 발생

ㅇheader를 보면 cookies가 보인다. ID의 키값으로 브라우저는 사용자가 누구인지 판단하게된다
-- 내가 docker에 vscode에서 더 많은 부분을 사용하고싶을때 -- 
ㅇsudo code-server --install-extension /home/vscode/파일명
-> 내가 필요한것 다운받아서 사용하기
ㅇdocker exec -it crawling bash
-> docker안으로 들어가기
ㅇsudo code-server --install-extension /home/vscode/*.vsix
-> docker 안에들어가서 install하기
ㅇdocker cp ./view.py crawling:/home/vscode/notebooks/
-> 내 컴퓨터에서 docker안으로 파일을 집어넣기
ㅇdocker cp crawling:/home/vscode/notebooks/ ./view.py
-> docker에서 컴퓨터로 집어넣기
ㅇReply - Add Link as Attachment

ㅇdocker run --rm --name crawling -itd -u vscode -p 8888:8888 -p 8088:8088 -p 6006-6015:6006-6015 -e JUPYTER_RUN=yes -v 
D:\PNU_201912\crawling:/home/vscode/crawling mrsono0/devremotecontainers:anaconda3

ㅇpip install bs4
-> bs4 설치
----------------------------------------------------------------------------------------------------------------------------------------------
20191210
-컨테이너실행 및 저장
docker run --rm --name crawling -itd -u vscode -p 8888:8888 -p 8088:8088 -p 6006-6015:6006-6015 -e JUPYTER_RUN=yes vmelove/crawling
docker commit crawling vmelove/crawling
192.168.99.100:8088 -> vs code 실행

ㅇsoup.selector -> beautifulsoup4에서 사용하는 css.selector

ㅇ크롬의 #copy selector를 사용하면 그부분의 selector를 사용할수있다


