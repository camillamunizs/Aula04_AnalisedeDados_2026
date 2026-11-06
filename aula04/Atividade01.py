valor_compra = float(input('Informe o valor da compra: '))


if valor_compra > 250:
    desconto = valor_compra * 0.16
    total = valor_compra - desconto
    print(f'Desconto de R$ {desconto:.2f}. \nTotal a pagar: R${total} ')

else:
    print(f'O valor sem desconto é R$ {valor_compra:.2f} ')
    







