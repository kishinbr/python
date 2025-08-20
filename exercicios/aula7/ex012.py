preco = float(input('Qual é o preco do produto? R$'))
print(f'O produto que custava R${preco}, na promoçao com desconto de 5% vai custar R${preco - ((preco*5)/100):.2f}')