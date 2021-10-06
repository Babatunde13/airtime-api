FROM python:3.9-alpine

###postgress dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev


##initialize the docker working directory
RUN mkdir /airtime-api

WORKDIR /airtime-api

COPY requirements.txt /airtime-api

RUN python -m pip install --no-cache-dir -r requirements.txt

COPY . /airtime-api

RUN flask db upgrade
    
CMD flask run --host=0.0.0.0 --port=5000
