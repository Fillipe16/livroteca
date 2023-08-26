from models.Livro import Livro
from views.TelaInicial import TelaInicial
from views.FormularioDoLivro import FormularioDoLivro
from views.Login import Login
from models.DAO.LivroDAO import LivroDAO
from models.DAO.UsuarioDAO import UsuarioDAO

def autenticar(nome, senha):
    usuarioDAO = UsuarioDAO()
    usuario = usuarioDAO.buscarPorNome(nome)
    if(usuario and usuario.senha == senha):
        return True
    return False

if __name__ == '__main__':
    opcao=0
    livroDAO = LivroDAO()
    usuario = None

    while(opcao!=6):
        opcao = TelaInicial.exibeMenuInicial()

        if(opcao==2):

            nome,senha = Login.exibeFormularioDeLogin()
            if(autenticar(nome,senha)):
                titulo,autor,genero,anoDePublicacao = FormularioDoLivro.exibeFormularioDoLivro()

                livroDAO.cadastrar(titulo,autor,genero,anoDePublicacao)
                
            else:
                print("Usuario ou senha incorretos")
        elif(opcao==1):
            
            listaDeLivros = livroDAO.listarTodos()
            TelaInicial.listaLivros(listaDeLivros)

        elif(opcao==3):
            nomeDoLivro = input("Digite o nome do livro: ")

            livro = livroDAO.buscarPorNome(nomeDoLivro)
            if(livro):
                titulo,autor,genero,anoDePublicacao = FormularioDoLivro.exibeFormularioDoLivro()
                livroDAO.atualizar(livro,titulo,autor,genero,anoDePublicacao)
        elif(opcao==4):
            nomeDoLivro = input("Digite o nome do livro: ")

            livro = livroDAO.buscarPorNome(nomeDoLivro)
            if(livro):
                livroDAO.deletar(livro)
        elif(opcao==5):

            nomeDoLivro = input("Digite o nome do livro: ")

            livro = livroDAO.buscarPorNome(nomeDoLivro)
            if(livro):
                TelaInicial.exibeInformacoesDoLivro(livro)

           

