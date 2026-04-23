# Criando usuarios
users = {
    'Alice': {
        'senha': '1234',
        'saldo' : 1000
},
    'Bob': {
        'senha': '5678',
        'saldo' : 500
},
    'Jefferson': {
        'senha': 'adm',
        'saldo' : 99999999
},
}

# Função para identificar o usuário e liberar o acesso
def indentificar_usuario(username, password):
    user = users.get(username)
    if user and user['senha'] == password:
        return user
    return None