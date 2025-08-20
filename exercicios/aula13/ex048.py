s = 0
cont =0 
for c in range(1,501,2):
    if c%3 == 0:
        s = s+c
        cont = cont+1
print(f'Somatoria total é {s} e foram somados {cont} numeros')