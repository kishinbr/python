frase = input('Digite uma frase: ').strip()
print(f"A letra A aparece na frase : {frase.lower().count('a')} ")
print(f"A letra a aparece na primeira vez na posicao : {frase.lower().find('a')}")
print(f"A letra a aparece na ultima vez na posicao : {frase.lower().rfind('a')}")