n = int(input('Digite um numero: '))
for c in range(n , 1 , -1):
    if c ==n:
        fat = n
    fat = fat*(c-1)
print(f'O fatorial de {n}! = {fat}')