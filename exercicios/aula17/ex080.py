valores= []
for c in range(1,6):
    num = int(input(f'Digite um numero: '))
    if c ==1 or num >= valores[-1] :
        valores.append(num)
        print('Adicionado ao final da lista...')
    else:
        for i in range(0,len(valores)):
            if num <= valores[i]:
                valores.insert(i, num)
                print(f"Adicionado na posição {i} da lista...")
                break
print(valores)
    
            
