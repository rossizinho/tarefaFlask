from flask import render_template, url_for, redirect, flash, request
from Projeto import app, database, bcrypt
from flask_login import login_user, logout_user, login_required, current_user
from Projeto.models import Usuario, Tarefa, Categoria
from Projeto.forms import FormLogin, FormCriarConta, FormTarefa

@app.route("/", methods=["GET", "POST"])
def homepage():
    if current_user.is_authenticated:
        return redirect(url_for('listar_tarefas'))
    form_login = FormLogin()
    if form_login.validate_on_submit():
        usuario = Usuario.query.filter_by(email=form_login.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, form_login.senha.data):
            login_user(usuario)
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('listar_tarefas'))
        else:
            flash('Login inválido. Verifique seu email e senha.', 'danger')
    return render_template('home.html', form=form_login)

@app.route('/criarconta', methods=['GET', 'POST'])
def criarconta():
    if current_user.is_authenticated:
        return redirect(url_for('listar_tarefas'))
    form = FormCriarConta()
    if form.validate_on_submit():
        usuario_existe = Usuario.query.filter_by(email=form.email.data).first()
        if usuario_existe:
            flash('Email já cadastrado. Faça login.', 'warning')
            return redirect(url_for('homepage'))
        senha_hash = bcrypt.generate_password_hash(form.senha.data).decode('utf-8')
        novo_usuario = Usuario(username=form.username.data, email=form.email.data, senha=senha_hash)
        database.session.add(novo_usuario)
        database.session.commit()
        login_user(novo_usuario)
        flash('Conta criada com sucesso!', 'success')
        return redirect(url_for('listar_tarefas'))
    return render_template('criarconta.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Você saiu da sua conta.', 'success')
    return redirect(url_for('homepage'))


@app.route('/tarefas')
@login_required
def listar_tarefas():
    tarefas = Tarefa.query.filter_by(usuario_id=current_user.id).all()
    return render_template('tarefa.html', tarefas=tarefas)

@app.route('/tarefas/criar', methods=['GET', 'POST'])
@login_required
def criar_tarefa():
    form = FormTarefa()
    if form.validate_on_submit():
        nova_tarefa = Tarefa(
            titulo=form.titulo.data,
            categoria_id=form.categoria.data,
            usuario_id=current_user.id
        )
        database.session.add(nova_tarefa)
        database.session.commit()
        flash('Tarefa criada com sucesso!', 'success')
        return redirect(url_for('listar_tarefas'))
    return render_template('criartarefa.html', form=form)
