n = int(input('Digite um numero: '))
divisores = 0
for c in range (1,n+1):
    if n%c ==0:
       # print(n,c)
        divisores = divisores + 1
if divisores >= 3:
    print(f'O numero {n} não é um numero primo')
elif n ==1:
    print(f'O numero {n} NAO CONTA COMO um numero primo')
else:
    print(f'O numero {n} é um numero primo')
