from random import randint
menor = maior = 0

for c in range (1,6):
    n = randint(0,10)
    if c == 1:
        menor = n
        maior = n
        n1 = n
    elif c==2:
        n2 = n
    elif c==3:
        n3 = n
    elif c==4:
        n4 = n
    else:
        n5 = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
tupla = (n1,n2,n3,n4,n5)
print('O valores sorteados foram: ', end='')

for pos,sla in enumerate(tupla):
    print(f'{sla}', end=' ')

print(f'\nO maior {maior} e o menor {menor}')
