cont = soma =0
n = int(input(f'Digite o {cont+1} numero[999 para parar]:'))
while n !=999 :
    cont += 1
    soma += n
    n = int(input(f'Digite o {cont+1} numero[999 para parar]:'))
print(f'A quantidade de numeros foi: {cont}')
print(f'A soma total dos numeros foi: {soma}')