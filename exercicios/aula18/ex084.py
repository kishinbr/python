lista = list()
dado = list()
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    lista.append(dado[:])
    dado.clear()
    while True:
        opc = str(input('Deseja continuar?[S/N]: ')).strip().upper()[0]
        if opc not in 'NS':
            print('Resposta invalida')
        else:
            break
    if opc == 'N':
        break
print('-='*30)
print(f'Ao todo voce cadastrou {len(lista)}')
maior = []
menor = []

for p in lista:
    if p[1]>=100:
        maior.append(p[0])
    elif p[1]<=70:
        menor.append(p[0])
print(f'O maior peso foi de 100kg, Peso de {maior}')
print(f'O menor peso foi de 70kg, Peso de {menor}')

            
            

