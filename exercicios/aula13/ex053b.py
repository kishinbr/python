frase = input('Digite uma frase: ').strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
#inverso = junto[::-1]
for c in range(len(junto)-1, -1 ,-1):
    inverso += junto[c]
if junto == inverso:
    print(f'A frase {frase} é um palindro')
else:
    print(f'A frase {frase} nao é um palindro')
  