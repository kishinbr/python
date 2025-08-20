def area (l,c):
    total = l*c
    print(f'A área de um terreno {l}x{c} é de {total:.1f}m2')


print('Controle de terreno')
print('-'*30)
area(float(input('LARGURA (m): ')),float(input('Comprimento (m): ')))