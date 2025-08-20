tupla = ('Lápis',1.75,'Borracha',2,'Caderno',15.90,'Estojo',25.00,'Transferido',4.20,'Compasso',9.99,'Mochila',120.32,'Canetas',22.30,'Livro',34.90)
print('-'*40)
print(f'{"Listagem de preco":^40}') #centralizado
print('-'*40)

for pos in range (0, len(tupla)):
    if pos %2 ==0:
        print(f'{tupla[pos]:.<31}', end='') #alinhado a esquerda cheio de pontos
    else:
        print(f'R${tupla[pos]:7.2f}')#7espacos.2f apos virgula