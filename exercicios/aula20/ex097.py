def escreva(txt):
    tam = len(txt) +4
    print(f'-'*tam)
    print(f'{txt.center(tam)}')
    print(f'-'*tam)

escreva('Olá, Mundo!')
escreva('nao sei oq estou fazendo')
escreva('abc')