lar=float(input('Largura da parede:'))
alt=float(input('Altura da parede:'))
area = lar * alt
print(f'Sua parede tem a dimensão de {lar}x{alt} e sua área é de {area}m2.')
print(f'Para pintar essa parede, voce precisara de {area/2:.2f} litros de tinta')