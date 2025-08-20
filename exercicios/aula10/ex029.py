vel = float(input('Digite a velocidade do carro: '))
if vel > 80:
    print('Voce ultrapassou o limite permitido de 80 km/h')
    print(f'Voce foi multado em R${(vel-80)*7:.2f} ')
else:
    print('Voce nao possui multas')
    print('Parabens por ser um bom condutor')