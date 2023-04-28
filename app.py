from flask import Flask, render_template, request, redirect, url_for
from models import Jogo

app = Flask(__name__)

jogos = [
    Jogo('Tetris', 'Puzzle', 'Atari'),
    Jogo('God Of War', 'RPG', 'Play Station'),
    Jogo('Skyrim', 'RPG', 'PC'),
]

@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=jogos)


@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar():
    if request.method == 'POST':
        nome = request.form['nome']
        categoria = request.form['categoria']
        console = request.form['console']
        jogos.append(Jogo(nome, categoria, console))
        return redirect(url_for('index'))
    else:
        return render_template('adicionar.html', titulo='Jogos')


if __name__ == '__main__':
    app.run(debug=True, port=8000)
