import requests


def verificar_site(url):
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            print(f"O site {url} está online!")
        else:
            print(f"O site {url} respondeu com o código {resposta.status_code}.")
    except requests.exceptions.RequestException:
        print(f"Não foi possível acessar o site {url}.")

# Exemplo de uso:
verificar_site("https://pudim.com")
