s= 0
cont =0
for c in range(1,7):
    n = int(input(f'Digite {c} numero: '))
    if n%2==0:
        s = s+n
        cont += 1
print(f'Voce informou {cont} numeros pares')
print(f'A soma dos numeros pares foi: {s}')

