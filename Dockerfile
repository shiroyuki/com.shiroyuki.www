FROM python:latest
MAINTAINER Juti Noppornpitak <jnopporn@shiroyuki.com>

ENV revision 20170322.2212
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

ADD ./requirements-longer-inst.txt ${app_path}/requirements-longer-inst.txt
RUN pip3 install -r requirements-longer-inst.txt

ADD ./requirements.txt ${app_path}/requirements.txt
RUN pip3 install -r requirements.txt

ADD . ${app_path}

ENTRYPOINT ["python", "/usr/local/bin/g3"]
CMD ["http"]

EXPOSE 8000
