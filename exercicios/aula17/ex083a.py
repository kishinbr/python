expressao = input('Digite a expressão: ')
pilha = []
for caractere in expressao:
    if caractere == '(':
        pilha.append('(')  # Adiciona à pilha quando encontra um '('
    elif caractere == ')':
        if len(pilha) > 0:  # Se há um '(' na pilha, remove ele
            pilha.pop()
        else:  # Se não há '(' para fechar, a expressão já é inválida
            print('EXPRESSÃO INVÁLIDA aaaa')
            break
else:
    if len(pilha) == 0:  # Se a pilha está vazia, todos os '(' foram fechados corretamente
        print('EXPRESSÃO VÁLIDA')
    else:
        print('EXPRESSÃO INVÁLIDA')