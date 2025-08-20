numero = []
par = []
impar = []
for c in range(1,8):
    num = int(input(f'Digite o {c}o. valor: '))
    if num % 2 ==0:
        par.append(num)
    else:
        impar.append(num)
par.sort()
impar.sort()
numero.append(par[:])
numero.append(impar[:])
print(f'Os valores pares digitados foram  : {numero[0]}')
print(f'Os valores impares digitados foram: {numero[1]}')