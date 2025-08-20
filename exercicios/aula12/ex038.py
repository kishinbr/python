num1 = float(input('Digite o primeiro numero: '))
num2 = float(input('Digite o segundo numero: '))
if num1 > num2:
    print(f'O numero 1: {num1} é maior que o numero 2: {num2}')
elif num2 > num1 :
    print(f'O numero 2: {num2} é maior que o numero 1: {num1}')
else:
    print(f'O numero 1 {num1} é igual o numero 2: {num2}')