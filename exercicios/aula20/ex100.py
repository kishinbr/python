from random import randint
numeros = list()
def sorteia(lst):
    print(f'Sorteando 5 valores da lista: ' , end='')
    for c in range(0, 5):
        lst.append(randint(1,10))
        print(f'{lst[c]} ', end='')
    print('Pronto!')
def somaPar(lst):
    somap = 0
    for c in lst:
        if c %2==0:
            somap +=c
    print(f'Somando os valores pares de {lst}, temos {somap} ')

sorteia(numeros)
somaPar(numeros)