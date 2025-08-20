valor = float(input('Digite o valor do imovel: '))
sal = float(input('Digite o salario do finaciador: '))
anos = int(input('Quantos anos vai ser quitado: '))
parcela = valor / (anos*12)
print(f'O valor da prestação mensal vai ser R${parcela:.2f} durante {anos:} anos.')
if parcela > sal*0.3: 
    print('Infelizmente não sera possivel realizar o imprestimo.')
else:
    print('Imprestimo concedido.')