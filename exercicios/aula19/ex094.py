dados = dict()
pessoas = list()
totp = soma = 0
while True:
    nome = str(input('Nome: '))
    sexo = str(input('Sexo[M/F]: ')).strip().upper()[0]
    idade = int(input('Idade: '))
    dados['Nome'] = nome
    dados['Sexo'] = sexo
    dados['Idade'] = idade
    pessoas.append(dados.copy())
    totp +=1
    soma += idade
    opc = str(input('Quer continuar?[S/N]: ')).strip().upper()[0]
    if opc == 'N':
        break
print('-='*30)
print(f'A) O grupo tem {totp} pessoas')
print(f'B) A media de idade é de {soma/totp:.2f} anos')
print(f'C) As mulheres cadastradas foram: ', end='')
for i in pessoas:
    if i['Sexo']=='F':
            print(f"{i['Nome']}, ", end='')
print()
print(f'D) Lista das pessoas que estão acima da média:')
for i in pessoas:
    if i['Idade'] > (soma/totp):
        print(f'   Nome= {i["Nome"]} , Sexo = {i["Sexo"]}, Idade = {i["Idade"]}')

            
            
            
            
