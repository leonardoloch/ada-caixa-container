FROM ubuntu:22.04

WORKDIR /app

RUN apt update
RUN apt install python3 -y

COPY main.py .

ENV ENVIRONMENT staging

ENTRYPOINT [ "python3" ]
CMD [ "main.py"]
