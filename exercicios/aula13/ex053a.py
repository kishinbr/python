frase = input("Digite uma frase: ")  # Remove espaços e coloca em minúsculas
inverso = ""

# Inverte a frase manualmente
for letra in frase:
    inverso = letra + inverso

# Verifica se é um palíndromo
if frase == inverso:
    print("A frase é um palíndromo!")
else:
    print("A frase NÃO é um palíndromo!")