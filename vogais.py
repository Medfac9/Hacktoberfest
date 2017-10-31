# hacktoberfest 2017

vogais = "aeiou"
cont = 0

palavra = input("Digite uma palavra: ").lower()

for i in palavra:
    if i in vogais:
        cont += 1

print("Quantidade de vogais na palavra: " + str(cont))
