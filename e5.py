# 🔹 Exercício 5 — Dicionário de notas

# Peça o nome e a nota de 3 alunos, salve em um dicionário e mostre:

# Aluno: João | Nota: 8.5
# Aluno: Maria | Nota: 9.0
# Aluno: Ana | Nota: 7.5


notas = {}
for _ in range(3):
    nome = input("Digite o nome do aluno: ")
    nota = float(input(f"Digite a nota de {nome}: "))
    notas[nome] = nota
for aluno, nota in notas.items():
    print(f"Aluno: {aluno} | Nota: {nota}")     
# Fim do código