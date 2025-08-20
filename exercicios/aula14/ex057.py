sexo = str(input('Digite sexo [F/M]')).strip().upper()[0]
while sexo not in 'MF':
    print('Erro.')
    sexo = str(input('Digite sexo [F/M]')).strip().upper()
print(f'Sexo {sexo} registrado')