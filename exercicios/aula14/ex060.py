n = int(input('Digite um numero: '))
c = n
print(f'Calculando {n}!', end=' ')
while c!=1:
    if c ==n:
        fat = n
    fat = fat*(c-1)
    c -=1
    if c !=1:
        print(f'{c+1} x ', end='')
    else:
        print(f'{c+1} x {c} = ', end='')
print(f'{fat}')