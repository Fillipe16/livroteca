from flask  import Flask
from flask import render_template, url_for, redirect, request
from src.models.DAO.LivroDAO import LivroDAO

app = Flask(__name__)
app.config.from_pyfile('config.py')
livroDAO = LivroDAO()

@app.route("/")
def index():
    
    listaDeLivros = livroDAO.listarTodos()

    return render_template("TelaInicial.html", livros = listaDeLivros)

@app.route("/telaCadastroDeLivro")
def telaCadastroDeLivro():

    return render_template("Cadastro.html")

@app.route('/cadastrarLivro', methods=['POST',])
def cadastrarLivro():

    tituloDoLivro = request.form['titulo']
    autorDoLivro = request.form['autor']
    generoDoLivro = request.form['genero']
    anoDePublicacaoDoLivro = request.form['ano']

    livroDAO.cadastrar(tituloDoLivro,autorDoLivro,generoDoLivro,anoDePublicacaoDoLivro)

    return redirect(url_for('index'))
 
@app.route('/deletarLivro/<int:id>')
def deletarLivro(id):

    livroParaDeletar = livroDAO.buscarPorId(id)
    livroDAO.deletar(livroParaDeletar)

    return redirect(url_for('index'))

@app.route('/telaDeEditarLivro/<int:id>')
def exibeTelaDeEditar(id):

    livroParaEditar = livroDAO.buscarPorId(id)

    return render_template('editar.html', livro=livroParaEditar)

@app.route("/editarLivro", methods = ['POST',])
def editarLivro():

    idDoLivro = request.form['id']
    livroParaEditar = livroDAO.buscarPorId(idDoLivro)

    novoTituloDoLivro = request.form['titulo']
    novoAutorDoLivro = request.form['autor']
    novoGeneroDoLivro = request.form['genero']
    novoAnoDePublicaoDoLivro = request.form['ano']

    livroDAO.atualizar(livroParaEditar,novoTituloDoLivro,novoAutorDoLivro,novoGeneroDoLivro,novoAnoDePublicaoDoLivro)

    return redirect(url_for('index'))

app.run(debug=True)