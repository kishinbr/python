c = ('\033[m', #0 sem nada
     '\033[0;30;41m', #1 vermelho
     '\033[0;30;42m', #2 verde
     );
    
def ajuda(com):
    help(com)


def titulo(msg,cor=0):
    tam = len(msg) +4
    print(c[cor], end='')
    print('-'*tam)
    print(f"  {msg}")
    print('-'*tam)
    print(c[0], end='')

comando = ''
while True:
    titulo('SISTEMA DE AJUDA PYHELP',2)
    comando = str(input('Funçao ou Biblioteca> '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATE LOGO!',1)