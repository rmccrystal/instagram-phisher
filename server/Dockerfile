FROM python:3.7.3-stretch

RUN apt-get update -y

COPY requirements.txt .
RUN pip3 install -r requirements.txt

ENV FLASK_RUN_PORT 80
ENV FLASK_RUN_HOST 0.0.0.0
ENV FLASK_APP app.py

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

COPY . .

EXPOSE 80

CMD ["flask", "run"]