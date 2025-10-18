# 🔹 Exercício 5 — Mini ETL com listas

# Simule uma operação de ETL (extração, transformação e carga) com uma lista de dicionários.

# Dados de entrada:
# dados = [
#     {"nome": "Ana", "idade": 23},
#     {"nome": "Carlos", "idade": 35},
#     {"nome": "Beatriz", "idade": 29},
#     {"nome": "João", "idade": 41}
# ]

# Passos:

# Extração: use map() para extrair só os nomes.

# Transformação: use filter() para manter apenas pessoas com idade ≥ 30.

# Carga (simulada): exiba a lista final no console.

# Saídas esperadas:

from functools import reduce

dados = [
    {"nome": "Ana", "idade": 23},   
    {"nome": "Carlos", "idade": 35},
    {"nome": "Beatriz", "idade": 29},
    {"nome": "João", "idade": 41}
]
# Extração: extrair nomes
nomes = list(map(lambda pessoa: pessoa["nome"], dados))

# Transformação: filtrar pessoas com idade ≥ 30
pessoas_filtradas = list(filter(lambda pessoa: pessoa["idade"] >= 30,
                                 dados))
# Carga: exibir a lista final
print("Nomes extraídos:", nomes)
print("Pessoas com idade ≥ 30:", pessoas_filtradas)
# Saída:
# Nomes extraídos: ['Ana', 'Carlos', 'Beatriz', 'João']
# Pessoas com idade ≥ 30: [{'nome': 'Carlos', 'idade': 35
# , 'nome': 'João', 'idade': 41}]
#