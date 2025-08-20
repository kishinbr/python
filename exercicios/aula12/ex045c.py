from random import randint
itens = ('PEDRA' , 'PAPEL' , 'TESOURA')
computador = randint(0,2)
print('''Sua opcoes:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Escolha uma jogada: '))
print('-='*11)
print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('-='*11)

if computador == 0:
    if jogador ==0:
        print('EMPATE')
    elif jogador ==1:
        print('VITORIA')
    elif jogador ==2:
        print('DERROTA')
    else:
        print('JOGADA INVALIDA')

elif computador == 1:
    if jogador ==0:
        print('DERROTA')
    elif jogador ==1:
        print('EMPATE')
    elif jogador ==2:
        print('VITORIA')
    else:
        print('JOGADA INVALIDA')
elif computador == 2:
    if jogador ==0:
        print('VITORIA')
    elif jogador ==1:
        print('DERROTA')
    elif jogador ==2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA')