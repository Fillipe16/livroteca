from models.Livro import Livro
class FormularioDoLivro:

    @staticmethod
    def exibeFormularioDoLivro():
        print("Digite as informações do Livro:\n")
        titulo = input("Informe o titulo do livro:")
        autor = input("Informe o autor do livro:")
        genero = input("Informe o genero do livro:")
        anoDePublicacao = input("Informe o ano de publicação do livro:")

        return titulo,autor,genero,anoDePublicacao