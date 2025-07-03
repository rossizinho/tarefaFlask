from Projeto import database, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))

class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(50), nullable=False)
    email = database.Column(database.String(120), unique=True, nullable=False)
    senha = database.Column(database.String(100), nullable=False)
    tarefas = database.relationship('Tarefa', backref='usuario', lazy=True)

class Categoria(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    nome = database.Column(database.String(50), nullable=False, unique=True)
    tarefas = database.relationship('Tarefa', backref='categoria', lazy=True)

class Tarefa(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    titulo = database.Column(database.String(100), nullable=False)
    usuario_id = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)
    categoria_id = database.Column(database.Integer, database.ForeignKey('categoria.id'), nullable=True)
