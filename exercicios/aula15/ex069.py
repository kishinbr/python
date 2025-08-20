qp18 = qh = qm20 = 0
while True:
    print('-'*30)
    print('     CADASTRE UMA PESSOA')
    print('-'*30)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo[M/F]: ')).upper().strip()[0]
    while sexo not in 'FfMm':
        sexo = str(input('Sexo[M/F]: ')).upper().strip()[0]
    if idade > 18:
        qp18 +=1
    if sexo in 'Mm':
        qh += 1
    if sexo in 'Ff' and idade < 20:
        qm20 += 1
    print('-'*30)
    opc = str(input('Quer continuar?[S/N]: ')).upper().strip()[0]
    while opc not in 'SsNn':
        opc = str(input('Quer continuar?[S/N]: ')).upper().strip()[0]
    if opc in 'Nn':
        print(f'======FIM DO PROGRAMA======')
        break
print(f'Total de pessoas com mais de 18 anos: {qp18}')
print(f'Ao todo temos {qh} homens cadastrados')
print(f'E temos {qm20} mulheres com menos de 20 anos')