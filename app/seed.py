from app.database import db
from app.models.filme import Filme

def seed_data():
    if Filme.query.count() == 0:  # Só insere se a tabela estiver vazia
        filmes = [
            {"titulo": "Matrix", "ano": 1999, "diretor": "Wachowski"},
            {"titulo": "Star Wars", "ano": 1997, "diretor": "George Lucas"},
            {"titulo": "The Avengers", "ano": 2012, "diretor": "Joss Whedon"},
            {"titulo": "John Wick – De Volta ao Jogo", "ano": 2014, "diretor": "Chad Stahelski"},
        ]
        for f in filmes:
            db.session.add(Filme(**f))
        db.session.commit()
        print("💾 Dados iniciais inseridos com sucesso!")
    else:
        print("📂 Banco já possui dados, não foi necessário inserir.")
