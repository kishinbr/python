matriz = [[0,0,0],[0,0,0],[0,0,0]]
par = col3 = mai2 = 0
for l in range (0,3):
    for c in range (0,3):
        matriz[l][c] = int(input(f'Digite um valor para posicao [{l}, {c}] '))
        if matriz[l][c] % 2 ==0:
            par += matriz[l][c]
        if c ==2:
            col3 += matriz[l][c]
        if (l == 1 and c == 0) or matriz[1][c]> mai2:
            mai2 = matriz[l][c]
print('-='*20)
for l in range (0,3):
    for c in range (0,3):
        print(f'[{matriz[l][c]:^3}] ', end='')
    print()
print('-='*20)
print(f'A soma dos valores pares é {par}')
print(f'A soma dos valores da terceira coluna é {col3}')
print(f'O maior valor da segunda linha é {mai2}')