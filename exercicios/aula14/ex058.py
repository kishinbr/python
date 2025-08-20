import random
import time
n = random.randint(1,10)
n1 = 0
erro = 1
print('Eu pensei em um numero entre 1 e 10, será que voce consegue adivinhar?')
while n1 != n:
    n1 = int(input('Digite um numero entre 1 e 10: '))
    print('PROCESSANDO...')
    time.sleep(0.5)
    if n == n1:
        print(f'PARABENS! Voce acertou o numero {n} em {erro} tentativas')
    else:
        erro +=1
        if n1 > n:
            print(f'Menos..., tente novamente')
        else:
            print(f'Mais..., tente novamente')