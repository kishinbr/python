print('='*30)
print(f'{"BANCO CEV":^30}')
print('='*30)
n = int(input('Que valor voce quer sacar?: R$'))
q50 = q20 = q10 = q1 = 0
while True:
    if n >= 50:
        n = n-50
        q50 +=1
    elif n >=20:
        n = n -20
        q20 +=1
    elif n >= 10:
        n = n -10
        q10 +=1
    elif n>=1:
        n = n -1
        q1 +=1
    else:
        break
if q50 > 0:
    print(f'Total de {q50} cedulas de R$50')
if q20 > 0:
    print(f'Total de {q20} cedulas de R$20')
if q10 > 0:
    print(f'Total de {q10} cedulas de R$10')
if q1 > 0:
    print(f'Total de {q1} cedulas de R$1')
print('='*20)
print('Volte sempre ao BANCO CEV!')

