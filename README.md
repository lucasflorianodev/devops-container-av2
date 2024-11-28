# CI/CD Pipeline com Flask e GitHub Actions 🚀

Este é um projeto simples que demonstra a implementação de um pipeline de **Integração Contínua** e **Entrega Contínua** (CI/CD) usando Flask, Docker e GitHub Actions. Ele inclui uma aplicação web básica em Flask, testes automatizados e uma configuração de pipeline CI/CD para garantir a qualidade do código e o processo de implantação.

---

## 📝 Funcionalidades

- **Aplicação Flask**: Um servidor básico que retorna `Hello, World!`.
- **Testes Automatizados**: Garante que o aplicativo funcione corretamente.
- **Pipeline CI/CD**: Automatiza o teste e a implantação usando GitHub Actions.
- **Deploy Simulado**: Exemplo simples para expandir para ambientes reais no futuro.

---

## 📁 Estrutura do Projeto

```plaintext
📂 projeto-ci-cd-flask
├── app.py                 # Código da aplicação Flask
├── test_app.py            # Testes unitários para a aplicação
├── Dockerfile             # Configuração para container Docker
├── requirements.txt       # Dependências do projeto
└── .github/
    └── workflows/
        └── main.yml       # Configuração do pipeline GitHub Actions
