print(">> CALCULO TRADICIONAL")
valor = float(input("Digite o Valor: "))
percentual = 20
total = valor * percentual / 100

print(f"Percentual Calculado: %.2f" % (total))

#100% equivale ao indice 1   (100/100)
#20% equivale ao indice  0.2 (20/100)

print(">> CALCULO SIMPLES")
print(f"Percentual Calculado: %.2f" % (valor * 0.2))


#Acrescentar 20% em um valor (1 + 0.2 = 1.2)
#descontar 20% de um valor (1 - 0.2 = 0.8)
print(f"Acrescentando 20%%: %.2f" % (valor * 1.2))
print(f"Descontando   20%%: %.2f" % (valor * 0.8))

