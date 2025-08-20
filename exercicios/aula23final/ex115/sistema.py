from time import sleep
from lib import interface , arquivo
arq = 'bancodedados.txt'
if not arquivo.arquivoExiste(arq):
    arquivo.criarArquivo(arq)
while True:
    respostas = interface.menu(['Ver Pessoas cadastradas','Cadastrar nova Pessoa','Sair do Sistema'])
    if respostas == 1: #opcao de lista o conteudo do arquivo
        arquivo.lerArquivo(arq)
    elif respostas ==2:
        interface.cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = interface.leiaInt('Idade: ')
        arquivo.cadastrar(arq , nome, idade)
    elif respostas ==3:
        print('Saindo do Sistema...')
        break
    else:
        print('ERRO!Digite um opção valida!')
    sleep(1)
