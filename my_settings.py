# my_sttings.py
DATABASES = {
    'default': {
        'ENGINE' : 'django.db.backends.mysql', #1 사용할엔진
        'NAME' : 'name_of_database', #2 연동할 MYSQL 데이터베이스 이름
        'USER' : 'root', #3 DB접속 계정명
        'PASSWORD' : 'password', #4 해당 DB접속 계정 비밀번호
        'HOST' : 'localhost', #5 실제 DB주소
        'PORT' : '3306' #6 포트번호
    }
}
# 시크릿키 : 기존 settings.py 에 있던거
SECRET_KEY = 'django-insecure-u1^xz@$9k^%!l@#srm3g#x!r4(6pw3mfr!3+0wuxbn^i+ov5hq'