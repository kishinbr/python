from datetime import datetime
ano = int(input('Digite o seu ano de nascimento: '))
idade = datetime.today().year - ano
if idade <=9:
    print(f'Voce tem {idade} anos')
    print('Sua categoria é MIRIN')
elif idade <= 14:
    print(f'Voce tem {idade} anos')
    print('Sua categoria é INFANTIL')
elif idade <= 19:
    print(f'Voce tem {idade} anos')
    print('Sua categoria é JUNIOR')
elif idade <= 20:
    print(f'Voce tem {idade} anos')
    print('Sua categoria é SENIOR')
else:
    print(f'Voce tem {idade} anos')
    print('Sua categoria é MASTER')