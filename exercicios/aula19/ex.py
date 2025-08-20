pessoas = {'nome': 'Gustavo', 'sexo': 'm', 'idade': 22}
print(pessoas)
print(pessoas['idade'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')

print(pessoas.keys()) #chaves, nome dos valores
print(pessoas.values())#mostra os valores dentro do dicionario
print(pessoas.items())#mostra uma lista da key e values

for k in pessoas.keys():
    print(k)
for k in pessoas.values():
    print(k)
for k, v in pessoas.items():
    print(f'{k} = {v}')

pessoas['nome'] = 'leandro'
pessoas['peso'] = 98.5
del pessoas['sexo']
for k, v in pessoas.items():
    print(f'{k} = {v}')

print('-'*50)
brasil = list()
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'Sao Paulo', 'sigla': 'SP'}

brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[1])
print(brasil[0]['uf'])
print(brasil[1]['sigla'])

print('-'*50)
estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
print(brasil)
for e in brasil:
    print(e)
for e in brasil:
    for k , v in e.items():
        print(f'O campo {k} tem valor {v}')