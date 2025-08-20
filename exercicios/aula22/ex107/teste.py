import moedas

p = float(input('Digite o preco R$: '))
print(f'A medate de {p} é {moedas.metade(p)}')
print(f'O dobro de {p} é {moedas.dobro(p)}')
print(f'Aumentando 10%, temos {moedas.aumentar(p,10)}')
print(f'Reduzindo 13%, temos {moedas.diminuir(p,13)}')