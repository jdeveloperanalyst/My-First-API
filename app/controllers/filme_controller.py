from app.models.filme import Filme
from app.database import db
from collections import OrderedDict


def listar_filmes():
    filmes = Filme.query.all()
    return [f.to_dict() for f in filmes]

def obter_filme_por_id(filme_id):
    filme = db.session.get(Filme, filme_id)
    if not filme:
        return None
    return filme.to_dict()

def adicionar_filme(data):
    try:
        filme = Filme(**data)
        db.session.add(filme)
        db.session.commit()
        return filme.to_dict()
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
    return filme.to_dict()


def deletar_filme(filme_id):
    filme = Filme.query.get(filme_id)
    if not filme:
        return None
    db.session.delete(filme)
    db.session.commit()
    return True
