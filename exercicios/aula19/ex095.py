jogadores= []
jogador = {}
gols = []
while True:
    jogador['Nome']= str(input('Nome do Jogador: '))
    part = int(input(f'Quantas partidas {jogador["Nome"]} jogou?: '))
    print('-='*30)
    tot = 0
    for i in range(0,part):
        ng = (int(input(f'Quantos gols na partida {i+1}?: ')))
        tot += ng
        gols.append(ng)
    jogador['Gols'] = gols[:]
    jogador['Total'] = tot
    gols.clear()
    opc = str(input('Quer continuar?[S/N]:')).strip().upper()
    jogadores.append(jogador.copy())
    jogador.clear()
    if opc =='N':
        break
print('-='*30)
print(f'{"Cod"} {"Nome":<12}{"Gols":<15}{"Total":<5}')
c = 0
for i in jogadores:
    ##["Gols"]!s:<15s
    print(f'{c:<3} {i["Nome"]:<12}{i["Gols"]!s:<15s}{i["Total"]:<5}')
    c +=1
print('-='*30)
while True:
    opcj = int(input('Mostrar dados de qual jogador?999: '))
    if opcj == 999:
        break
    print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[opcj]["Nome"]}')
    cj = 1
    for i in jogadores[opcj]['Gols']:
        print(f'No jogo {cj} fez {i} gols')
        cj+=1
print('Fim')
