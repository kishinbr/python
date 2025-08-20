continuar = 'S'
cont = soma = 0
while continuar in 'Ss':
    n = int(input('Digite um numero: '))
    soma = soma + n
    cont = cont+1
    if cont == 1:
        menor = maior = n
    else:
        if n < menor: 
            menor = n
        if n > maior:
            maior = n
    continuar = input('Deseja continuar? [S/N]: ').upper().strip()[0]
print(f'Foram digitados {cont} numeros')
print(f'A media foi {soma/cont:.2f}')
print(f'O maior numero foi {maior}')
print(f'O menor numero foi {menor}')
