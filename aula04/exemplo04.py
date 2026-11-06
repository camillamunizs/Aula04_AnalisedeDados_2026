nome = input('Nome do Usuário: ')
senha = input('Digite a senha: ')

if nome == 'admin' and senha == '1234':
    print('Login realizado com sucesso!')
else:
    print('Usuário ou senha incorreto.')
