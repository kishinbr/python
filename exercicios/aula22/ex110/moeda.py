def metade(preco = 0, format = False) :
    res = preco/2
    return res if not format else moeda(res)


def dobro(preco = 0, formato = False) :
    res = preco*2
    return res if not formato else moeda(res)


def aumentar(preco = 0, taxa = 0 , formato = False):
    res = preco + (preco*taxa)/100 
    return res if formato is False else moeda(res)


def diminuir(preco = 0, taxa = 0 , formato = False):
    res = preco - (preco*taxa)/100 
    return  res if formato is False else moeda(res)


def moeda (preco, moeda ='R$' ):
    return f'{moeda}{preco:.2f}'.replace('.',',')

def resumo(preco, aumen, redu):
    print('-'*30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-'*30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preco: \t{dobro(preco,True)}')
    print(f'Metade do preco: \t{metade(preco,True)}')
    print(f'{aumen}% de aumento: \t{aumentar(preco,aumen,True)}')
    print(f'{redu}% de aumento: \t{diminuir(preco,redu,True)}')
    print('-'*30)