numeros = []
Executando = True

def menu():
    print("=" * 30)
    print(f"{'MENU PRINCIPAL':^30}")
    print("=" * 30)
    print("1 - MÉDIA")
    print("2 - MEDIANA")
    print("3 - SAIR")
    print("=" * 30)

def obter_nums():
    """Pede a quantidade de números e retorna a lista."""
    numeros.clear()
    while True:
        try:
            qtd_nums = int(input("Quantos números você deseja inserir? "))
            if qtd_nums <= 0:
                print("Por favor, insira um valor maior que zero.")
                continue
            for n in range(qtd_nums):
                valor = float(input(f"Digite o {n + 1}º número: "))
                numeros.append(valor)
        except ValueError:
            print("Entrada inválida. Digite apenas números.")

def calculo_media():
    """Calcula a média"""
    print("\n" + "-" * 30)
    print(f"{'CÁLCULO DA MÉDIA':^30}")
    print("-" * 30)

    obter_nums()
    media = sum(numeros) / len(numeros)

    print("\nNúmeros Escolhidos:", numeros)
    print(f"Média: {media:.2f}")
    print("-" * 30)

def calculo_mediana():
    """Calcula a mediana"""
    print("\n" + "-" * 30)
    print(f"{'CÁLCULO DA MEDIANA':^30}")
    print("-" * 30)

    obter_nums()
    num_sort = sorted(numeros)
    meio = len(num_sort) // 2

    if len(num_sort) % 2 == 0:
        mediana = (num_sort[meio - 1] + num_sort[meio]) / 2
    else:
        mediana = num_sort[meio]

    print("\nNúmeros ordenados:", num_sort)
    print(f"Mediana: {mediana:.2f}")
    print("-" * 30)

def sair():
    """Sai do programa"""
    print("Saindo...")
    return False

# Loop principal
while Executando:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        calculo_media()
    elif opcao == '2':
        calculo_mediana()
    elif opcao == '3':
        Executando = sair()
    else:
        print("\nOpção inválida! Tente novamente.\n")
