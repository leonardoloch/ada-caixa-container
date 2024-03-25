# Projeto Final
O projeto final vai se basear no projeto do modulo anterior, mesmo as pessoas que não finalizaram o projeto passado poderão desenvolver utilizando o que foi feito.

O projeto se baseia na criação de um docker compose, com os seguintes serviços:

* Aplicação
* Minio
* Redis
* RabbitMQ

O docker compose deve conter uma orquestração dos container, onde a aplicação deve ser o ultimo container a subir, garantindo assim que quando subir a aplicação não encontre nenhum error.

* Volume para persistir os dados do container do Minio, Redis e Rabbit.
* Criação de uma network e expor apenas as portas necessárias.
* Criação de um dockerfile para a aplicação.

Pense que é uma aplicação que deve ter como preocupação uma alta disponibilidade e que seja resiliente.

A entrega pode ser feita através de um repositório como o github. Deve conter:

* Uma documentação de como funciona o seu software
* Quais os comandos necessário para executar a solução
* Todos os arquivos: Lógica da aplicação, Dockerfile e um docker compose.

Lembre que toda solução deve esta contida no repositório , sem nenhuma ação previa no host que vai executar a solução .