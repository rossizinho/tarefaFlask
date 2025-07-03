from Projeto import database, app
from Projeto.models import Usuario, Categoria, Tarefa

with app.app_context():
    database.create_all()