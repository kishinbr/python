maiorp = 0
menorp = 100000000000000
for c in range(1,6):
    peso = float(input('Digite um peso: '))
    if peso > maiorp:
        maiorp = peso
    if peso < menorp:
        menorp = peso
print(f'O maior peso é : {maiorp}')
print(f'O menor peso é : {menorp}')