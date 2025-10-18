# Digite uma palavra: programação
# A palavra 'programação' tem 5 vogais.

palavra = input("Digite uma palavra: ")
vogais = "aãâáeiouAEIOU"
contador = 0
for letra in palavra:
    if letra in vogais:
        contador += 1
print(f"A palavra '{palavra}' tem {contador} vogais.")

# Fim do código