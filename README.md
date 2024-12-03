# Projeto DevOps com Containers 🐳

Este projeto configura um ambiente DevOps utilizando **Docker** e **Docker Compose** para orquestrar containers de banco de dados, backend, frontend e servidor web. Ele contém um **backend em Node.js**, um **frontend estático** servido via Nginx, e bancos de dados como **MySQL**, **PostgreSQL** ou **MongoDB** configurados com variáveis de ambiente.

---

## Sumário

1. [Visão Geral](#visão-geral)
2. [Tecnologias Utilizadas](#tecnologias-utilizadas)
3. [Decisões Arquiteturais](#decisões-arquiteturais)
4. [Estrutura do Projeto](#estrutura-do-projeto)
5. [Configuração do Ambiente](#configuração-do-ambiente)
6. [Como Executar](#como-executar)
7. [Testes Básicos](#testes-básicos)
8. [Desafios Enfrentados](#desafios-enfrentados)
9. [Contribuições e Licença](#contribuições-e-licença)

---

## Visão Geral

O objetivo deste projeto é demonstrar como criar, configurar e executar uma aplicação multi-container com **Docker** e **Docker Compose**, garantindo persistência de dados, modularidade e uma comunicação eficiente entre os serviços.

### Componentes:

- **Frontend**: Um contador simples (HTML, CSS e JavaScript).
- **Backend**: API construída com Python Flask para processamento de dados.
- **Banco de Dados**: PostgreSQL com persistência via volumes Docker.
- **API Mock**: Simula uma API externa para fornecer dados ao backend.

---

## Tecnologias Utilizadas

- **Docker**: Para containerização dos serviços.
- **Docker Compose**: Para orquestração de múltiplos containers.
- **Python Flask**: Para criar o backend e a API mock.
- **PostgreSQL**: Banco de dados relacional.
- **Nginx**: Para servir o frontend.
- **JavaScript**: Para a lógica do frontend.

---

## Decisões Arquiteturais

1. **Modularidade**: Cada componente roda em um container independente, facilitando a manutenção e o escalonamento.
2. **Persistência de Dados**: O banco de dados utiliza volumes para garantir que os dados não sejam perdidos após a reinicialização dos containers.
3. **Comunicação entre Containers**: Todos os containers estão conectados a uma rede Docker personalizada, permitindo comunicação eficiente usando nomes de serviços como hostnames.
4. **Orquestração com Docker Compose**: Gerenciar serviços, redes e volumes de forma simplificada.

---


## Estrutura do Projeto

Abaixo está uma explicação detalhada sobre cada diretório e arquivo presente no projeto:

### 1. **bd**
Este diretório contém arquivos relacionados ao banco de dados:

- **.env**: Arquivo com variáveis de ambiente, como credenciais do banco e configurações importantes.
- **docker-compose.yml**: Define o serviço de banco de dados no ambiente Docker Compose.
- **Dockerfile**: Configura o container para o banco de dados, com personalizações adicionais, caso necessário.

---

### 2. **backend**
Diretório responsável pela lógica do backend da aplicação.

- **src/**: Contém o código-fonte principal do backend.
- **Dockerfile**: Define a configuração Docker para o backend.
- **package.json e package-lock.json**: Gerencia as dependências do backend (Node.js).
- **wait-for-db.sh**: Script que garante que o backend só será iniciado após o banco de dados estar disponível.

---

### 3. **frontend**
Diretório do frontend da aplicação, contendo arquivos para exibição e interação com o usuário.

- **index.html**: Estrutura HTML do frontend.
- **style.css**: Arquivo de estilos para personalização visual.
- **script.js**: Arquivo de JavaScript com a lógica do contador.
- **Dockerfile**: Configura a imagem Docker para servir o frontend como conteúdo estático (usando Nginx).

---

### 4. **init-scripts**
Scripts de inicialização para o banco de dados.

- **init.sql**: Script SQL para inicializar o banco de dados com tabelas e dados básicos.
- **backup.sql**: Script contendo um backup do banco de dados para restauração.

---

### 5. **mock-api**
Diretório dedicado à API mock, que simula uma API externa para comunicação com o backend.

## Configuração do Ambiente

Antes de começar, certifique-se de ter o seguinte instalado:

1. **Docker**: [Guia de Instalação do Docker](https://www.docker.com/get-started)
2. **Docker Compose**: [Guia de Instalação do Docker Compose](https://docs.docker.com/compose/install/)

## Fluxo do Projeto

1. **Banco de Dados**:
   - O banco de dados é configurado e inicializado com os scripts SQL presentes em `init-scripts/`.
   - As credenciais e configurações são gerenciadas via variáveis de ambiente no arquivo `.env`.

2. **Backend**:
   - O backend se comunica com o banco de dados para manipulação de dados e com a API mock para simulação de dados externos.
   - A inicialização é gerenciada por scripts como `wait-for-db.sh`.

3. **Frontend**:
   - Interface simples que consome os dados do backend.
   - Servido por um container Nginx configurado no `Dockerfile` do frontend.

4. **API Mock**:
   - Simula uma API externa para fornecer dados ao backend.
   - Implementada em Python Flask e configurada via Docker.
