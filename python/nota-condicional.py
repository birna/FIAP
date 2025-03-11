nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 6:
	status = "APROVADO"
else:
	status = "REPROVADO"




print("\n>>     LOG")
print(f"Nota1: %.2f" % (nota1))
print(f"Nota2: %.2f" % (nota2))
print(f"Nota3: %.2f\n_____________________________" % (nota3))
print(f"Media: %.2f" % (media))
print(f">>status: {status}<<")
