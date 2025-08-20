num = (int(input('Digite 1 numero: ')),int(input('Digite 2 numero: ')),int(input('Digite 3 numero: ')),int(input('Digite 4 numero: ')))
print(num)
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O numero 3 apareceu na {num.index(3)+1} posicao')
else:
    print(f'O numero 3 nao apareceu')
print(f'Os valores pares foram ', end='')
for n in num:
    if n% 2== 0:
        print(n, end=' ')