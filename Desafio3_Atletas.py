qAtletas = int(input("Qual a quantidade de atletas? "))

somaPeso = 0
qHomens = 0
qMulheres = 0
somaAltura = 0
alturaMaior = 0
mulheres = 0

for i in range(1, qAtletas + 1):
  print(f"Digite os dados do atleta numero {i}:")
  nome = input("Nome: ")
  
  sexo = input("Sexo: ")
  while (sexo != "F") and (sexo != "M"):
    sexo = input("Valor invalido! Favor digitar F ou M: ")
  
  altura = float(input("Altura: "))
  while (altura <= 0):
    altura = float(input("Valor invalido! Favor digitar um valor positivo: "))

  peso = float(input("Peso: "))
  while (peso <= 0):
    peso = float(input("Valor invalido! Favor digitar um valor positivo: "))

  somaPeso += peso
  pesomedio = somaPeso / qAtletas

  if (altura > alturaMaior):
    alturaMaior = altura
    atletaAlto = nome
    
    mulheres += 1

  if sexo == 'M':
    qHomens += 1
    aMedia = 0
  elif sexo == 'F':
    qMulheres += 1
    somaAltura += altura
    aMedia = somaAltura / qMulheres

  percentH = (qHomens / qAtletas) * 100




print("RELATÓRIO:")
print()
print(f"Peso médio dos atletas: {pesomedio:.2f}")
print(f"Atleta mais alto: {atletaAlto}")
print(f"Porcentagem de homens: {percentH:.1f}%")

if qMulheres > 0:
  print(f"Altura média das mulheres: {aMedia:.2f}")
else:
  print("Não há mulheres cadastradas.")
  
  
