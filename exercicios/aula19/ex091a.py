from random import randint
from time import sleep
from operator import itemgetter
jogo = {'Jogador1' : randint(1,6),
         'Jogador2' : randint(1,6),
         'Jogador3' : randint(1,6),
         'Jogador4' : randint(1,6)}
ranking = list()
print('Valores Sorteados:')
sleep(1)
for i,v in jogo.items():
    print(f'     O {i} tirou {v}')
    sleep(0.5)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('Ranking dos jogadores:')
for i,v in enumerate(ranking):
    print(f'     {i+1}o Lugar: {v[0]} com {v[1]}')
    sleep(0.5)