# 🎬 MY-FIRST-API

![Python](https://img.shields.io/badge/python-3.10-blue)
![Flask](https://img.shields.io/badge/framework-Flask-red)
![SQLAlchemy](https://img.shields.io/badge/ORM-SQLAlchemy-orange)
![Docker](https://img.shields.io/badge/container-Docker-blue)
![Swagger](https://img.shields.io/badge/docs-Swagger-brightgreen)

Uma API RESTful para gerenciamento de filmes, desenvolvida com **Python**, utilizando o framework **Flask**, o ORM **SQLAlchemy** e conteinerizada com **Docker**. O projeto segue o padrão arquitetural **MVC (Model-View-Controller)** e inclui documentação interativa via **Swagger**, acessível diretamente na raiz (`/`) da aplicação.

---

## 📁 Estrutura do Projeto
```
MY-FIRST-API/
├── app/
│   ├── __pycache__/              # Cache de compilação Python
│   ├── controllers/              # Lógica de negócio (Controller)
│   │   ├── __pycache__/
│   │   └── filme_controller.py
│   ├── models/                   # Modelos de dados (Model)
│   │   ├── __pycache__/
│   │   └── filme.py
│   ├── views/                    # Rotas da API (View)
│   │   ├── __pycache__/
│   │   └── routes.py
│   ├── __init__.py               # Inicializa o módulo app
│   ├── app.py                    # Ponto de entrada da aplicação Flask
│   ├── database.py               # Configuração da conexão com o banco
│   ├── seed.py                   # Script para popular o banco com dados iniciais
│   └── swagger.yaml              # Documentação Swagger (OpenAPI)
├── .env                          # Variáveis de ambiente
├── .env.example                  # Exemplo de configuração
├── .gitignore                    # Arquivos ignorados pelo Git
├── docker-compose.yml            # Orquestração dos serviços com Docker
├── Dockerfile                    # Imagem da API Flask
└── requirements.txt              # Dependências do projeto
```

---

## 🚀 Tecnologias Utilizadas

- **Python 3.10**
- **Flask** — microframework web
- **SQLAlchemy** — ORM para manipulação do banco de dados
- **MySQL** — banco de dados relacional
- **Docker & Docker Compose** — ambiente isolado e replicável
- **Swagger (via Flasgger)** — documentação interativa da API

---

## 📦 Como subir o projeto

1. Clone o repositório:
    ```bash
    git clone https://github.com/jdeveloperanalyst/My-First-API.git
    cd MY-FIRST-API
    ```

2. Configure o arquivo .env com suas variáveis de ambiente (veja .env.example como referência).
    <img width="348" height="164" alt="image" src="https://github.com/user-attachments/assets/f8f8b8e6-8413-499c-81f9-4bb1301e4bf2" />



3. Instale o Docker e o Docker Compose (se ainda não tiver).

4. Suba os containers com:
   ```bash
   docker-compose up --build
   ```
   docker-compose.yml
   <img width="810" height="817" alt="image" src="https://github.com/user-attachments/assets/be6f6a3f-c726-4d56-b5d6-e0906bc42ea3" />

6. Acesse a API em:
   ```
   http://localhost:5000/
   ```

## 📚 Documentação da API
A documentação Swagger está disponível diretamente na raiz da aplicação:

## 🔗 http://localhost:5000/

Você pode visualizar todos os endpoints, parâmetros e realizar testes diretamente pela interface.

<img width="1726" height="907" alt="image" src="https://github.com/user-attachments/assets/cf5ce2f0-8196-414f-810f-37b93f2bcf1d" />



## 🛠️ Endpoints principais
`GET /filmes` — Lista todos os filmes

`GET /filmes/<id>` — Busca filme por ID

`POST /filmes` — Adiciona novo filme

`PUT /filmes/<id>` — Atualiza filme existente

`DELETE /filmes/<id>` — Remove filme

## 📌 Observações
O projeto está em desenvolvimento e pode receber melhorias.

Sugestões, issues e pull requests são bem-vindos!


