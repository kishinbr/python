p1 = int(input('Digite o primeiro termo da P.A: '))
ra = int(input('Digite a razao da P.A: '))
termo = p1
cont = 1
total = 0
mais = 10
qtermo = mais
while mais !=0:
    total = total + mais
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo += ra
        cont +=1
    print(f'Pausa')
    mais = int(input('Quanto termos voce quer ainda ver?: '))
    qtermo = qtermo + mais
print(f'Acabou com {qtermo} termos')
