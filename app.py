from flask import Flask, render_template, request, redirect, url_for
from models import Jogo
from db import db
from bson import ObjectId

app = Flask(__name__)

'''jogos = [
    Jogo('Tetris', 'Puzzle', 'Atari'),
    Jogo('God Of War', 'RPG', 'Play Station'),
    Jogo('Skyrim', 'RPG', 'PC'),
]'''

@app.route('/')
def index():
    jogos = db.jogos.find()
    return render_template('lista.html', titulo='Jogos', jogos=jogos, db=db)


@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar():
    if request.method == 'POST':
        nome = request.form['nome']
        categoria = request.form['categoria']
        console = request.form['console']
        jogo = Jogo(nome, categoria, console)
        jogo.add()
        return redirect('/')
    else:
        return render_template('adicionar.html', titulo='Jogos')


@app.route('/excluir/<id>', methods=['POST', 'GET'])
def excluir(id):
    _id = ObjectId(id)
    jogo = db.jogos.find_one({'_id': _id})
    if request.method == 'POST':
        db.jogos.delete_one({'_id': _id})
        return redirect('/')
    else:
        return render_template('excluir.html', jogo=jogo)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
