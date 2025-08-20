def ficha(n = '' , g = ''):
    if n == '':
        n = '<desconhecido>'
    if g == '':
        g = 0
    print(f'O jogador {n} fez {g}(s) no campeonato')
    
nome = str(input('Nome do Jogador: '))
ngol = str(input('Número de Gols: '))
ficha(nome,ngol)