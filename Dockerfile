FROM ubuntu:18.04

MAINTAINER nikolas adaloglou "n.adaloglou@hotmail.com"

RUN apt-get update -y && \  
    apt-get install -y python3-pip python3-dev

COPY ./requirements.txt /requirements.txt

WORKDIR /

RUN pip3 install -r requirements.txt

COPY . /


