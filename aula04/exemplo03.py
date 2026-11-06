pontos = int(input('Informe a quantidade de pontos: '))

if pontos >= 100: 
    pontos = pontos + 10
    print(f'Parabéns! Você tem {pontos} agora!')

elif pontos >= 50:
    pontos = pontos + 5
    print(f'Bom desempenho! Você tem {pontos} agora!')

else:
    print(f'Não foi desta vez, mas continue tentando! Seus pontos: {pontos}')