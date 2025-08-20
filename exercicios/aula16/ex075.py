n1 = int(input('Digite 1 numero: '))
n2 = int(input('Digite 2 numero: '))
n3 = int(input('Digite 3 numero: '))
n4 = int(input('Digite 4 numero: '))
tupla = (n1,n2,n3,n4)
c = cont9 = contpar  = d =0
po = -1
while c < 4:
    if tupla[c] == 9:
        cont9 = cont9+1
    if tupla[c] == 3:
        po = c
    c+=1
print(f'Voce digitou os valores: {tupla}')
print(f'O valor 9 apareceu {cont9} vezes')
if po > 0:
    print(f'O valor 3 apareceu na {po+1} posicao')
else:
    print(f'O valor 3 nao apareceu')
print(f'Os valores pares digitados foram', end=' ')
while d < 4:
    if tupla[d]%2 ==0:
        print(f'{tupla[d]}', end=' ')
    d +=1
        