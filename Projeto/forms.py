from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from Projeto.models import Categoria

class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    botao_confirmacao = SubmitField('Login')

class FormCriarConta(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    username = StringField('Nome do Usuário', validators=[DataRequired()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 15)])
    confirmacao_senha = PasswordField('Confirme a Senha', validators=[DataRequired(), EqualTo('senha')])
    botao_confirmacao = SubmitField('Criar Conta')

class FormTarefa(FlaskForm):
    titulo = StringField('Título da Tarefa', validators=[DataRequired()])
    categoria = SelectField('Categoria', coerce=int, validators=[DataRequired()])
    botao_confirmacao = SubmitField('Criar Tarefa')

    def __init__(self, *args, **kwargs):
        super(FormTarefa, self).__init__(*args, **kwargs)
        self.categoria.choices = [(c.id, c.nome) for c in Categoria.query.order_by(Categoria.nome).all()]
