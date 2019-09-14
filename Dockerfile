FROM python:3.6
ADD . /home/spider
RUN mkdir /home/download
RUN pip install scrapy
RUN pip install fake-useragent
RUN pip install pymongo
RUN pip install Logbook
RUN pip install pillow
WORKDIR /home/spider