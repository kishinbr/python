p1 = int(input('Digite o primeiro termo da P.A: '))
ra = int(input('Digite a razao da P.A: '))
termo = p1
cont = 1
while cont <11:
    print(f'{termo}',end='')
    print(' -> ' if cont < 10 else ' ', end='')
    termo += ra
    cont += 1
print('FIM')