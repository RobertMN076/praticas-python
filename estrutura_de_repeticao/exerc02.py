nome_de_usuario = str(input('Digite seu nome de usuário:'))
senha = input('Digite sua senha:')

while senha == nome_de_usuario:
    print('Erro: Login e senha iguais')
    nome_de_usuario = str(input('Digite outro usuário:'))
    senha = input('Digite outra senha:')
print('Login concluído')