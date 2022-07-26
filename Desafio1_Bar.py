## DESAFIO DEV SUPERIOR 1 - BAR


sexo = input("Selecione o Sexo (M/F): ")
Qcerv = int(input("Quantidade de Cervejas: "))
Qrefri = int(input("Quantidade de Refrigerantes: "))
Qespet = int(input("Quantidade de espetinhos: "))

#Preço dos Produtos
Pcerv = 5.00
Prefri = 3.00
Pespet = 7.00

if sexo == "M":
    ingresso = 10.00
else:
    ingresso = 8.00

totalConsumo = ((Qcerv * Pcerv) + (Qrefri * Prefri) + (Qespet * Pespet))

if totalConsumo > 30:
    totalPagar = totalConsumo + ingresso
    print()
    print("==============")
    print("TOTAL DA CONTA:")
    print(f"Consumo = R$ {totalConsumo:.2f}")
    print("Isento de Couvert")
    print(f"Ingresso = R$ {ingresso:.2f}")
    print()
else:
    couvert = 4.00
    totalPagar = totalConsumo + couvert + ingresso
    print()
    print("==============")
    print("TOTAL DA CONTA:")
    print(f"Consumo = R$ {totalConsumo:.2f}")
    print(f"Couvert = R$ {couvert:.2f}")
    print(f"Ingresso = R$ {ingresso:.2f}")
    print()

print(f"Valor a pagar = R$ {totalPagar:.2f}")