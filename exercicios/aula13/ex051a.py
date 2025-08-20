p1 = int(input('Digite o primeiro termo da P.A: '))
ra = int(input('Digite a razao da P.A: '))
dec = p1 + (10-1) *ra
for c in range(p1, dec+ra , ra):
    print(f'{c} -> ', end='')
print('Acabou')