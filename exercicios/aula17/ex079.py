valores = []
while True:
    num = (int(input(f'Digite um numero: ')))
    if num in valores:
        print("VALOR IGUAL! Tente novamente.")
    else:
        valores.append(num)
    while True:
        opc = input('Deseja continuar?[S/N]: ').strip().upper()[0]
        if opc not in 'SN':
            print('Resposta invalida:')
        else:
            break
    if opc == 'N':
        break
valores.sort()
print(f"{valores}")


