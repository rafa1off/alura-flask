from db import db

# Classes
class Jogo():
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console
        self.document = {
            'nome': self.nome,
            'categoria': self.categoria,
            'console': self.console
        }

    def add(self):
        db.jogos.insert_one(self.document)
