p1 = int(input('Digite o primeiro termo da P.A: '))
ra = int(input('Digite a razao da P.A: '))
dec = p1 + (10-1) *ra
c = p1
while c != dec+ra:
    print(f'{p1} -> ', end='')
    p1 = p1+ra
    c = c+ra
print('Acabou')