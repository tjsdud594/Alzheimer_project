# Alzheimer_project
VRAIN은 백엔드 프레임워크 Django 와 오픈소스 데이터베이스인 PostgreSQL을 사용하여 데이터베이스를 구축한다.

# 프로젝트 진행과정
> https://www.notion.so/2021-Innovative-Growth-Course-Team-Five-s-Project-e26a2c0b573e4b2d88236e649b850020

## Requirements
- requirements.txt

## How to runserver?
- 가상환경 생성
``` 
python -m venv django # 원하는 가상환경 이름을 설정
```
- 가상환경 실행
```
 source django/Scripts/activate # Windows
 source django/bin/activate # Mac
```
- 가상환경 실행 확인
```
 where python
```
- 패키지 목록 확인/관리
```
pip list #확인
pip freeze #관리
```
- 패키지 설치
```
pip install -r requirement.txt
```
- 서버 실행
```
python manage.py runserver
```
- 가상환경 비활성화
```
deactivate
```
<!-- ##  -->
<!-- <p>
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
 -->


## Preview
- **main**<br>
 > 서비스 개발 소개
 
![main](https://user-images.githubusercontent.com/84279479/141241124-3014bc7f-f011-4b66-8fb0-18440d155641.gif)


- join/login<br>
![login](https://user-images.githubusercontent.com/84279479/141241709-d0cda9de-86c8-465b-884d-b58dcab55685.gif)

- predict<br>
![predict](https://user-images.githubusercontent.com/84279479/141242115-98447afb-6da0-43f9-be33-a2c5b74a6708.gif)

- mypage<br>
![mypage](https://user-images.githubusercontent.com/84279479/141242012-2d42ae4c-3216-4587-b014-b981f5c47126.gif)
