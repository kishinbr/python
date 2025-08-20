flag = 1
cont = 0
soma = 0
numerorandom = 1
while flag !=999 :
    print('Se quiser parar digite 999')
    n = int(input(f'Digite o {cont+1} numero: '))
    if n !=999:
        cont += 1
        soma = soma + n
    else:
        flag=n
        print('Finalizado')
print(f'A quantidade de numeros foi: {cont+1}')
print(f'A soma total dos numeros foi: {soma}')
        
    



