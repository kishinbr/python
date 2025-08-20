km = float(input('Qual a distancia da sua viagem? em KM: '))
if km <=200:
    print(f'O preco da sua passagem é {km*0.5:.2f}')
else:
    print(f'O preco da sua passagem é {km*0.45:.2f}')