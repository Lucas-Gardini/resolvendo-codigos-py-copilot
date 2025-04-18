# Vamso verificar se um número é par ou ímpar

# Vamos solicitar um número ao usuário e verificar se ele é par ou ímpar.
entrada = input("Digite um número: ")

# Convertendo a entrada para inteiro
numero = int(entrada)

# Verificando se o número é par ou ímpar
if numero % 2 == 0:
    resultado = "par"
else:
    resultado = "ímpar"

print("O número", numero, "é", resultado)
