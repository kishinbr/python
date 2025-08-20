def voto(anon):
    from datetime import date

    anoatual = date.today().year
    idade = anoatual - anon

    if  16 <= idade <18 or idade >=65:
        voto = 'Voto opcional'
    elif 18 <= idade <65:
        voto = 'Voto Obrigatorio'
    else:
        voto = 'Não vota'
    return f'Com {idade} anos: {voto}'


ano = (int(input('Em que ano voce nasceu? ')))
print(voto(ano))
        

