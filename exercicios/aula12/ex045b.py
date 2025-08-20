import random
import time
pc = random.randint(1,3)
print('1 - TESOURA\n2 - PEDRA\n3 - PAPEL')
p = int(input('Escolha oque vai jogar: '))

if pc == 1 and p == 1:
    pcj ='TESOURA'
    pj = 'TESOURA'
    res = 'EMPATE'
elif pc == 2 and p == 1:
    pcj ='PEDRA'
    pj = 'TESOURA'
    res = 'DERROTA'
elif pc == 3 and p == 1:
    pcj ='PAPEL'
    pj = 'TESOURA'
    res = 'VITORIA'
elif pc == 1 and p == 2:
    pcj ='TESOURA'
    pj = 'PEDRA'
    res = 'VITORIA'
elif pc == 1 and p == 3:
    pcj ='TESOURA'
    pj = 'PAPEL'
    res = 'DERROTA'
elif pc == 2 and p == 2:
    pcj ='PEDRA'
    pj = 'PEDRA'
    res = 'EMPATE'
elif pc == 2 and p == 3:
    pcj ='PEDRA'
    pj = 'PAPEL'
    res = 'VITORIA'
elif pc == 3 and p == 3:
    pcj ='PAPEL'
    pj = 'PAPEL'
    res = 'EMPATE'
elif pc == 3 and p == 2:
    pcj ='PAPEL'
    pj = 'PEDRA'
    res = 'DERROTA'
else:
    print('JOGADA INVALIDA')
    
print('JO')
time.sleep(0.5)
print('KEN')
time.sleep(0.5)
print('PO')
time.sleep(1)
print('-=-'*15)
print(f'Voce jogou {pj}')
print(f'Maquina jogou {pcj}')
print(f'O resultado da partida foi : {res}')
print('-=-'*15)


