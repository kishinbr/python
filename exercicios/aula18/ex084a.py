temp= []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(str(input('Peso: ')))
    if len(princ)==0:
        mai = men = temp[1]
    else:
        if temp[1]>mai:
            mai = temp[1]
        if temp[1]<men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar?[S/N]: '))
    if resp in 'Nn':
        break
print('-='*30)
print(f'Ao todo, foram cadastrados {len(princ)}')
print(f'O maior peso foi de {mai}kg, foi de ', end='')
for p in princ:
    if p[1]==mai:
        print(f'{p[0]}...',end='')
print(f'O menor peso foi de {men}kg, foi de ', end='')
for p in princ:
    if p[1]==men:
        print(f'{p[0]}...',end='')
        




