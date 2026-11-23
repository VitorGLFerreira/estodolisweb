from datetime import date
from flask import Flask, render_template, request, session, redirect, flash
from database import consultar_tarefas, inserir_tarefa

app = Flask(__name__)
app.secret_key = "vitorgabriel"

# Dados de acesso do ADMIN
ADMIN_EMAIL = "vithor@gmail.com"
ADMIN_SENHA = "141414"

CATEGORIAS = ["Escola", "Trabalho", "Projetos", "Pessoal", "Saúde", "Outros"]

def validar_tarefa(Nome, Descricao, Categoria, Prazo, Prioridade):
    erros = []
    if len(Nome) < 5 or len(Nome) > 30 or Nome.isdigit():
        erros.append("Nome: de 5 a 30 caracteres, não só números.")

@app.route("/") # HomePage - Página Inicial
def index():
    if "login" not in session:
        return redirect("/login")
    # Usúario logado
    tarefas = consultar_tarefas()
    return render_template("index.html", tarefas=tarefas) 

#Rota de login
@app.route("/login", methods=["GET","POST"])
def login():
    if "login" in session:
        return redirect("/")

    if request.method == "GET":
        return render_template("login.html")

    # POST
    email = request.form.get("email") # Pegando o emial que estava no form HTLM
    senha = request.form.get("senha") # Essa informação está no atributo name

    if email == ADMIN_EMAIL and senha == ADMIN_SENHA:
        session["login"] = True # Cria a sessao login
        return redirect("/") # Redireciona para a rota inicial
    else:
        return render_template("login.html", msgerro = "E-mail ou senha estão errados! Seu animal, muito burro kkkkkkk")

#Rota Logout
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

# Tratamento de erro - Codigo 404
@app.errorhandler(404)
def not_found(erro):
    return render_template("erro404.html"),404

# Rota que mostra o formulário
@app.route("/adicionar", methods=["GET", "POST"])
def adicionar() :
    if request.method == "GET":
        return render_template("formulario.html", categorias=CATEGORIAS, dados={}, erros=[])

    # POST: ler o que veio do formulário 
    Nome_tarefa = request.form.get("Nome_tarefa", "").strip()
    Descricao = request.form.get("Descricao", "").strip()
    Categoria = request.form.get("Categoria", "").strip()
    Data_prazo = request.form.get("Data_prazo", "")
    Prioridade = request.form.get("Prioridade", "")

    # validar os campos aqui

    if inserir_tarefa(Nome_tarefa, Descricao, Categoria, Data_prazo, Prioridade):
        flash("Tarefa adicionada com sucesso!")
    else:
        flash("Não foi possível salvar. Confira a conexão com o banco.")
    return redirect("/")



    



if __name__ == "__main__":
    app.run(debug=True, port=5000)
# host='0.0.0.0' Habilita o IP publico
app.run

