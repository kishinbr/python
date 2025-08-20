galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo[M/F]: ')).upper()
        if pessoa['sexo'] in "MF":
            break
        print('Erro! Por favor user M ou F')
    pessoa['idade'] = str(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar?[S/N]: ')).strip().upper()[0]
        if resp in "SN":
            break
        print('Erro! Por favor user S ou N')
    if resp == 'N' :
        break
print('-='*30)
print(f'A) O grupo tem {len(galera)} pessoas')
media = soma / len(galera)
print(f'B) A media de idade é de {media:5.2f} anos')
print(f'C) As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['sexo']=='F':
        print(f'{p["nome"]} ', end='')
print()
print(f'D) Lista das pessoas que estão acima da média:')
for p in galera:
    if p['idade'] >= media:
        print('     ', end="")
        for k , v in p.items():
            print(f'{k} = {v} ', end='')
        print()
print('Encerrado')

