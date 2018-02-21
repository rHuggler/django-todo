FROM python:3.6.4-alpine

WORKDIR /usr/src/app

COPY requirements.txt .

RUN apk update && \
 apk add postgresql-libs && \
 apk add --virtual .build-deps gcc python3-dev musl-dev postgresql-dev

RUN pip install --no-cache-dir -r requirements.txt && \
 apk --purge del .build-deps

COPY . .