nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))

media = (nota1 + nota2 + nota3) / 3

nota1Invalid = nota1 < 0 or nota1 > 10
nota2Invalid = nota2 < 0 or nota2 > 10
nota3Invalid = nota3 < 0 or nota3 > 10


if nota1Invalid or nota2Invalid or nota3Invalid:
	print("\n############################################################################")
	print("####  Erro ao calcular media, digite apenas notas validas entre 0 e 10.#####")
	print("############################################################################\n\n")
else:
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
