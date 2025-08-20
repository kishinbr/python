import moeda 

p = float(input('Digite o preco R$: '))
print(f'A medate de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10%, temos {moeda.aumentar(p,10)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p,13)}')