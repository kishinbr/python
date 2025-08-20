frase = 'Curso em Video Python'
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[:])
print(frase[1:15:2])
print(frase[::2])

print('='*40)
print(frase.count('o'))
print(frase.upper().count('O'))
print(len(frase))
print(len(frase.strip()))
print(frase.replace('Python','teste'))
#frase = frase.replace('Python','teste')
#print(frase)
print('Curso' in frase)
print(frase.find('Curso'))
print(frase.find('video'))
print(frase.lower().find('video'))
print(frase.split())
dividido = frase.split()
print(dividido[0][1])
print(dividido[0],dividido[3])

"""
frase = 'Curso em Video Python' = 21 //character , comeca do 0 e conta espacos

frase[9] = V
frase[9:13] = Vide //(o 9 entra e o 13 nao)
frase[9:21:2] = VdoPto
frase[:5] = Curso
frase[15:] = Python
frase[9::3] = VePh

len(frase) = 21
frase.count('o') = 3
frase.count('o',0,13) = 1 //(contagem com fatiamento do 0 ate o 13)

frase.find('deo') = 11
frase.find('Android') = -1 //(nao foi encontrado)

'curso' in frase = true 

frase.replace('Python' , 'Android')
frase.upper() 
frase.lower()
frase.capitalize() // tudo minusculo só a primeira maiscula
frase.title()      // todas 1 letras maiscula

frase.strip() //remove espacos vazio 
frase.rstrip() // so remove espado da direita
frase.lstrip() // da esquerda

frase.split() // divide no ESPACO , gera uma lista 
'-'.join(frase)
 """