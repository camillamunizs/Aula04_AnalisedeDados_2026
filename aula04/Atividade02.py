salario = float(input('Informe o salário: R$ '))
vendas = float(input('Informe o valor da venda: R$ '))

if vendas >= 1000: 
    vendas = salario + 150
    print(f'Sua remuneração total: R$ {vendas:.2f} ')

elif vendas >= 500:
    vendas = salario + 75
    print(f'Sua remuneração total: R$ {vendas:.2f} ')

else:
    print(f'Sua remuneração sem bônus será: R$ {salario:.2f}')