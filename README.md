# Projeto DevOps com Containers 🐳

Este projeto configura um ambiente DevOps utilizando **Docker** e **Docker Compose** para orquestrar containers de banco de dados, backend, frontend e servidor web. Ele contém um **backend em Node.js**, um **frontend estático** servido via Nginx, e bancos de dados como **MySQL**, **PostgreSQL** ou **MongoDB** configurados com variáveis de ambiente.

## Funcionalidades

- **Frontend**: Servido por Nginx usando uma imagem leve (`nginx:alpine`).
- **Backend**: Node.js com **NestJS** e **TypeORM**.
- **Banco de Dados**: Suporte a **MySQL**, **PostgreSQL** ou **MongoDB**, configurado com variáveis de ambiente para facilitar a configuração de credenciais.
- **Docker Compose**: Facilita a orquestração dos containers de banco de dados, backend e frontend.

## Tecnologias Utilizadas

- **Docker**: Para criar e rodar os containers.
- **Node.js**: Backend utilizando a framework **NestJS**.
- **Nginx**: Servindo arquivos estáticos do frontend.
- **MySQL / PostgreSQL / MongoDB**: Banco de dados com containers dedicados.
- **Docker Compose**: Para gerenciar múltiplos containers de forma simplificada.

## Estrutura do Projeto

```plaintext
📂 devops-container-av2
├── 📂 backend
│   ├── src/                  # Código do backend
│   ├── Dockerfile            # Dockerfile para o backend
│   ├── package.json          # Dependências do Node.js
│   └── tsconfig.json         # Configuração do TypeScript
├── 📂 frontend
│   ├── index.html            # Arquivo principal do frontend
│   ├── styles.css            # Arquivo de estilos
│   ├── script.js             # Arquivo de script
│   ├── Dockerfile            # Dockerfile para o frontend
│   └── nginx.conf            # Configuração do Nginx
├── 📂 database
│   ├── docker-compose.yml    # Orquestração dos containers de banco de dados
│   └── .env                  # Arquivo de variáveis de ambiente para banco de dados
├── .dockerignore             # Arquivos a serem ignorados pelo Docker
└── README.md                 # Documentação do projeto
