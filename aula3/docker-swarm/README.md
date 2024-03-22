# Aula 3

## Criando o cluster do Docker Swarm
```Bash
docker network create dind-network

docker run --rm --privileged --name master -d \
	--network dind-network \
    -p 127.0.0.1:8080:8080 \
	docker:dind

docker run --rm --privileged --name worker-01 -d \
	--network dind-network \
	docker:dind

docker run --rm --privileged --name worker-02 -d \
	--network dind-network \
	docker:dind
```

# Inicializar o Cluster
## Master
```Bash
docker swarm init
```

## Workers
Copiar o comando join que saiu no comando anterior

Examplo:
```Bash
docker swarm join --token SWMTKN-1-2ogrb3p01a4zkq7fera9z7vrtcmmuzl4fw14ydck4gnjxx54ve-dqr961mght0avk1v6sdsum9mv 172.19.0.2:2377
```

## Nodes
Podemos validar os nodes que estão no cluster
```Bash
docker node ls
```

# Service
## Criacao
```Bash
docker service create  --replicas 2 --constraint "node.role==worker" --publish published=8080,target=80 --name nginx nginx
```

## Listando Services
```Bash
docker service ls
```


### Rodando apenas nos workers
```Bash
docker service create --constraint "node.role==worker" --replicas 2 --name nginx nginx

```
Utilizamos o --constraint "node.role==worker" para indicar que a aplicação só deve rodar nos workers.
## Update
```Bash
docker service update nginx  --image nginx:stable-alpine3.17-slim
```

## Scale

```Bash
docker service scale nginx=3
```
## Rollback

```Bash
docker service update nginx  --rollback
```
Ou
```Bash
docker service rollback nginx 
```


## Romovendo
```Bash
docker service rm nginx
```

# Destruindo o ambiente
```Bash
docker kill master worker-01 worker-02
```