
# Importando a biblioteca Flask
from flask import Flask, request, render_template
# Importando users.py para acessar os dados dos usuários
from users import indentificar_usuario

# Criando uma instância da aplicação Flask
app = Flask(__name__)

# Definindo a rota para a página inicial
@app.route('/')
def home():
    # Aqui você diz: "Ei Flask, pegue o arquivo login.html e mostre pro usuário"
    # render_tamplate faz uma busca na pasta templates, então certifique-se de que seu login.html esteja lá
    return render_template('login.html')

# Definindo a rota para o login
@app.route('/login')
# A função login() é chamada quando o usuário acessa a rota /login, e é responsável por processar os dados do formulário de login
def login():
    # Pegando os dados do formulário de login usando request.args.get(), achando o valor de user e senha
    u = request.args.get('user')
    s = request.args.get('senha')

    # Adicionando print para ver se estamos recebendo os dados corretamente do HTML
    print(f"DEBUG: O que chegou do HTML -> Usuario: {u}, Senha: {s}")

    # Chamando a função indentificar_usuario para verificar se o usuário existe e a senha está correta
    resultado = indentificar_usuario(u, s)
    
    # Adicionando print para ver o que a função indentificar_usuario está retornando
    print(f"DEBUG: O que a função retornou -> {resultado}")

    if resultado:
        return "Logado com sucesso!"
    else:
        return "Negado!"



if __name__ == '__main__':
    # Iniciando a aplicação Flask em modo de depuração
    # .run() faz rodar a aplicação infinitamente, e debug=True é para facilitar o desenvolvimento, mostrando erros detalhados na página e toda vez
    # que você fizer uma mudança no código, a aplicação reinicia automaticamente.
    app.run(debug=True)