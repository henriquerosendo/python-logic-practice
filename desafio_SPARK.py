# 🚀 Desafio bônus (nível Spark)

# Dada a lista:

# dados = [
#     {"produto": "Camiseta", "preco": 50},
#     {"produto": "Calça", "preco": 120},
#     {"produto": "Tênis", "preco": 250}
# ]


# Crie uma transformação que:

# Aumente o preço de todos os produtos em 10% (map());

# Filtre apenas os produtos com preço final acima de 100 (filter());

# Calcule o total desses produtos (reduce()).

# Saída esperada:

# Produtos acima de 100: [{'produto': 'Calça', 'preco': 132.0}, {'produto': 'Tênis', 'preco': 275.0}]
# Total: 407.0


from functools import reduce
dados = [
    {"produto": "Camiseta", "preco": 50},
    {"produto": "Calça", "preco": 120},
    {"produto": "Tênis", "preco": 250}
]
# Aumentar o preço em 10%
dados_aumentados = list(
    map(lambda item: {"produto": item["produto"], "preco": item["preco"] * 1.1}, dados))    
# Filtrar produtos com preço acima de 100
produtos_filtrados = list(
    filter(lambda item: item["preco"] > 100, dados_aumentados))

# Calcular o total dos preços

total = reduce(lambda x, y: x + y["preco"], produtos_filtrados, 0)

print("Produtos acima de 100:", produtos_filtrados)

print("Total:", total)
