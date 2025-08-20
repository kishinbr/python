from random import randint
from time import sleep
dados = {}
dados['Jogador1'] = randint(1,6)
dados['Jogador2'] = randint(1,6)
dados['Jogador3'] = randint(1,6)
dados['Jogador4'] = randint(1,6)
print('Valores Sorteados:')
sleep(1)
for i,v in dados.items():
    print(f'     O {i} tirou {v}')
    sleep(0.5)
rank = dict(sorted(dados.items(),key = lambda item: item[1], reverse=True))
print('Ranking dos jogadores:')
c = 1
for i,v in rank.items():
    print(f'     {c}o Lugar: {i} com {v}')
    c+=1
    sleep(0.5)