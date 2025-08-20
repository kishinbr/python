print('-'*30)
print('      LOJA SUPER BARATÃO')
print('-'*30)
total = c = p1k = menorp = 0
mbarato = ''
while True:
    c +=1
    nomep = str(input('Nome do produto: ')).strip()
    preco = float(input('Preco: R$'))
    total += preco
    if preco > 1000:
        p1k += 1
    if c == 1 or preco < mpreco:
        mpreco = preco
        mbarato = nomep
    opc = str(input('Quer continuar?[S/N]')).upper().strip()[0]
    while opc not in 'SsNn':
        opc = str(input('Quer continuar?[S/N]')).upper().strip()[0]
    if opc in 'Nn':
        print('{:-^40}'.format('Fim do Programa'))
        print(f'{"Fim do Programa":-^40}')
        break
print(f'O total da compra foi de R${total}')
print(f'Temos {p1k} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi \'{mbarato}\' que custa R${mpreco}')

