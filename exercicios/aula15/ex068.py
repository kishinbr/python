from random import randint
print('=-'*15)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-'*15)
v = 0
while True:
    n = int(input('Diga um valor: '))
    pi = ' '
    while pi not in 'PI':
        pi = str(input('Par ou Impar? [P/I]: ')).upper().strip()[0]
    npc = randint(0,10)
    print('-'*30)
    if (n+npc)% 2 ==0:
        print(f'Voce jogou {n} e o computador {npc}. Total deu {n+npc} DEU PAR')
        if pi in 'Pp':
            print('Voce VENCEU!')
            v+=1
        else:
            print('Voce PERDEU!')
            break
    else:
        print(f'Voce jogou {n} e o computador {npc}. Total deu {n+npc} DEU IMPAR')
        if pi in 'Ii':
            print('Voce VENCEU!')
            v+=1
        else:
            print('Voce PERDEU!')
            break
    print('-'*30)
    print('Vamos jogar novamente...')
    print('=-'*15)
print('=-'*15)
print(f'GAME OVER! Voce venceu {v} vezes.')
