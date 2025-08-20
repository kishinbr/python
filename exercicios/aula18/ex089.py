lista = []
dados=[]
while True:
    dados.append(str(input('Nome: '))) 
    dados.append(float(input('Nota 1: ')))
    dados.append(float(input('Nota 2: ')))
    lista.append(dados[:])
    dados.clear()
    opc = str(input('Quer continuar?[S/N]: ')).strip().upper()[0]
    if opc =='N':
        break
print('-='*20)
print(f'No.{"NOME":<10}{"MEDIA":>3}')
print('-'*30)
for i in range (0,len(lista)):
    print(f'{i}   {lista[i][0]:<10} {(lista[i][1]+lista[i][2])/2:3.1f}')
print('-'*30)
while True:
    choice= int(input('Mostrar notas de qual aluno?(999 interrompe)'))
    if choice == 999:
        break
    print(f'Notas da {lista[choice][0]} são : {lista[choice][1:3]}')
    print('-'*30)

