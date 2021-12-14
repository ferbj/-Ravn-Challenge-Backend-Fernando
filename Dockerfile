FROM python:3
RUN apt-get update
RUN apt-get install nano
ENV PYTHONUNBUFFERED 1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code

EXPOSE 80