# Documentação da API

## Visão Geral
O objetivo deste projeto foi criar uma API que fornece acesso a um banco de dados de filmes, permitindo que os usuários obtenham uma lista de filmes disponíveis. A API foi construída utilizando o framework <kbd>**Flask**</kbd> em <kbd>**Python**</kbd> e utiliza um banco de dados <kbd>**MySQL (on cloud)**</kbd> para armazenar informações sobre os filmes.

Além disso, o projeto também incluiu o deploy da API na plataforma Vercel, que é uma plataforma de hospedagem de aplicativos que oferece escalabilidade automática e integração contínua. Para armazenar o banco de dados, foi utilizado o serviço on cloud do Railway, que oferece hospedagem de banco de dados MySQL gerenciada.

Com este projeto, o objetivo foi criar uma API funcional e escalável que permite aos usuários acessar facilmente informações sobre filmes disponíveis, utilizando tecnologias modernas e serviços de hospedagem confiáveis.

<br>

## Endpoints da API

Endpoint principal: https://my-first-api-jdeveloperanalyst.vercel.app

__*Resposta:*__
```
API disponível! 

Para recuperar a lista de filmes disponíveis, faça uma solicitação GET para o endpoint /filmes.
```

#### GET /filmes

Endpoint de filmes: https://my-first-api-jdeveloperanalyst.vercel.app/filmes

A resposta é um objeto JSON contendo uma lista de objetos de filme, onde cada objeto de filme contém os seguintes campos:

* Id (inteiro): o ID do filme
* Título (string): o título do filme
* Ano (inteiro): o ano em que o filme foi lançado
* Direção (string): o diretor do filme

__*Exemplo de resposta:*__
```
[
  {
    "Id": 1,
    "Título": "Matrix",
    "Ano": 1999,
    "Direção": "Wachowski"
  },

  {
    "Id": 2,
    "Título": "Star Wars",
    "Ano": 1997,
    "Direção": "George Lucas"
  },

  {
    "Id": 3,
    "Título": "The Avengers",
    "Ano": 2012,
    "Direção": "Joss Whedon"
  },

  {
    "Id": 4,
    "Título": "John Wick – De Volta ao Jogo",
    "Ano": 2014,
    "Direção": "Chad Stahelski"
  }
]
```

#### Código de status:
* **200 OK:** *A solicitação foi bem sucedida e os dados solicitados foram retornados com sucesso.*

#### Códigos de erro:
* **404 Não encontrado:** *O endpoint solicitado não existe.*
* **500 Erro interno do servidor:** *Ocorreu um erro ao processar a solicitação.*

:construction: [*Clique aqui*]() *Vídeo explicativo em construção :construction:*

<h5 align="center">
  :construction: Projeto README :rocket: em construção :construction:
</h5>
 
