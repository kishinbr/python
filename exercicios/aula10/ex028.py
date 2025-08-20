import random
import time
n = random.randint(0,5)
print('Eu pensei em um numero entre 0 e 5, será que voce consegue adivinhar?')
n1 = int(input('Digite um numero entre 0 e 5: '))
print('PROCESSANDO...')
time.sleep(1)
if n == n1:
    print('PARABNES! Voce acertou o numero')
else:
    print(f'Voce errou, o numero escolhido foi {n}')
