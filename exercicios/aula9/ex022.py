nome = input('Digite o seu nome completo:')
#nome = str(input('Digite o seu nome completo:')).strip
print(f'Seu nome em maisuculas é : {nome.upper()}')
print(f'Seu nome em minuscula é : {nome.lower()}')
divido = nome.split()

voltando = ''.join(divido)
print(f'Seu nome completo possui : {len(voltando)} letras')
print(f"Seu nome completo possui : {len(nome)-nome.count(' ')} letras")

print(f"Seu primeiro nome {nome.find(' ')}")
print(f'Seu primeiro nome {divido[0]} possui : {len(divido[0])} letras')
#print(len(voltando))
#print(len(divido[0]))