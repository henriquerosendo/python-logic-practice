# 🔹 Exercício 2 — Usando map()

def quadrado(x):
    return x * x

numeros = [1, 2, 3, 4, 5]
resultado = list(map(quadrado, numeros))
print(resultado)