nota = float(input("Digite uma nota: "))

if nota >= 0 and nota <= 10:
	print("Nota Valida! (AND)")
else:
	print("Nota Invalida! (AND)")


if nota == 1 or nota == 2 or nota == 3 or nota == 4 or nota == 5 or nota == 6 or nota == 7 or nota == 8 or nota == 9 or nota == 10:
	print("Nota Valida! (OR)")
else:
	print("Nota Invalida! (OR)")
