jogador = {}
gols = []
jogador['Nome']= str(input('Nome do Jogador: '))
part = int(input(f'Quantas partidas {jogador["Nome"]} jogou?: '))
print('-='*30)
tot = 0
for i in range(0,part):
    ng = (int(input(f'Quantos gols na partida {i+1}?: ')))
    tot += ng
    gols.append(ng)
jogador['Gols'] = gols
jogador['Total'] = tot
print('-='*30)
print(f'{jogador}')
print('-='*30)
for k , v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["Nome"]} jogou {len(jogador["Gols"])} partidas')
for c,k in enumerate(jogador['Gols']):
    print(f'   => Na partida {c}, fez {k} gols')
print(f'Foi um total de {jogador["Total"]} gols')


