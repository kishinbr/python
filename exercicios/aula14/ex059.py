from time import sleep
choice = 0
n1 = float(input('Digite o 1 numero: '))
n2 = float(input('Digite o 2 numero: '))
while choice != 5:
    print('='*40)
    print('Oque deseja fazer:')
    print('''[1]SOMAR\n[2]MULTIPLICAR\n[3]MAIOR\n[4]NOVOS NUMEROS\n[5]SAIR DO PROGRAMA''')
    choice = int(input('Escolha uma opcão: '))
    if choice ==1:
        print(f'A soma entre {n1} e {n2} é igual a {n1+n2}')
    elif choice ==2:
        print(f'A multiplicacao entre {n1} e {n2} é igual a {n1*n2}')
    elif choice==3:
        if n1 > n2:
            print(f'O maior numero entre entre {n1} e {n2} é igual a {n1}')
        else:
            print(f'O maior numero entre entre {n1} e {n2} é igual a {n2}')
    elif choice==4:
        print('Digite os novos numeros: ')
        n1 = float(input('Digite o 1 numero: '))
        n2 = float(input('Digite o 2 numero: '))
    elif choice==5:
        print('Finalizando..')
    else:
        print('Digite uma opcao valida')
    sleep(2)
print('='*40)
print('Voce escolheu: [5]Sair do programa')
    

