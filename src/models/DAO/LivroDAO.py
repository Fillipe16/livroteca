import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from src.models.Livro import Livro
from src.models.DAO.FabricadeConexao import FabricaDeConexao


class LivroDAO:

    fabricaDeConexao = FabricaDeConexao()
    engine = fabricaDeConexao.getConexao()

    Session = sessionmaker(bind = engine)
    session = Session()

   
    def cadastrar(self,tituloDoLivro,autorDoLivro,generoDoLivro,anoDePublicacaoDoLivro):
        
        novoLivro = Livro(titulo = tituloDoLivro,autor = autorDoLivro,genero = generoDoLivro,anoDePublicacao = anoDePublicacaoDoLivro)

        self.session.add(novoLivro)
        self.session.commit()

   
    def listarTodos(self):

        listaDeLivros = self.session.query(Livro).all()
        return listaDeLivros
    
    def buscarPorNome(self,tituloDoLivro):

        livroProcurado = self.session.query(Livro).filter(Livro.titulo==tituloDoLivro).first()
        return livroProcurado
    
    def buscarPorId(self,idDoLivro):

        livroProcurado = self.session.query(Livro).filter(Livro.id==idDoLivro).first()
        return livroProcurado
    
    def atualizar(self,livro,titulo,autor,genero,anoDePublicacao):

        livro.titulo = titulo
        livro.autor = autor
        livro.genero = genero
        livro.anoDePublicacao = anoDePublicacao

        self.session.commit()

    def deletar(self,livro):

        self.session.delete(livro)

        self.session.commit()