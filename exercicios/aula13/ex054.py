from datetime import datetime
data = datetime.today().year
ma= 0
nma = 0
for c in range(1,8):
    ano = int(input(f'Em que ano a {c} pessoa nasceu?: '))
    if data-ano <21:
        nma = nma+1
    else:
        ma = ma +1
print(f'A quantidade que atingiu a maioridade foram {ma} e que nao atingiram foi {nma}')
