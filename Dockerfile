FROM python:3.7

WORKDIR /image-api

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src/ .