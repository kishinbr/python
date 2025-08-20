tupla = ('Lápis',1.75,'Borracha',2,'Caderno',15.90,'Estojo',25.00,'Transferido',4.20,'Compasso',9.99,'Mochila',120.32,'Canetas',22.30,'Livro',34.90)
print('-'*40)
print(f'{"Listagem de preco":^40}')
print('-'*40)
c=0
for c in range (0,len(tupla),2) :
    print(f'{tupla[c]}{"." * (30 - len(tupla[c]))}R${tupla[c+1]:7.2f}')
    print(f'{tupla[c]:.<30}R${tupla[c+1]:7.2f}')
print('-'*40)