from flask import Flask, render_template

app = Flask(__name__)

# Criar a primeira do site

# route -> dekisite/

# função -> o que você quer exibir naquela página

# SEGUNDO PASSO:

# Criar uma pasta "templates" na mesma pasta do progeto.

# Colocar seu site no ar com heroku:
    # Criar um login no hiroku ,depois instalar o git conforme no site do hiroku.
    # Depois de tudo instalado fechar e abrir seu editor de desenvolvimento.
    # Testar no terminal o git e o heroku se aparecer os comandos quer dizer que foi instalado com sucesso!
    # Criar um arquivo "Procfile" e dentro do arquivo "web: gunicorn 'nome_do_site':app"
    # No terminal executar o comando "pip freeze > requirements.txt"
@app.route("/")
def homepage():
    return render_template("homepage.html")


@app.route("/contatos")
def contatos():
    return render_template("contatos.html")


@app.route("/usuario/<nome_usuario>")
def usuario(nome_usuario):
    return render_template("usuario.html", nome_usuario=nome_usuario)


# colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)
