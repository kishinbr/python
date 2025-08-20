def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',','.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'ERRO!! {entrada} é um preco invalido!')
        else:
            valido = True
            return float(entrada)
       
       
def leiaInt():
    while True:
        l = 0
        num = input('Digite um numero:')
        for c in num:
            if c in '0123456789':
                l = l+1
            else:
                print('ERRO!Digite um numero inteiro')
                break
        if l == len(num) :
            break
    return num