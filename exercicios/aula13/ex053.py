frase = input('Digite uma frase: ').strip()
num = len(frase)
sla = 0
print(len(frase))
print(frase[0])
for c in range(0,num):
    if frase[c] == frase[2]:
        sla = sla+1
if sla == num:
    print('A frase é palindromo')
else:
    print('A frase é normal')