FROM python:latest
MAINTAINER Juti Noppornpitak <jnopporn@shiroyuki.com>

ENV app_path /opt/app

# Retrieve the list
RUN apt-get update

# Python 3
RUN apt-get install -y libtiff5-dev libjpeg-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev

# Clean up
RUN apt-get clean
RUN apt-get autoclean
RUN apt-get autoremove -y

RUN mkdir -p ${app_path}

WORKDIR ${app_path}

ADD . ${app_path}
RUN pip3 install -r requirements.txt

CMD make web && python server.py
