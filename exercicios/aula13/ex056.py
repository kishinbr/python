media = 0
midade= 0
qm = 0
nomeh = 'nao tem'
for c in range (1,5):
    print(f'----- {c} Pessoa -----')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [F/M]: ').strip().lower()
    media = media+idade
    if sexo == 'm' and idade > midade:
        midade = idade
        nomeh = nome
    if sexo == 'f' and idade<20:
        qm = qm+1



print(f'A media das idades é {media/4}')
print(f'O nome do HOMEM mais velho é {nomeh} e tem {midade}')
print(f'A quantidade de mulheres com menos de 20 é {qm}')