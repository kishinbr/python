maiorp = 0
menorp = 0
for c in range(1,6):
    peso = float(input(f'Peso da {c} pessoa: '))
    if c ==1:
        maiorp = peso
        menorp = peso
    else:
        if peso > maiorp:
            maiorp = peso
        if peso < menorp:
            menorp = peso
print(f'O maior peso é : {maiorp}')
print(f'O menor peso é : {menorp}')