continuar = 'S'
cont = 0
soma = 0
while continuar == 'S':
    n = int(input('Digite um numero: '))
    continuar = input('Deseja continuar? [S/N]: ').strip().upper()
    soma = soma + n
    cont = cont+1
    if cont == 1:
        menor = n
        maior = n
    if n < menor: 
        menor = n
    if n > maior:
        maior = n
print(f'Foram digitados {cont} numeros')
print(f'A media foi {soma/cont:.2f}')
print(f'O maior numero foi {maior}')
print(f'O menor numero foi {menor}')
