from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'blabla'

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

jogo1 = Jogo('Super Mario', 'Acao', 'SNES')
jogo2 = Jogo('Pokemon Gold', 'RPG', 'GBA')
jogo3 = Jogo('Mortal Kombat', 'Luta', 'SNES')
lista = [jogo1, jogo2, jogo3]

@app.route('/')
def index():
    #lista = ['Tetris', 'Super Mario', 'Pokemon Gold']
    
    return render_template('lista.html', titulo='Jogos',
                            jogos=lista)

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo jogo')


@app.route('/criar',  methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria =  request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect('/')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if 'mestra' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(request.form['usuario'] + ' logou com sucesso!')
        return redirect('/')
    else :
        flash('Não Logado.')
        return redirect ('/login')

#app.run(debug=True)

app.run(host='0.0.0.0')