n = int(input('Digite um numero: '))
divisores = 0
for c in range(1, n+1):
    if n%c ==0:
        divisores +=1
        print(f'\033[31m{c}\033[0m', end=' ')
    else:
        print(f'\033[34m{c}\033[0m' , end=' ')
if divisores == 2:
    primo = 'é Primo'
else:
    primo = 'Não é primo'
print(f'\nO numero {n} foi divisivel {divisores} vezes')
print(f'Por isso o numero {n} {primo}')