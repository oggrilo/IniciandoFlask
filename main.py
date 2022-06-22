from flask import Flask, render_template, request
import operacoes

import this

this.nome = ""
this.telefone = ""
this.endereco = ""
this.data = ""
this.dados = ""

this.mensagem = ""

this.codigo = ""

pessoa = Flask(__name__) #representando uma variável do tipo flask

@pessoa.route('/', methods=['GET','POST'])
def cadastrar():
    if request.method == 'POST':
        this.nome = request.form['tNovoNome']
        this.telefone = request.form['tNovoTelefone']
        this.endereco = request.form['tNovoEndereco']
        this.data = request.form['tNovoData']
        this.dados = operacoes.inserir(this.nome, this.telefone, this.endereco, this.data)
    return render_template('index.html', titulo='Página Principal', resultado=this.dados)

@pessoa.route('/consultar.html', methods=['GET', 'POST'])
def consultarTudo():
    if request.method == 'POST':
        this.mensagem = operacoes.consultar()
    return render_template('/consultar.html', titulo='Página de Consulta', dados=this.mensagem)


@pessoa.route('/consultarCodigo.html', methods=['GET', 'POST'])
def consultarUm():
    if request.method == 'POST':
        this.codigo = request.form['Codigo']
        this.mensagem = operacoes.consultar(this.codigo)
    else:
        this.mensagem = ""
    return render_template('/consultarCodigo.html', titulo='Página de Consulta Por Código', dados=this.mensagem)


if __name__ == '__main__':
    pessoa.run(debug=True, port=5000)
