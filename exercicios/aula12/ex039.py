from datetime import datetime
ano = int(input('Digite o seu ano de nascimento: '))
anoatual = datetime.today().year
idade = anoatual - ano
if idade <18:
    print(f'Voce tem {idade} anos e ainda falta {18-idade} anos para se alistar no execito')
elif idade == 18:
    print(f'Voce tem {idade} anos e deve se alistar no exercito')
else:
    print(f'Voce tem {idade} anos se alistou em {anoatual-(idade-18)} e ja passou {idade-18} anos do tempo de alistamento')