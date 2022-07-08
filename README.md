# 더배움 백엔드

## 서버 필요 환경
1. Python 3.10 이상
2. Poetry 패키지 매니저 https://python-poetry.org/

## .env
프로젝트 루트에 .env 파일을 생성하여 아래 변수를 입력합니다.

`key=value` 형식으로 각 줄에 변수를 입력합니다.
>`DEBUG` True | False - 개발 모드인지의 여부 
> 
>`SECRET_KEY` 보안을 위한 무작위 코드 - https://miniwebtool.com/django-secret-key-generator/ 에서 생성
> 
>`DB_NAME` 이 프로젝트에 사용되는 mysql DB의 이름
> 
>`DB_USER` mysql 사용자 이름
> 
>`DB_PASSWORD` mysql 비밀번호
> 
>`DB_HOST` mysql 주소
> 
>`DB_PORT` mysql 포트 - 기본 3306

## 서버를 처음 시작하기 전에
`poetry install`

`poetry run python manage.py migrate`

`poetry run python manage.py collectstatic`

## 서버 실행

`poetry run python manage.py runserver`