FROM ubuntu:latest

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

ENV FLASK_RUN_PORT 80
ENV FLASK_RUN_HOST 0.0.0.0

EXPOSE 80

ENTRYPOINT ["flask", "app.py"]