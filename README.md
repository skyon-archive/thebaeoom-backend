# 더배움 백엔드

## 서버 필요 환경
1. Python 3.10 이상
3. MySQL 5.7

## .env
프로젝트 루트에 .env 파일을 생성하여 아래 변수를 입력합니다. 

메모장으로 작업하는 경우 반드시 저장 시 인코딩 옵션을 "ANSI"로 설정해야 합니다.

`key=value` 형식으로 각 줄에 변수를 입력합니다.

`.env.example` 파일을 참고하세요.
>`DEBUG` True | False - 개발 모드인지의 여부 (개발 중이 아닐 경우에는 False여야 합니다.)
>
>`FRONTEND_URL` 프론트엔드 서버의 주소(맨 끝 슬래시(/) 제외) - ex) http://localhost:3000, https://thebaeoom.com
>
>`SECRET_KEY` 보안을 위한 무작위 코드 - https://miniwebtool.com/django-secret-key-generator/ 에서 생성
> 
>`DB_NAME` 이 프로젝트에 사용되는 mysql DB의 이름
> 
>`DB_USER` mysql 사용자 이름
> 
>`DB_PASSWORD` mysql 비밀번호
> 
>`DB_HOST` mysql 주소(http:// 제외, 맨 끝 슬래시(/) 제외)
> 
>`DB_PORT` mysql 포트 - 기본 3306

## mysql db 생성

`create database thebaeoom charset utf8 collate utf8_unicode_ci;`

## 서버를 처음 시작하기 전에
`pip install -r requirements.txt`

`python manage.py migrate`

`python manage.py collectstatic`

## 콘솔 유저 생성
`python manage.py createsuperuser` - 이메일 주소 입력 불필요함

## 서버 실행
`python manage.py runserver 0.0.0.0:8000 --insecure` - 기본 포트 8000

`python manage.py runserver 0.0.0.0:<port> --insecure` - < port >에 서버가 실행될 포트 숫자 입력 ex) poetry run python manage.py runserver 8080

`/admin`에서 콘솔 접속 가능

## 기타

현재 static/과 uploads/ 폴더가 django를 통해 호스팅되도록 설정되어 있으나 보안 상 안전하지 않습니다.

두 주소에 대해서는 nginx 등을 통해 정적 파일을 호스팅하도록 설정하는 것을 권장합니다.