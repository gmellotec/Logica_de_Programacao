n = int(input("Qual a quantidade de pessoas? "))

candidatos = []
notas1 = []
notas2 = []
medias = []
mediaAprovados = []

## Entrada dos dados e inserindo cada dado em sua lista especifica
for i in range(0, n):
  print(f"Digite os dados da {i+1}a pessoa:")
  nome = input("Nome: ")
  candidatos.append(nome)
  nota1 = float(input("Nota etapa 1: "))
  notas1.append(nota1)
  nota2 = float(input("Nota etapa 2: "))
  notas2.append(nota2)

## Média das notas de cada aluno
for i in range(0, n):
  mediaNotas = (notas1[i] + notas2[i]) / 2
  medias.append(mediaNotas)

## Exibir todas as informações de cada candidato: 
## Nome, Nota1, Nota2 e Média
print()
print("TABELA:")
for i in range(0, n):
  print(f"{candidatos[i]}, {notas1[i]}, {notas2[i]}, MEDIA = {medias[i]:.2f}")

## Exibir nome dos candidatos aprovados e o nome do candidato com maior média e percentual aprovados
## e fazer o calculo de média das notas dos aprovados
print()
print("PESSOAS APROVADAS:")
contAprovados = 0
maiorMedia = 0
somaMediaAprovados = 0

## Para separar as médias acima de 70 pontos (APROVADOS) e o % de aprovados
for i in range(0, n):
  if medias[i] >= 70:
    print(candidatos[i])
    mediaAprovados.append(medias[i])
    contAprovados += 1
    somaMediaAprovados += medias[i]

percentAprovados = (contAprovados / n) * 100

## Para exibir o nome do candidato com maior nota
for i in range(0, n): 
  if medias[i] > maiorMedia:
    maiorMedia = medias[i]
    maiorMediaNome = candidatos[i]

print()
print(f"Porcentagem de aprovação: {percentAprovados} %")
print(f"Maior média: {maiorMediaNome}")

## Exibir a nota média dos candidatos aprovados SE houver
if contAprovados == 0:
  print("Não há candidatos aprovados")
else:
  notaMediaAprovados = somaMediaAprovados / contAprovados
  print(f"Nota média dos aprovados: {notaMediaAprovados:.2f}")