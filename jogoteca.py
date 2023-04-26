from flask import Flask, render_template
from models import Jogo

app = Flask(__name__)

@app.route('/')
def index():
    jogos = [
        Jogo('Tetris', 'Puzzle', 'Atari'),
        Jogo('God Of War', 'RPG', 'Play Station'),
        Jogo('Skyrim', 'RPG', 'PC')
    ]
    return render_template('lista.html', titulo='Jogos', jogos=jogos)
