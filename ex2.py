# Exercício 2

lista1 = []
lista2 = []
lista3 = []

# Lendo as duas listas
for i in range(10):
    lista1.append(int(input("Digite o {}º elemento da primeira lista: ".format(i + 1))))
    lista2.append(int(input("Digite o {}º elemento da segunda lista: ".format(i + 1))))

# Gerando a terceira lista intercalada
for i in range(10):
    lista3.append(lista1[i])
    lista3.append(lista2[i])

# Imprimindo a terceira lista
print("Lista intercalada: ", lista3)

