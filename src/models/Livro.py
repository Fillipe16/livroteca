import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Livro(Base):

    __tablename__ = "livro"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(200), nullable=False)
    autor = db.Column(db.String(200))
    genero = db.Column(db.String(50))
    anoDePublicacao = db.Column(db.Integer, nullable=False)

    def getId(self):
        return self.id