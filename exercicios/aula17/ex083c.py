expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append(simb)
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(simb)
            break
if len(pilha)== 0:
    print('Sua expressao esta valida')
else:
    print('Sua expressao esta invalida')