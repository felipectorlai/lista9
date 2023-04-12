# Exercício 3

medias = []
alunos_aprovados = 0

# Lendo as notas dos alunos e calculando as médias
for i in range(10):
    notas = []
    for j in range(3):
        nota = float(input("Digite a {}ª nota do {}º aluno: ".format(j + 1, i + 1)))
        notas.append(nota)
    media = sum(notas) / len(notas)
    medias.append(media)

# Contando quantos alunos foram aprovados
for media in medias:
    if media >= 7.0:
        alunos_aprovados += 1

    # Imprimindo o resultado
print("Número de alunos com média maior ou igual a 7.0: ", alunos_aprovados)