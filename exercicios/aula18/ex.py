teste = list()
teste.append('Gustavo')
teste.append(40)
print(teste)

galera = list()
galera.append(teste[:])

teste[0]= 'maria'
teste[1]= 22

galera.append(teste[:])

print(teste)
print(galera)