from datetime import date
dados = {}
dados['Nome'] = str(input('Nome: '))
datan = int(input('Ano de nascimento: '))
datahj = date.today().year
dados['Idade'] = datahj-datan
cart = int(input('Carteira de trabalho (0 nao tem): '))
dados['CTPS'] = cart
if cart !=0:
    datac = int(input('Ano de Contrataçao: '))
    dados['Contraçao'] = datac
    dados['Salario'] = float(input('Salario: '))
    dados['Aposentadoria']= (datahj-datan) - (datahj - datac) + 35
print('-='*30)
print(dados)
for k , v in dados.items():
    print(f'{k} tem o valor {v}')
