num = int(input('Digite um numero para base de conversão:'))

print('Escolha qual será a base de conversão :')
print('\033[2;33m-\033[2;34m1 \033[0mpara \033[2;33mbinario \n\033[2;33m-\033[2;34m2 \033[0mpara \033[2;33moctal\n\033[2;33m-\033[2;34m3 \033[0mpara \033[2;33mhexadecimal\033[0m')

choice = int(input('Digite sua escolha: '))
if choice == 1:
    print(f'Sua escolha foi binario')
    print(f'{bin(num)[2:]}')

elif choice ==2:
    print('Sua escolha foi octal')
    print(f'{oct(num)[2:]}')

elif choice ==3:
    print('Sua escolha foi Hexadecimal')
    print(f'{hex(num)[2:].upper()}')

else:
    print('Digite a opcao certa')