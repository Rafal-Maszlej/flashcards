FROM python:3.7

WORKDIR /backend

RUN apt-get update -q
RUN apt-get install -yq netcat

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000
