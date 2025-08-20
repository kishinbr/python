cidade = input('Digite o nome da sua cidade:').strip()
div = cidade.lower().split()
#print(f"Sua cidade {div[0].lower().find('santo')} comeca com SANTO")
print(f"Sua cidade {'santo' in div[0]}, comeca com Santo")