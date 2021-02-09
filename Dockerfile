FROM python:3.8-slim

RUN cp /usr/share/zoneinfo/Europe/Moscow /etc/localtime && \
    echo "Europe/Moscow" > /etc/timezone && \
    date

COPY ./requirements.txt .
RUN pip install -r requirements.txt

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . .

EXPOSE 8000:8000