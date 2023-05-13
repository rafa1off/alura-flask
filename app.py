from flask import Flask, render_template, request, redirect, url_for
from models import Jogo
from db import jogos
from bson import ObjectId

app = Flask(__name__)

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


if __name__ == '__main__':
    app.run(debug=True, port=8000)
