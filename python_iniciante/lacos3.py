aprovado  = 0
reprovado = 0

for voltas in range(1,11,1):
	media = float(input("Digite a media: "))

	if media >= 6:
		aprovado = aprovado +1
	else:
		reprovado = reprovado + 1

print(f">> {'APROVADO:':>10} %02d\n>> REPROVADO: %02d" % (aprovado, reprovado))
