sal = float(input('Digite o salario: '))
if sal > 1250:
    print(f'Recebera aumento de 10% e o valor sera R${sal*1.10:.2f}')
else:
    print(f'Recebera aumento de 15% e o valor sera R${sal*1.15:.2f}')