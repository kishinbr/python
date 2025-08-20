def notas(*notas , sit = True ):
    boletim = dict()
    media = 0
    for i,v in enumerate(notas):
        if i == 0 or v > maior:
            maior = v
        if i == 0 or v < menor:
            menor = v
        media +=v
    media = media/len(notas)
    
    boletim['total'] = len(notas)
    boletim['maior'] = maior
    boletim['menor'] = menor
    boletim['media'] = media

    

    return boletim

        
resp = notas(5,2,10,10,10,5,1,1,1,10, sit=False)
print(resp)