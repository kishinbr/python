numero = ('Zero','Um','Dois','Tres','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez')
while True:
    while True:
        n = int(input('Digite um numero entre 0 e 10: '))
        if 0 <= n <=10:
            break
        print('Tente novamente.', end=' ')
    print(f'Numero escolhido foi {n} e por extenso se le {numero[n]}')
    while True:
        opc = input('Deseja continuar?[S/N]: ').strip().upper()[0]
        if opc in 'NS':
            break
    if opc == 'N':
        break

        
    


