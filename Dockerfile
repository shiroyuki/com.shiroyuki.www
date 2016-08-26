FROM debian:latest
MAINTAINER Juti Noppornpitak <jnopporn@shiroyuki.com>

# Retrieve the list
RUN apt-get update

# Python 2.7
RUN apt-get install -y python-dev python-pip mongodb-dev
RUN apt-get install -y libtiff5-dev libjpeg-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk

# Clean up
RUN apt-get clean
RUN apt-get autoclean
RUN apt-get autoremove -y

RUN pip install sphinx sphinxcontrib-actdiag sphinxcontrib-blockdiag sphinxcontrib-seqdiag

ADD . /opt/www

WORKDIR /opt/www

RUN pip install -r requirements.txt

CMD make web && python server.py
