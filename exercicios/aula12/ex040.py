nota1 = float(input('Digite o valor da primeira nota: '))
nota2 = float(input('Digite o valor da segunda nota: '))
media = (nota1 + nota2 )/ 2
if media < 5:
    print(f'Sua media foi de {media} e voce foi reprovado')
elif 5 <= media <7:
    print(f'Sua media foi de {media} e voce ficou de recuperacao')
else:
    print(f'Sua media foi de {media} e voce foi Aprovado')