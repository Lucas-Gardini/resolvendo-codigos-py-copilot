# Vamos verificar se uma palavra é um palíndromo

# Vamos solicitar uma palavra ao usuário e verificar se ela é um palíndromo.
entrada = input("Digite uma palavra: ")

# Convertendo a entrada para minúsculas e removendo espaços
entrada = entrada.lower().replace(" ", "")

# Verificando se a palavra é um palíndromo
if entrada == entrada[::-1]:
    resultado = "é um palíndromo"
else:
    resultado = "não é um palíndromo"

print("A palavra", entrada, resultado)
