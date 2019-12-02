Django 설정방법

pip install django 설치(conda install django)]

$ django-admin startproject django1 <= django1 프로젝트 생성

$ cd django1 <= 프로젝트 폴더로 이동

$ django-admin startapp blog <= 앱 생성

$ python manage.py runserver <= 서버 구동

static, templates 폴더를 만들어준다

모든 폴더들은 상위폴더를 거치게되고, 상위폴더를 거친후에 하위폴더로 넘어가게된다
URL을 설정하여서 만들어주는 방법
project1의 urls -> board의 urls 이렇게 거쳐서 url이 간다

# DB 설정 방법
settings.py에 가서
-> 'DIRS': [os.path.join(BASE_DIR, 'templates')] 라고 설정해주기
-> STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')] 설정
Oracle로 사용하여야하기때문에 settings의 DataBase 설정을 바꾸어준다
DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),

        'ENGINE' : 'dango.db.backends.oracle',
        'NAME' : 'xe',
        'USER' : 'admin',
        'PASSWORD' : '1234',
        'HOST' : '192.168.99.100',
        'PORT' : '32764'
    }
}

$ python manage.py check
$ python manage.py makemigrations
$ python manage.py migrate <= DB에 반영
->하게된다면 DB에 Django와 Auth에 관련된 테이블이 나타게된다

#Session에 대한 정의
session이라는것은 전역변수라고 생각할수있다.
한 페이지에서 다른 페이지로 옮겨간다면 그순간에 데이터는 소멸되는데
그 소멸되는 데이터를 저장하여서 다른곳에서 사용하고싶다면
session[]에 넣어서 사용하여야한다. Django View에서는 request.sessions[''] 형식으로 사용하여야하며
html은 {{ request.session.login }}이라는 형식을 사용한다
request.sessions['userid'] = a 는 자료형 딕셔너리 {"userid":"a"} 형태로 데이터가 입력되게된다
웹페이지에서는 다른페이지로 옮겨갈대는 항상 세션을 사용하여서 데이터를 저장해주어야 그 데이터를
보존하여서 다른곳에서 사용할수있다.

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
-> 6가지가있어야한다

#model 추가방법
->'shop'을 INSTALLED_APPS에 추가해준다
$ python manage.py check
$ python manage.py makemigrations
$ python manage.py migrate <= DB에 반영
$ python manage.py createsuperuser <= admin 암호 변경

#(admin 사용법)
from django.contrib import admin
# Register your models here.
from .models import Item
admin.site.register(Item)
-> models의 Item의 클래스를 admin에서 사용할수있도록 해준다

#Django model 사용방법
Django는 디폴트로 모든 Django 모델 클래스에 대해 "objects" 라는 Manager (django.db.models.Manager) 객체를 자동으로 추가한다 (이 objects라는 이름을 변경할 수도 있지만, 대부분 그대로 사용한다). Django 에서 제공하는 이 Manager를 통해 특정 데이타를 필터링 할 수도 있고 정렬할 수도 있으며 기타 여러 기능들을 사용할 수 있다.
ㅇINSERT
save() : INSERT문과 똑같은 결과를 나타내낸다
ㅇSELECT
데이타를 읽어오기 위해서는 Django 모델의 Manager 즉 "모델클래스.objects" 를 사용한다. 예를 들어, Feedback 이라는 모델의 경우 "Feedback.objects" 를 사용한다 
    (객체명이 아니라 클래스명을 사용함에 주의).
all() : 테이블 데이타를 전부 가져오기 위해서는 Feedback.objects.all() 과 같이 all() 메서드를 사용한다. 다음은 Feedback 테이블의 모든 데이타의 id와 name 컬럼을 출력하는 예이다.
get() : 하나의 Row만을 가져오기 위해서는 get() 메서드를 사용한다. 예를 들어, 아래는 Primary Key (일반적으로 id 컬럼)가 1인 row를 가져온다.
filter() : 특정 조건에 맞는 Row들을 가져오기 위해서는 filter() 메서드를 사용한다. 예를 들어, 아래는 name 필드가 Kim 인 데이타만 가져온다.
exclude() : 특정 조건을 제외한 나머지 Row들을 가져오기 위해서는 exclude() 메서드를 사용한다. 예를 들어, 아래는 name 필드가 Kim이 아닌 데이타만 가져온다.
count() : 데이타의 갯수(row 수)를 세기 위해 count() 메서드를 사용한다.
order_by() : 데이타를 키에 따라 정렬하기 위해 order_by() 메서드를 사용한다. order_by() 안에는 정렬 키를 나열할 수 있는데, 앞에 -가 붙으면 내림차순이다. 아래는 id를 기준으로 올림차순,
    createDate로 내림차순으로 정렬하게 된다.
distinct() : 중복된 값은 하나로만 표시하기 위해 distinct() 메서드를 사용한다. SQL의 SELECT DISTINCT 와 같은 효과를 낸다. 아래는 name필드가 중복되는 경우 한번만 표시하게 된다.
first() : 데이타들 중 처음에 있는 row만을 리턴한다. 아래는 name필드로 정렬했을 때 처음 row를 리턴한다.
last() : 데이타들 중 마지막에 있는 row만을 리턴한다. 아래는 name필드로 정렬했을 때 마지막 row를 리턴한다.
ㅇUPDATE
fb = Feedback.objects.get(pk=1)
fb.name = 'Park'
fb.save()
-> 객체를 불러와서 저장시킨후, 이름을 변경하고 다시 save
ㅇDELETE
fb = Feedback.objects.get(pk=2)
fb.delete()
-> 마찬가지로 객체 불러와서 자장시키고, 그 객체를 delete해주어서 삭제해주기