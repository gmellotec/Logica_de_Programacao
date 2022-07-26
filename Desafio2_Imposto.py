## DESAFIO DEV SUPERIOR 2 - IMPOSTO

rendaAnSalario = float(input("Renda anual com salário: "))
rendaAnServico = float(input("Renda anual com prestação de serviço: "))
rendaAnGanhoCap = float(input("Renda anual com ganho de capital: "))
gastosMedicos = float(input("Gastos Médicos: "))
gastosEducacao = float(input("Gastos Educacionais: "))

#Imposto sobre Salário / Serviço / Capital / Total Bruto

if rendaAnSalario < 3000 * 12:
    impostoSalario = 0
elif (rendaAnSalario >= 3000 * 12) and (rendaAnSalario < 5000 * 12):
    impostoSalario = rendaAnSalario * 0.1
else:
    impostoSalario = rendaAnSalario * 0.2

impostoPServico = rendaAnServico * 0.15
impostoGCapital = rendaAnGanhoCap * 0.2

impostoBTotal = impostoGCapital + impostoSalario + impostoPServico


#Calculo Deduções

maxDedutivel = impostoBTotal * 0.3
gastosDedutiveis = (gastosEducacao + gastosMedicos)


if gastosDedutiveis < maxDedutivel:
    abatimento = gastosDedutiveis
else:
    abatimento = maxDedutivel

totalfinal = impostoBTotal - abatimento

print()
print("=============================")
print("RELATÓRIO DE IMPOSTO DE RENDA")
print()
print("CONSOLIDADO DE RENDA")
print(f"Imposto sobre salário: R$ {impostoSalario:.2f}")
print(f"Imposto sobre serviço: R$ {impostoPServico:.2f}")
print(f"Imposto sobre ganho de capital: R$ {impostoGCapital:.2f}")
print()
print("DEDUÇÕES:")
print(f"Máximo dedutível: R$ {maxDedutivel:.2f}")
print(f"Gastos dedutíveis: R$ {gastosDedutiveis:.2f}")
print()
print("RESUMO")
print(f"Imposto bruto total: R$ {impostoBTotal:.2f}")
print(f"Abatimento: R$ {abatimento:.2f}")
print(f"Imposto devido: R$ {totalfinal:.2f}")