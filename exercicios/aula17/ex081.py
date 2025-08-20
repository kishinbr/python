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
print('-='*20)
print(f'Voce digitou {len(valores)} elementos')
valores.sort(reverse=True)
print(f"{valores}")
if 5 in valores:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 nao faz parte da lista')