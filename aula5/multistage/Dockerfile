#----------------------
#------  Stage 1  -----
FROM python:3.9 as builder

WORKDIR /app

COPY . /app/

#----------------------
#------  Stage 2  -----
FROM python:3.9-alpine as test

WORKDIR /app
COPY --from=builder . /app

COPY ./tests /app

RUN python /app/test.py

#----------------------
#------  Stage 3  -----
FROM python:3.9-alpine as final

WORKDIR /app

COPY --from=builder . /app
