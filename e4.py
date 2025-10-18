# 🔹 Exercício 4 — Maior e menor número

# Dada uma lista, mostre o maior e o menor número sem usar max() nem min().
numeros = [34, 12, 5, 67, 23, 89, 1, 45, 78, 3]
maior = numeros[0]
menor = numeros[0]
for numero in numeros:
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero 
print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")     
