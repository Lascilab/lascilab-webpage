# Base Image Name and Tag
FROM python:2.7

ENV PYTHONUNBUFFERED 1

RUN mkdir /webpage
WORKDIR /webpage
ADD . /webpage/
RUN pip install -r requirements.txt
