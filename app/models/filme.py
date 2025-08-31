from app.database import db
from collections import OrderedDict

class Filme(db.Model):
    __tablename__ = "filmes"

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(40), nullable=False)
    ano = db.Column(db.Integer)
    diretor = db.Column(db.String(30))

    def to_dict(self):
        return OrderedDict([
            ("id", self.id),
            ("titulo", self.titulo),
            ("ano", self.ano),
            ("diretor", self.diretor)
        ])
