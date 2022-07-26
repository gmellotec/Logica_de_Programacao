## Trabalhando com Funções

def impostoSobreSalario(valor):
  if valor < 3000 * 12:
    return 0
  elif (valor >= 3000 * 12) and (valor < 5000 * 12):
    return valor * 0.1
  else:
    return valor * 0.2

def impostoSobreServico(valor):
  if valor > 0:
    return valor * 0.15
  else:
    return 0

def impostosobreGC(valor):
  if valor > 0:
    return valor * 0.2
  else:
    return 0

## Esta função realiza o calulo do total de imposto bruto
def impostoBrutoTotal(salario, servico, gc):
  return impostoSobreSalario(salario) + impostoSobreServico(servico) + impostosobreGC(gc)

## Esta função calcula os abatimentos com GMédicos e Educacionais
def abatimento(salario, servico, gc, gastosMedicos, gastosEducacionais):
  gastosDedutiveis = gastosMedicos + gastosEducacionais
  maximoDedutivel = impostoBrutoTotal(salario, servico, gc) * 0.3

  if (gastosDedutiveis > maximoDedutivel):
    return maximoDedutivel
  else:
    return gastosDedutiveis



print("Digite os dados do contribuinte:")
salario = float(input("Renda anual com salario: "))
servico = float(input("Renda anual com prestação de serviço: "))
gc = float(input("Renda anual com ganho de capital: "))
gastosMedicos = float(input("Gastos médicos: "))
gastosEducacionais = float(input("Gastos educacionais: "))

print()
print("RELATÓRIO:")
print(f"Imposto sobre salário: R$ {impostoSobreSalario(salario):.2f}")
print(f"Imposto sobre serviços: R$ {impostoSobreServico(servico):.2f}")
print(f"Imposto sobre ganho de capital: R$ {impostosobreGC(gc):.2f}")
print(f"Imposto bruto total: R$ {impostoBrutoTotal(salario, servico, gc):.2f}")
print(f"Abatimento: R$ {abatimento(salario, servico, gc, gastosMedicos, gastosEducacionais):.2f}")

impostoDevido = impostoBrutoTotal(salario, servico, gc) - abatimento(salario, servico, gc, gastosMedicos, gastosEducacionais)
print(f"Imposto devido: R$ {impostoDevido:.2f}")