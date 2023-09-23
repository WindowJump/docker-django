FROM python:3.11.5-alpine3.18

COPY requirements.txt /temp/requirements.txt
COPY main_dir /main_dir
WORKDIR /main_dir
EXPOSE 8000

RUN apk add python3-dev postgresql-client build-base postgresql-dev

RUN pip install -r /temp/requirements.txt

RUN adduser --disabled-password admin

USER admin
