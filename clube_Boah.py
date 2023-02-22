import re
def login():
    user='sam'
    passaword='1234'

    answer_user=input('Digite o nome do seu usuário ')
    answer_password=input('Digite a senha do seu usuário ')

    if answer_user==user and answer_password==passaword:
        print('Olá '+user+'. Seja bem vindo!')
    else:
        print('######### \n'
              'Dados inseridos incorretos! \n'
              'Você tem mais 3 chances \n'
              '#########')
        attempt =0

        while answer_user != user or answer_password != passaword:
            answer_user = input('Digite novamente o nome do seu usuário ')
            answer_password = input('Digite novamente a senha do seu usuário ')
            attempt += 1
            if attempt >= 3:
                print('Acesso Negado. Reinicie o programa e tente novamente')
                break

def confirmacao_cadastro(user,password, conf_password, email, CPF):
    print("Carregando...")
    val_CPF=1
    val_user=1
    val_password=1
    val_email= 1

    if user.__len__()<2:
        print('Nome inválido. O nome deve conter mais que dois caracteres')
        val_user= -1

    if password != conf_password:
        print('Senhas diferentes')
        val_password= -1

    email_regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'#error
    res=re.search(email_regex, email)
    if (res == None):
        print("Email inválido")
        val_email = -1

    cpf_regex = '^\d{3}\.\d{3}\.\d{3}\-\d{2}$'
    if re.search(cpf_regex, cpf) == None:
        print('CPF inválido')
        val_CPF= -1

    if val_CPF== -1 or val_user== -1 or val_password== -1 or val_email == -1:#error
       print("Erro no Cadastro. Tente novamente ")

    else:
        print("Cadastro realizado com sucesso. Seja bem vindo "+user)

nome= input("Olá. Qual opção você deseja, Cadastro ou login? ")
resposta= nome.upper()

if resposta=='LOGIN':
    login()
elif resposta == "CADASTRO":
    print('Vamos realizar o cadastro...')
    user = input('Digite seu nome: ')
    password = input('Digite sua senha: ')
    conf_password = input('Confirme sua senha: ')
    email = input('Digite seu email: ')
    cpf = input('Digite seu CPF: ')
    confirmacao_cadastro(user,password, conf_password, email, cpf)
else:
    print('Opção inválida. Tente novamente')