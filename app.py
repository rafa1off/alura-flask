from flask import Flask, render_template, request, redirect, session, flash
from models import Jogo
from db import jogos
from bson import ObjectId

app = Flask(__name__)
app.secret_key = 'alura'

@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=jogos.find())


@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar():
    if request.method == 'POST':
        jogos.insert_one(Jogo(request.form['nome'], request.form['categoria'], request.form['console']).document)
        return redirect('/')
    else:
        return render_template('adicionar.html', titulo='Jogos')


@app.route('/excluir/<id>', methods=['POST', 'GET'])
def excluir(id):
    if request.method == 'POST':
        jogos.delete_one({'_id': ObjectId(id)})
        return redirect('/')
    else:
        return render_template('excluir.html', jogo=jogos.find_one({'_id': ObjectId(id)}))


@app.route('/logar')
def logar():
    return render_template('login.html', titulo='Faça seu login')


@app.route('/autenticar', methods=['POST'])
def autenticar():
    if request.form['senha'] == 'senha':
        session['usuario_logado'] = request.form['usuario']
        flash(session['usuario_logado'] + ' logado com sucesso')
        return redirect('/')
    else:
        flash('Falha na autenticação')
        return redirect('/logar')

if __name__ == '__main__':
    app.run(debug=True, port=8000)
