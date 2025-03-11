valorCompras = float(input("Digite o valor da compra: "))

if valorCompras > 300:
	valorCompras = valorCompras * 0.9

print(f"Valor pagamento: %.2f" % (valorCompras))
