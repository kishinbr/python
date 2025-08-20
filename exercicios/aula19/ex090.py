dados = {}
dados['Nome'] = str(input('Nome: '))
dados['Media'] = float(input(f'Media de {dados["Nome"]}: '))
if dados['Media'] >= 7:
    dados['Situacao'] = 'Aprovado'
elif dados['Media'] >= 5:
    dados['Situacao'] = 'Recuperacao'
else:
    dados['Situacao'] = 'Reprovado'
for e,v in dados.items():
    print(f'{e} é igual a {v}')