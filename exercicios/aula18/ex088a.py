from time import sleep
from random import randint
lista = []
jogos = list()
print('-'*40)
print(f'{"JOGA NA MEGA SENA":^40}')
print('-'*40)
quant = int(input('Quantos jogos voce quer que eu sortei: '))
tot=1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont +=1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot +=1
print(f'-='*3,f' SORTEANDO {quant} JOGOS ',f'-='*3)
for i , l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
