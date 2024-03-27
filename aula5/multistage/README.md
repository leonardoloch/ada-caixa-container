# Comandos
Com docker multistage podemos ter varios stages no mesmo docker image, mas apenas o utimo stage vai ser a docker imagem final

Caso algum stage não ter dependencia sobre o ultimo stage vai ser ignorado sobre o processo de build. Para forçar rodar esse stage devesse passar o target
```bash
docker build -t multistage --target test  .
``` 