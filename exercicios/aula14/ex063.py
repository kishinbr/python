n = int(input("Quantos termos da sequência de Fibonacci deseja ver? "))
n1 = 1
n2 = 1
c = 0 
while c < n:
    print(f'{n1}', end=' ')
    temp = n1
    n1 = n2
    n2 = temp + n2
    c = c+1

