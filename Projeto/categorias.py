from Projeto import app, database
from Projeto.models import Categoria

with app.app_context():
    cat1 = Categoria(nome="Estudo")
    cat2 = Categoria(nome="Casa")
    cat3 = Categoria(nome="Trabalho")
    cat4 = Categoria(nome="Lazer")
    cat5 = Categoria(nome="Saúde")

    database.session.add_all([cat1, cat2, cat3, cat4, cat5])
    database.session.commit()
    print("Categorias criadas com sucesso!")

