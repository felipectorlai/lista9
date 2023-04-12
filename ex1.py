# Exercício 1

numeros = []
pares = []
impares = []

for i in range(10):
    numero = int(input("Digite um número inteiro: "))
    numeros.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("Números digitados: ", numeros)
print("Números pares: ", pares)
print("Números ímpares: ", impares)