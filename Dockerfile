FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . /app

RUN chmod 777 /app/production.sh

CMD /app/production.sh