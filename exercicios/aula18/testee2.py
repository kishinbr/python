from random import randint
from time import sleep
print('-'*40)
print(f'{"JOGA NA MEGA SENA":^40}')
print('-'*40)
lista = []
dados = []
jogos = int(input('Quantos jogos voce quer que eu sorteie?: '))
for c in range (0,jogos):
    for d in range(0,6):
        dados.append(randint(0,10))
    dados.sort()
    lista.append(dados[:])
    dados.clear()
for c in range(0,jogos):
    print(f'Jogo {c+1}: {lista[c]}')
    sleep(0.5)
print(f'{" < Boa sorte > ":=^40}')