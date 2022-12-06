FROM python:3.7

WORKDIR /image-api

COPY requirements.txt .

RUN pip3 install -r requirements.txt

ADD src .