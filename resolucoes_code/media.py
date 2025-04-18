# Vamos calcular a média de 4 números inteiros fornecidos pelo usuário.

# Vamos solicitar ao usuário quatro números inteiros e calcular a média deles.
entrada = input("Digite quatro números inteiros separados por espaço: ")

# Vamos separar os números
numeros = entrada.split()

# Convertendo os números para inteiros
numeros = [int(num) for num in numeros]

# Calculando a média
media = sum(numeros) / len(numeros)
print("A média dos números é:", media)
