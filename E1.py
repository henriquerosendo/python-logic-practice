# 🔹 Exercício 1 — Par ou Ímpar

# Crie um programa que peça um número e diga se ele é par ou ímpar.
while True:
    try:
        numero = int(input("Digite um número: "))
        
        if numero % 2 == 0:
            print("O número é par")
        else:
            print("O número é ímpar")   
        
        sair = input("Deseja sair? (S/N): ")
        
        if sair.lower() == "s":
            print("Programa encerrado!")
            break
            
    except ValueError:
        print("Por favor, digite um número válido!")