valores = list()
for cont in range(0,5):
    valores.append(int(input(f'Digite um valor para Posicao {cont}: ')))
print(valores)
print(f'Maior numero foi {max(valores)} na posicaos ', end='')
for i , n in enumerate(valores):
    if n == max(valores):
        print(f'{i}... ', end='')
print(f'\nMenor numero foi {min(valores)} na posicaos ', end='')
for i , n in enumerate(valores):
    if n == min(valores):
        print(f'{i}... ', end='')
