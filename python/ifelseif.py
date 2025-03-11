nota = int(input("Digite uma nota: "))

if nota > 10:
	print("Nota Invalida! (Precisa ser ate 10)")
elif nota < 0:
	print("Nota Invalida! (Precisa ser maior que 0)")
else:
	print("Nota Valida!")
