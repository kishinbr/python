def maior(*num):
    print(f'-='*30)
    print('Analisando os valores passados..')
    maior = 0
    for c in num:
        if c==0 or c > maior:
            maior = c
        print(f'{c} ', end='')
    print(f'Foram informados {len(num)} valores ao todo')
    print(f'O maior valor informado foi {maior}')


maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()