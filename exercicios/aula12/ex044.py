preco = float(input('Digite o preco R$: '))
print("OPCOES DE PAGAMENTO:")
print("-1: A vista dinheiro/cheque/pix: 10% de desconto")
print("-2: A vista no cartao: 5% de desconto")
print("-3: Em ate 2x no cartão")
print("-4: 3x ou mais no cartão: 20% de juros")
choice = int(input('INFORME A OPCAO DE PAGAMENTO:'))

if choice == 1:
    print('Metodo escolhido foi: 1 - A VISTA')
    print(f'O valor a ser pago do produto é R$ {preco-(preco*0.1)}')
elif choice == 2 :
    print('Metodo escolhido foi: 2 - A VISTA NO CARTAO')
    print(f'O valor a ser pago do produto é R$ {preco-(preco*0.05)}')
elif choice == 3 :
    print('Metodo escolhido foi: 3 - 2X NO CARTAO')
    print(f'O valor a ser pago do produto é R$ {preco} e cada parcela será de {preco/2}')
else:
    print('Metodo escolhido foi: 4 - 3X OU MAIS NO CARTAO')
    quant = int(input('Quantas vezes?: '))
    print(f'O valor a ser pago do produto é R$ {preco+(preco*0.2)} e suas parcelas serao de R${(preco+(preco*0.2))/quant}')
