```bash
docker compose up
```


```bash
docker compose down
```

Para docker stack tambem conseguimos utilizar a seguinte sintaxe:
* echo secret_echo | docker secret create secret_echo_nome -
* docker secret create file_db_pass file_db_pass

e conseguimos referenciar no manifesto do docker stack:
```yaml
secrets:
  secret_echo_nome:
    external: true
```

# Links
* https://docs.docker.com/engine/swarm/secrets/
* https://spacelift.io/blog/docker-secrets