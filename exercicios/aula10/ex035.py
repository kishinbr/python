n1 = float(input('Digite o primeiro lado: '))
n2 = float(input('Digite o segundo lado: '))
n3 = float(input('Digite o terceiro lado: '))

if n1+n2 > n3 and n2+n3 > n1 and n1+n3 > n2:
    print('Pode se formar um triangulo')
else:
    print('NAO pode se formar um triangulo')