n1 = float(input('Digite o primeiro lado: '))
n2 = float(input('Digite o segundo lado: '))
n3 = float(input('Digite o terceiro lado: '))

if n1+n2 > n3 and n2+n3 > n1 and n1+n3 > n2:
    print('Pode se formar um triangulo')
    if n1 == n2 == n3:
        print('O triangulo formado é EQUILATERO')
    elif n1 == n2 or n2 == n3 or n1 == n3:
        print('O triangulo formado é ISOCELES')
    else:
        print('O triangulo formado é ESCALENO')
else:
    print('NAO pode se formar um triangulo')
