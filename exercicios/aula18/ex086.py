lista = [list(),list(),list()]
for c in range(0,3):
    num = int(input(f'Digite um valor para [0, {c}]: '))
    lista[0].append(num)
for c in range(0,3):
    num = int(input(f'Digite um valor para [1, {c}]: '))
    lista[1].append(num)
for c in range(0,3):
    num = int(input(f'Digite um valor para [2, {c}]: '))
    lista[2].append(num)
print('-='*30)
print(lista[0])
print(lista[1])
print(lista[2])
