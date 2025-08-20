lanche = ('Hamburguer', 'Suco' , 'Pizza', 'Pudim')

for coint in range(0, len(lanche)): #igual
    print(f'Eu vou comer 1 {lanche[coint]}')
for comida in lanche:
    print(f'Eu vou comer 2 {comida}')#igual

for pos, comida in enumerate(lanche): #nome e posicao
    print(f'Eu vou comer 3 {comida} na posicao {pos}')
    
a = (2,5,4)
b = (5,8,1,2)
c = a+b
d = b+a
print(c)
print(d)
print(c.count(5))
print(d.index(5)) #posicao q ta o 5
print(d.index(5,1))#posicao q ta o 5 dps da 1 pos
print(sorted(lanche)) #alfabetico
g = ('arroz', '40kg')
del(g)


