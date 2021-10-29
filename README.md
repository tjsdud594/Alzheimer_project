# Alzheimer_project

<p>
- ref 
https://wikidocs.net/53383
</p>

<p>
- Backend 진행상황: Django 기본틀 <br>
    - html 연결 <br>
    - model -> function의 Test model만 생성 <br>
    - admin : root2, 1234 a@a.com <br>
<br>
- PostgreSQL <BR>
    - https://www.enterprisedb.com/downloads/postgres-postgresql-downloads <br>
    - PostgreSQL <br>
    - Backend/settings.py <br>
        DATABASES = { <br>
            'default': { <br>
                'ENGINE': 'django.db.backends.postgresql', <br>
                'NAME': 'metrisdata',   >> 생성한 PostgreSQL DB 이름 <br>
                'USER': 'postgres',     >> 생성한 PostgreSQL DB user 이름 <br>
                'PASSWORD': 'pass1234', >> 생성한 PostgreSQL DB 패스워드 <br>
                'HOST': '127.0.0.1', <br>
                'PORT': '5432', <br>
            } <br>
        }
    <br>
    > python manage.py migrate <br>
     <br>
    - 새로운 DB에 연결 후엔 superuser 생성을 새로 해줘야 함 <br>
    - python manage.py createsuperuser <br>
     <br>
<br>
</p>
- .gitattributes : 임시모델 weight 저장 값(10/27 기준)
