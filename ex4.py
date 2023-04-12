# Exercício 4

notas = []
nota = 0
soma = 0
media = 0
quantidade = 0
acima_da_media = 0
abaixo_de_sete = 0

# Lendo as notas e calculando a soma
while nota != -1:
    nota = float(input("Digite uma nota (-1 para sair): "))
    if nota != -1:
        notas.append(nota)
        soma += nota
        quantidade += 1

    # Calculando a média
if quantidade > 0:
    media = soma / quantidade

# Calculando a quantidade de valores acima da média e abaixo de sete
for n in notas:
    if n > media:
        acima_da_media += 1
    if n < 7:
        abaixo_de_sete += 1

    # Imprimindo os resultados
print("Quantidade de valores lidos: ", quantidade)
print("Soma dos valores: ", soma)
print("Média dos valores: ", media)
print("Quantidade de valores acima da média: ", acima_da_media)
print("Quantidade de valores abaixo de sete: ", abaixo_de_sete)