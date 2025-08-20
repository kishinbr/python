def l():
    print('-'*30)


def mensagem(msg):
    print('-'*30)
    print(msg)
    print('-'*30)


l()
print('Eu sou foda')
l()

mensagem('Eu sou foda')

def soma(a,b):
    print(a+b)
    
#soma(int(input('Digite 1 numero:')),int(input('Digite 2 numero:')))

def soma1(c,d):
    print(f'C = {c} e D = {d}')
    s = c+d
    print(f'A soma C + D = {s}')


soma1(4,5)
soma1(c=5,d=4)


def contador(*num):
    for valor in num:
        print(f'{valor}', end=' ')
    print('Fim!')

    tam = len(num)
    print(f'Recebi os valores {num} e sao ao todo {tam} numeros')

contador(2,1,7)
contador(8,0)
contador(4,4,7,6,2)

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *=2
        pos +=1
    print(f'{lst}')

valores = [7,2,5,0,4]
print(valores)
dobra(valores)

def somar2(*valores):
    s = 0
    for num in valores:
        s+=num
    print(f'Somando os {valores} = {s}')


somar2(5,2)
somar2(2,9,4)
