# Comandos
```bash
docker network create rede-nginx
```

```bash
docker network ls
```

```bash
docker network inspect rede-nginx
```

```bash
docker network inspect rede-nginx
```

```bash
docker run --rm -d --name nginx --network rede-nginx  nginx 
```

```bash
docker run --rm -d --name nginx2 --network rede-nginx  nginx 
```
Uma vez que foi criado uma rede bridge podemos chamar os container pelo nome, assim facilita a comunicação