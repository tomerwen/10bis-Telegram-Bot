#syntax=docker/dockerfile:1

FROM python:latest
#install dependencies

RUN pip3 install python-telegram-bot --upgrade

#setup work enviorment
RUN mkdir app
WORKDIR /app
COPY . ./
#create the directory for the vouchers
RUN mkdir Vouchers

#start the application
CMD ["python","./10bisbot.py"]