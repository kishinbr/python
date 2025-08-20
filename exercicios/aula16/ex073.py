times = ('Zero','Um','Dois','Tres','Quatro','Cinco','Seis','Sete','Chape','Nove','Dez')
print(f'{times[:4]}')
print(f'{times[-4:]}')
print(f'{sorted(times)}')
for i, time in enumerate(times):
    if time == 'Chape':
        print(f'{time} esta na {i} posicao')
print(f'Chape esta na {times.index("Chape")} posicao')
