FROM ubuntu:22.04

WORKDIR /app

RUN apt update
RUN apt install python3 -y

COPY . .

ENTRYPOINT [ "bash" ]
CMD [ "/app/entrypoint.sh" ]
