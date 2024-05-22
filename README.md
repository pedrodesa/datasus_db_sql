# Banco de Dados Sinan Hanseníase

## Objetivo
Este banco de dados foi criado para armazenar os dados úblicos do Sinan hanseníase do DATASUS.

## Stack
Python
Docker
PostgreSQL
PgAdmin4

## Web scraping de dados



## Banco de Dados - PostgreSQL com Docker

1) Criar um arquivo Dockerfile

````
# Use the official PostgreSQL image as a base
FROM postgres:latest

# Define arguments and then convert them to environment variables
ARG POSTGRES_PASSWORD
ARG POSTGRES_USER
ARG POSTGRES_DB

ENV POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
ENV POSTGRES_USER=${POSTGRES_USER}
ENV POSTGRES_DB=${POSTGRES_DB}

# Expose the default PostgreSQL port
EXPOSE 5432

# Set the default command to run when starting the container
CMD ["postgres"]
````

2) Criar imagem

Criar imagem
```
docker build -t minha_imagem_postgres --build-arg POSTGRES_PASSWORD=minha_senha --build-arg POSTGRES_USER=meu_usuario --build-arg POSTGRES_DB=meu_banco .
```

Criar container
```
docker run --name meu_container_postgres -p 5432:5432 -v meu_volume_postgres:/var/lib/postgresql/data -d minha_imagem_postgres
```

## Acesso ao banco de dados
Para acessar o banco de dados utilizamos o PgAdmin

Link para criação do container do Docker Hub para o [PgAdmin](https://www.pgadmin.org/docs/pgadmin4/latest/container_deployment.html)

### Conecção com o banco de dados
* Para conexão com o banco de dados é necessário utilizar o endereço IP do container docker

```
docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' meu_container_postgres
```

## Criação de bancos de dados e tabelas
Os arquivos para a criação dos bancos de dados e tabelas estão no diretório do projeto db_sql



# Segurança
Para evitar exposição de dados sensíveis e senhas não devem ser salvas informações de usuário e senha no Dockerfile

É necessário criar um arquivo .env para colocar essas variáveis
```
touch .env
```

Nesse arquivo vamos ter as seguintes variáveis
```
POSTGRES_PASSWORD=minha_senha
POSTGRES_USER=meu_usuario
POSTGRES_DB=meu_banco
```

