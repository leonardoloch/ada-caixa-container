# Aula 2
```Bash
docker build --tag aula2volume .

docker volume create aula2

docker run --volume=aula2:/volume/ --rm -d --name aula2volume aula2volume

docker exec -it aula2volume bash
```