dias = int(input('Quantos dias o carro foi alugado?: '))
km = float(input('Quantos Km foram percorridos?: '))
print(f'O preço total a se pagar é R${(km*0.15) + (dias*60):.2f}')