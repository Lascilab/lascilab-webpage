# Dockerizing HTCondor
# docker build -t htcondor .
# docker run -it -p 3000:3000 --rm htcondor
FROM 	   ubuntu:14.04
MAINTAINER Riccardo Bucchi <riccardo.bucchi26@gmail.com>
ENV 	   TINI_VERSION v0.9.0

ADD     https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /sbin/tini
RUN	set -ex \
	# CONDOR
	&& apt-get update && apt-get install -y wget procps \
	&& chmod +x /sbin/tini \
	&& echo "deb http://research.cs.wisc.edu/htcondor/ubuntu/stable/ trusty contrib" >> /etc/apt/sources.list \
	&& wget -qO - http://research.cs.wisc.edu/htcondor/ubuntu/HTCondor-Release.gpg.key | apt-key add - \
        && export DEBIAN_FRONTEND=noninteractive \
	&& apt-get update \
	&& apt-get install condor -y --force-yes \
 	&& apt-get install -y nano nodejs nodejs-legacy npm python-pip && pip install supervisor supervisor-stdout \
	# CLEAN
	&& apt-get -y remove wget python-pip \
        && apt-get clean all 

COPY 	supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY    condor_config /etc/condor/condor_config
COPY    run.sh /usr/local/sbin/run.sh

COPY ./tty.js/ /usr/src/app
COPY config.json /tmp/config.json
COPY ejemplos /home/lascilab/ejemplos
WORKDIR /usr/src/app

RUN npm install
RUN useradd -ms /bin/bash lascilab
RUN gpasswd -a lascilab condor
RUN newgrp condor
RUN chmod 777 /usr/local/sbin/run.sh
RUN chown -R lascilab:lascilab /home/lascilab /usr/local/sbin/run.sh /etc/supervisor/conf.d/supervisord.conf
ENV SHELL bash

ENTRYPOINT ["/sbin/tini", "--", "/usr/local/sbin/run.sh"]
