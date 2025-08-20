e = [input('Digite a expressao: ')]
aberto = 0
for i in e[0]:
    if i == '(':
        aberto +=1
    elif i == ')':
        aberto -=1
        if aberto <0:
            break
if aberto == 0:
    print('Expressao valida')
else : 
    print('Expressao invalida')  