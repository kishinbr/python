from math import cos  , tan , radians , sin
ang = float(input('Digite o angulo :'))
print(f'Seno {sin(radians(ang)):.2f}')
print(f'Cosseno {cos(radians(ang)):.2f}')
print(f'Tangente {tan(radians(ang)):.2f}')