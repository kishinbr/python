from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I]: ')).upper().strip()[0]
    print(f'Voce jogou {jogador} e o computador {computador}. Total de {total}')
    if tipo == 'P':
        if total % 2 ==0:
            print('Voce Venceu')
            v +=1
        else:
            print('Voce Perdeu')
            break
    elif tipo == 'I':
        if total % 2 ==0:
            print('Voce Venceu')
            v +=1
        else:
            print('Voce Perdeu')
            break
    print('Vamos tentar novamente..')
print(f'GAME OVER! Voce venceu {v} vezes')
