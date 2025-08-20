def fatorial(num=1,show = True):
    """
    param num 0 numero a ser calculado
    paran show opc mostrar ou nao a conta
    return o valor do fotrial de um numero n
    """
    f = 1
    for c in range(num,0,-1):
        f *= c
        if show:
            print(f'{c} = ' if c == 1 else f'{c} x ', end='')
    return print(f'{f}')

numero = int(input('Digite um numero: '))
mostrar = (input('Deseja ver a conta?: ')).strip().upper()[0]
if mostrar == 'S':
    sim = True
else:
    sim= False
#fatorial(5,False)
fatorial(numero,sim)
