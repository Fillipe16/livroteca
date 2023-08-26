class TelaInicial:

    @staticmethod
    def exibeMenuInicial():
        print("Escolha uma das opções abaixo:")
        print("1 - Listar livros no catálogo")
        print("2 - Cadastrar livro no catálogo")
        print("3 - Editar infomrações de um livro")
        print("4 - Deletar livro do catálogo")
        print("5 - Pesquisar por livro no catálogo")
        print("6 - Sair\n")
        opcao = int(input())

        return opcao
    
    @staticmethod
    def listaLivros(livros):
        for livro in livros:
            print(f'O livro {livro.titulo} foi lançado em {livro.anoDePublicacao}')
    
    @staticmethod
    def exibeInformacoesDoLivro(livro):
        informacoesDoLivro = f'Titulo do livro: {livro.titulo}\n' +\
                              f'Autor do Livro: {livro.autor}\n' +\
                              f'Genero do livro: {livro.genero}\n' +\
                              f'Ano de publicação do livro: {livro.anoDePublicacao}\n'
        print(informacoesDoLivro)

    