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