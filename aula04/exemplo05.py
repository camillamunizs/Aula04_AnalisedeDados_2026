compra = float(input('Valor da Compra: '))
cliente_frequente = input('Programa de Fidelidade? [S/N]: ')

if compra > 100 or cliente_frequente == 's':
    print('Retire seu brinde!')
else:
    print('Sem brinde')