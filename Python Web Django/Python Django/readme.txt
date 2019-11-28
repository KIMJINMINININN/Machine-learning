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

settings.py 
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

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
-> 6가지가있어야한다

$ python manage.py check
$ python manage.py makemigrations
$ python manage.py migrate <= DB에 반영
->하게된다면 DB에 Django와 Auth에 관련된 테이블이 나타게된다
