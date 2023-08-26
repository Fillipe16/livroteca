import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Usuario(Base):

    __tablename__ = "usuario"

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    senha = db.Column(db.String(100),nullable=False)

    

    