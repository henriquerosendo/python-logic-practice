# 🔹 Exercício 4 — Usando reduce()

# Use reduce() para somar todos os valores de uma lista sem usar sum().

from functools import reduce


numeros = [3, 5, 7, 9]
soma = reduce(lambda x, y: x + y, numeros)
print(soma)  # Saída: 15
# 🔹 Fim do Exercício 4