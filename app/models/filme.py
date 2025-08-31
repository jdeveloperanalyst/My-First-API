from app.database import db

class Filme(db.Model):
    __tablename__ = "filmes"

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(40), nullable=False)
    ano = db.Column(db.Integer)
    diretor = db.Column(db.String(30))

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "ano": self.ano,
            "diretor": self.diretor
        }
