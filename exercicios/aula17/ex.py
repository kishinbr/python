#lanche.append('sla') adiciona 1 item no final da lista
#lanche.insert(0,'algo') , adiciona na posicao , dps o nome

#del lanche[x] posicao
#lanche.pop[x] ultimo ou posicao
#lanche.remove[valor] valor escrito

#if pizza in lanche:
    #lanche.remove[pizza] 
#valores = list(range(4,11))
#4 5 6 7 8 9 10
#0 1 2 3 4 5 6 
#valores.sort()
#valores.sort(reverse=True)
#len(valores)
num = [2,5,9,2]
num[2]=num[3]
num.append(7)
num.insert(0,7)
num.sort(reverse=True)
num.pop()
print(num)
print(len(num))
if 5 in num:
    num.remove(5)
else:
    print('nao tem 5')
print(num)

valores = []
valores.append(5)
valores.append(6)
valores.append(7)
for v in valores:
    print(f'{v}..')
for i, v in enumerate(valores):
    print(f'pos {i} ta no numero {v}')
#
valores = list()
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))
for i, v in enumerate(valores):
    print(f'pos {i} ta no numero {v}')

a = [2,3,4,7]
b = a[:] #cria copia
b[2]=8
print(a , b)
