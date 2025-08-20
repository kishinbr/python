def contador(i, f, p):
    if p == 0:
        p = 1  # Garante que o passo nunca seja zero
    
    if i > f and p > 0:
        p = -p  # Inverte o passo para contagem regressiva
    elif i < f and p < 0:
        p = -p  # Corrige passo negativo na contagem crescente
    
    print('-=' * 30)
    print(f'Contagem de {i} até {f} de {abs(p)} em {abs(p)}')

    if (i < f and p > 0) or (i > f and p < 0):
        for c in range(i, f + (1 if i < f else -1), p):
            print(f'{c} ', end='', flush=True)
    else:
        print('Não é possível realizar a contagem.')

    print('!Fim')
    print('-=' * 30)


# Testes
contador(1, 10, 1)
contador(10, 0, -2)

# Entrada do usuário
print(f'Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(inicio, fim, passo)