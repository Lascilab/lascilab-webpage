FROM node:6-slim

ARG VERSION=3.2.0
RUN npm install --global gitbook-cli &&\
	gitbook fetch ${VERSION} &&\
	npm cache clear &&\
	rm -rf /tmp/*
RUN mkdir -p /srv /srv/html

RUN apt-get update && apt-get install -y git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

#WORKDIR /srv/gitbook
#VOLUME /srv/gitbook /srv/html

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY package.json /usr/src/app/
RUN npm install
COPY . /usr/src/app
CMD [ "npm", "start" ]
