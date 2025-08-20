n1 = float(input('Digite o 1 numero: '))
n2 = float(input('Digite o 2 numero: '))
choice=0
while choice !=5:
    print('''    [1]SOMAR
    [2]MULTIPLICAR
    [3]MAIOR
    [4]NOVOS NUMEROS
    [5]SAIR DO PROGRAMA''')
    choice = int(input('Oque deseja fazer:'))
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
    print('=-='*10)
print('FIM DO PROGRAMA! VOLTE SEMPRE!')