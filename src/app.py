
# Importando a biblioteca Flask
from flask import Flask, request, render_template, redirect, session
# Importando users.py para acessar os dados dos usuários
from users import indentificar_usuario

# Criando uma instância da aplicação Flask
app = Flask(__name__)
# Criando uma chave secreta para a aplicação, necessária para sessões e segurança (so para meu servidor)
app.secret_key = 'sua_chave_secreta_aqui'

# Definindo a rota para a página inicial
@app.route('/')
def home():
    # Aqui você diz: "Ei Flask, pegue o arquivo login.html e mostre pro usuário"
    # render_tamplate faz uma busca na pasta templates, então certifique-se de que seu login.html esteja lá
    return render_template('login.html')

# Definindo a rota para o login, recebendo dados pelo body (post)
@app.route('/login', methods=['POST'])
# A função login() é chamada quando o usuário acessa a rota /login, e é responsável por processar os dados do formulário de login
def login():
    # Pegando os dados do formulário de login usando request.form.get(), achando o valor de user e senha no body(post)
    u = request.form.get('user')
    s = request.form.get('senha')

    # Chamando a função indentificar_usuario para verificar se o usuário existe e a senha está correta
    resultado = indentificar_usuario(u, s)

    if resultado:
      # 1. SALVA O CRACHÁ: Guardamos quem logou na sessão
        session['usuario_id'] = u 
        # 2. REDIRECIONA: Empurra o usuário para a rota do dashboard
        return redirect('/dashboard')
    else:
        return "<h1>Acesso Negado!</h1>", 401 # 401 para receber essa informação no backend (Terminal)

# --- NOVA ROTA: O PAINEL DO BANCO ---
@app.route('/dashboard')
def dashboard():
    # 3. VERIFICA O CRACHÁ: Se não tiver o ID na sessão, expulsa pro login
    if 'usuario_id' not in session:
        return redirect('/')
    
    # 4. BUSCA OS DADOS ATUAIS: Pegamos o saldo atualizado do dicionário
    from users import users # Importe seu dicionário de usuários aqui ou no topo
    id_logado = session['usuario_id']
    dados_usuario = users[id_logado]

    # 5. MOSTRA A PÁGINA: Agora sim usamos o render_template
    return render_template('banco.html', nome=id_logado, saldo=dados_usuario['saldo'])

# --- ROTA DE SAÍDA ---
@app.route('/logout')
def logout():
    session.clear() # Destrói o crachá
    return redirect('/')


if __name__ == '__main__':
    # Iniciando a aplicação Flask em modo de depuração
    # .run() faz rodar a aplicação infinitamente, e debug=True é para facilitar o desenvolvimento, mostrando erros detalhados na página e toda vez
    # que você fizer uma mudança no código, a aplicação reinicia automaticamente.
    app.run(debug=True)