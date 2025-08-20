n = int(input("Quantos termos da sequência de Fibonacci deseja ver? "))
a, b = 1, 1  # Primeiros dois termos
contador = 0
while contador < n:
    print(a, end=" ")  # Mostra o termo atual
    a, b = b, a + b  # Atualiza os valores
    contador += 1  # Incrementa o contador
