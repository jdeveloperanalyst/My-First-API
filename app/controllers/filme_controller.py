from app.models.filme import Filme
from app.database import db
from collections import OrderedDict

def filme_to_dict(filme):
    return OrderedDict([
        ("id", filme.id),
        ("titulo", filme.titulo),
        ("ano", filme.ano),
        ("diretor", filme.diretor)
    ])


def listar_filmes():
    filmes = Filme.query.all()
    return [filme_to_dict(f) for f in filmes]


def obter_filme_por_id(filme_id):
    filme = db.session.get(Filme, filme_id)
    if not filme:
        return None
    return filme_to_dict(filme)


def adicionar_filme(data):
    try:
        filme = Filme(**data)
        db.session.add(filme)
        db.session.commit()
        return filme_to_dict(filme)
    except Exception as e:
        db.session.rollback()
        return {"erro": str(e)}


def atualizar_filme(filme_id, data):
    filme = Filme.query.get(filme_id)
    if not filme:
        return None
    for key, value in data.items():
        setattr(filme, key, value)
    db.session.commit()
    return filme_to_dict(filme)


def deletar_filme(filme_id):
    filme = Filme.query.get(filme_id)
    if not filme:
        return None
    db.session.delete(filme)
    db.session.commit()
    return True
