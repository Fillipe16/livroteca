class Login:

    @staticmethod
    def exibeFormularioDeLogin():
        nome = input("Digite o nome do usuario:")
        senha = input("Digite a senha do usuario:")

        return nome, senha