def leiaInt():
    while True:
        try:
            n = int(input('Digite um inteiro: '))
        except ValueError:
            print('ERRO!Digite um numero inteiro!')
            continue
        except KeyboardInterrupt:
            print('\nUsuario infelizmente interrompeu o programa')
            return 0
        else:
            return n
    
        

def leiaFloat():
    while True:
        try:
            n = float(input('Digite um REAL: '))
            return n
        except ValueError:
            print('ERRO!Digite um numero REAL!')
        except KeyboardInterrupt:
            print('\nUsuario infelizmente interrompeu o programa')
            n = 0
            break
    return n

