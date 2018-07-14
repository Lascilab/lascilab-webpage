# Base Image Name and Tag
FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN mkdir /webpage
ADD . /webpage
WORKDIR /webpage
RUN pip install -r prod_req.txt
