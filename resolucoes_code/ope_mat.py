# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

entradas = input("Digite dois números separados por espaço: ")

# Vamos separar os números
numeros = entradas.split()

# Convertendo os números para float
num1 = float(numeros[0])
num2 = float(numeros[1])

# Realizando a operação de soma
resultado = num1 + num2

print("O resultado da soma é:", resultado)
