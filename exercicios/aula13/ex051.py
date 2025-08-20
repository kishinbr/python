p1 = int(input('Digite o primeiro termo da P.A: '))
ra = int(input('Digite a razao da P.A: '))
for c in range(1,11):
    if c ==1:
        pa = p1
    pa = pa + ra
    print(f'{pa-ra} -> ', end='')
print('Acabou')