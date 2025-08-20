palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 
            'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

for palavra in palavras:
    vogais = ""  # Variável para armazenar as vogais
    for letra in palavra:  # Percorre cada letra da palavra
        if letra in "aeiou":  # Verifica se é uma vogal
            vogais += letra + " "  # Adiciona a vogal e um espaço
    print(f"Na palavra {palavra.upper()} temos {vogais}")