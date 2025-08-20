numero = [list(),list()]
for c in range(1,8):
    num = int(input(f'Digite o {c}o. valor: '))
    if num % 2 ==0:
        numero[0].append(num)
    else:
        numero[1].append(num)
numero[0].sort()
numero[1].sort()
print(f'Os valores pares digitados foram  : {numero[0]}')
print(f'Os valores impares digitados foram: {numero[1]}')