from models.DAO.FabricadeConexao import FabricaDeConexao
from sqlalchemy.orm import sessionmaker
from models.Usuario import Usuario

class UsuarioDAO:

    fabricaDeConexao = FabricaDeConexao()
    engine = fabricaDeConexao.getConexao()
    Session = sessionmaker(bind = engine)
    session = Session()


    def buscarPorNome(self,nomeDoUsuario):

        usuario = self.session.query(Usuario).filter(Usuario.nome == nomeDoUsuario).first()
        return usuario

