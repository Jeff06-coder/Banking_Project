# Banking_Project
Esse projeto é para estudo e geração de conhecimento. O objetivo é criar o uso de contas bancárias simples, onde tem indentificação de senhas e usuários, com o funcionamento de saldo (saque e depósito). Pode incluir também o uso de servidor, e usar suas rotas + soluções de erros.

## 🛠️ Configuração Inicial do Projeto

Para este projeto de sistema bancário, seguimos as melhores práticas de desenvolvimento backend:

1. **Isolamento de Ambiente**: Foi criado um ambiente virtual para gerenciar dependências de forma segura e para evitar erros de execução com sua máquina.
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt

2. **Instalação de Dependências**: Utilizado o pip para instalar o Framework Flask. Use o *pip install -r requirements.txt* para instalar as dependências.
    ```bash
    pip install flask
    pip freeze > requirements.txt  


## app.py
É a página principal do projeto, onde esta a ligação do servidor, as transições de páginas e sistema de segurança. O coração do projeto, onde o backend e frontend se encontram e trabalham juntos. 

*app.route*: Está carregando suas functions e definindo sua local de operação. Nele é executado a função e seus devidos códigos, um processo feito na quela página, como verificações e redirecionamentos a outros route também.

*from* e *import*: É a importação de uma biblioteca ao seu código ou de arquivos diferentes feitos.

**É possivél encontrar mais informações no código, pois de acordo com que você vai navegando, vai vendo meus comentários atravez dos códigos sobre meu intendimentos.**

## users.py
É onde está armazenado os usuários e suas informações, nele á uma função que faz válidação desses usuários também.

## templates
A *pasta* templates tem em si, arquivos *.html* para serem usados como interfaces, que são redirecionados ao *app.py*. Dentro desses arquivos, á a presença de estilização da página e seus dados, são passados os dados para o app.py usando metodos HTTPS e ações como *from* e *actions*.
