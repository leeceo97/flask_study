# /server/Dockerfile
FROM python:3.8

RUN apt-get -y update
RUN apt-get -y install vim

RUN mkdir /server
ADD . /server

WORKDIR /flask_study/flaskr

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install gunicorn

EXPOSE 8000
CMD ["gunicorn", "--bind", "0:8000", "views:app"]