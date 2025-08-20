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


n = leiaInt()
print(f'Voce acabou de digitar o numero {n}')