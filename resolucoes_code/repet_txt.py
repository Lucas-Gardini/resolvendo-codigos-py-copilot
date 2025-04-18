# Repetindo um texto baseado em uma entrada do usuário

# Vamos solicitar ao usuário um texto e um número, e repetir o texto o número de vezes especificado.
entrada = input("Digite um texto: ")
repeticoes = int(input("Quantas vezes você quer repetir o texto? "))

# Repetindo o texto
resultado = entrada * repeticoes
print("O resultado da repetição é:", resultado)
