from users import users

# Função para processar operações de depósito e saque
def processar_operacao(usuario_id, tipo, valor):
    
    # Buscamos o usuário no dicionário
    usuario = users.get(usuario_id)

    if not usuario:
        return False, "Usuário não encontrado"
    
    if tipo == 'sacar':
        if valor <= usuario['saldo']:
            usuario['saldo'] -= valor
            return True, f"Saque de R$ {valor} realizado com sucesso. Saldo atual: R$ {usuario['saldo']}"
        else:
            return False, "Saldo insuficiente"
        

    elif tipo == 'depositar':
        usuario['saldo'] += valor
        return True, f"Depósito de R$ {valor} realizado com sucesso. Saldo atual: R$ {usuario['saldo']}"
    
    return False, "Tipo de operação inválida"
