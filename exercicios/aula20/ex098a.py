from time import sleep
def contador(i,f,p):
    print('-='*30)
    print(f'Contagem de {i} até {f} de {abs(p)} em {abs(p)}')
    if i<f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.1)
            cont +=p
        print('!Fim')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.1)
            cont -=p
        print('!Fim')

    print('-='*30)

contador(1,10,1)
contador(10,0,2)
print(f'Agora é sua vez de personalizar a contagem!')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(inicio,fim,passo)
