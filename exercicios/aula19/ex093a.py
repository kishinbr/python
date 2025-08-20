jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou?: '))
print('-='*30)
for i in range(0,tot):
    partidas.append(int(input(f'  Quantos gols na partida {i+1}?: ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-='*30)
print(jogador)
print('-='*30)
for k , v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for c,k in enumerate(jogador['Gols']):
    print(f'   => Na partida {c}, fez {k} gols')
print(f'Foi um total de {jogador["Total"]} gols')
    