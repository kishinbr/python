galera = [['Joao', 19],['Ana', 33],['Joaquin', 13],['Maria',45]]
print(galera)
print(galera[0])
print(galera[0][0])
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')
galera = list()
dado = list()
for c in range (0,3):
    dado.append(str(input('Digite seu nome: ')))
    dado.append(int(input('Digite sua idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)
totmai =totmen =0
for p in galera:
    if p[1]>=21:
        print(f'{p[0]} é maior de idade')
        totmai +=1
    else:
        print(f'{p[0]} é menor de idade')
        totmen +=1
print(f'Temos {totmai} maiores e {totmen} menores de idade')