def contador(i,f,p):
    if f ==i:
        print(f'Não é possivel realizar a contagem')
    if p ==0:
        p=1
    if i > f and p > 0:
        p = abs(p)
        p = -p
        f = f-1
    if f > i:
        p = abs(p)
        f = f+1
    print('-='*30)
    print(f'Contagem de {i} até {f} de {abs(p)} em {abs(p)}')
    #for c in range(i,f,p): 
    for c in range(i, f, p):
        print(f'{c} ', end='')
    print('!Fim')
    print('-='*30)

contador(1,10,1)
contador(10,0,-2)
print(f'Agora é sua vez de personalizar a contagem!')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(inicio,fim,passo)
