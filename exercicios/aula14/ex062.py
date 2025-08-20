p1 = int(input('Digite o primeiro termo da P.A: '))
ra = int(input('Digite a razao da P.A: '))
dec = p1 + (10-1) *ra
c = p1
while c != dec+ra:
    print(f'{p1} -> ', end='')
    p1 = p1+ra
    c = c+ra
print('Acabou')
resp = ''
while resp !='N':
    resp = input('\nDeseja ver mais termos? [S/N]: ').strip().upper()
    if resp == 'S':
        mt = int(input('Digite quantos termos deseja ver: '))
        ulterm = p1 + (mt-1) *ra
        while c != ulterm + ra:
            print(f'{p1} -> ', end='')
            p1 = p1+ra
            c = c+ra
        if c == ulterm + ra:
            print(f'Acabou')
    elif resp not in 'NS':
        print('Digite opcao valida')
    else:
        print('Decidiu parar')
    ultimon = p1
print(f'Programa finalizado')



    




