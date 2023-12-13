import matplotlib.pyplot as plt

num_alunos = int(input("Digite o número de alunos:"))
alunos = []
generos = []

for i in range(num_alunos):
    nome = input(f"Digite o nome do aluno: ") 
    genero = input(f"Digite o gênero do aluno (M/F): ").upper()
    notas = []

    for n in range(4):
        nota = float(input(f"Digite a nota {n + 1} de {nome}: "))
        notas.append(nota)

    alunos.append({"nome" : nome, "notas": notas, "genero": genero})
    generos.append(genero)

# Calcular a média
medias = []
media_genero = {"M": [], "F": []}

for aluno in alunos:
    nome = aluno["nome"]
    notas = aluno["notas"]
    genero = aluno["genero"]
    media = sum(notas) / len(notas)
    medias.append(media)
    media_genero[genero].append(media)

    # print(f"Número de Alunos: {i}")
    # print(f"Nome: {nome}")
    # print(f"Gênero: {genero}")

# Exibir gráfico de média das notas
plt.figure(figsize=(8, 4))
plt.bar(range(num_alunos), medias, tick_label=[aluno["nome"] for aluno in alunos])
plt.xlabel("Alunos")
plt.ylabel("Média das Notas")
plt.title("Média das Notas dos Alunos")
plt.savefig("media_notas_alunos.png")  # Salva o gráfico como uma imagem PNG
plt.show()

# Exibir gráfico de média por gênero
generos = list(media_genero.keys())
medias_por_genero = [sum(media_genero[genero]) / len(media_genero[genero]) for genero in generos]

plt.figure(figsize=(4, 4))
plt.bar(generos, medias_por_genero)
plt.xlabel("Gênero")
plt.ylabel("Média das Notas")
plt.title("Média das Notas por Gênero")
plt.savefig("media_notas_genero.png")  # Salva o gráfico como uma imagem PNG
plt.show()

#  git rm --cached -r .
