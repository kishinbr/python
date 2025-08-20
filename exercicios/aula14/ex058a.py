from random import randint
computador = randint(0,10)
print('SOU SEU COMPUTADOR... Acabei de pensar em um numero entre 0 e 10')
print('Sera que voce consegue adivinhar qual foi?')
acerto = False
palpites = 0
while not acerto:
    jogador = int(input('Qual o seu palpite? '))
    palpites += 1
    if jogador ==computador:
        acerto = True
    else:
        if jogador < computador:
            print('Mais.. Tente novamente')
        else:
            print('Menos.. Tente novamente')
print(f'Acertou com {palpites} tentativas')