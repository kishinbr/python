valores = []
while True:
    valores.append(int(input(f'Digite um numero: ')))
    while True:
        opc = input('Deseja continuar?[S/N]: ').strip().upper()[0]
        if opc not in 'SN':
            print('Resposta invalida:')
        else:
            break
    if opc == 'N':
        break
par = []
impar = []
for i in valores:
    if i % 2==0:
        par.append(i)
    else:
        impar.append(i)
print(f'A lista completa   é {valores}')
print(f'A lista de pares   é {par}')
print(f'A lista de impares é {impar}')
