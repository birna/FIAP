#while (enquanto)
#while true (faca-enquanto)
#for(para)

print("\n***********************************")
print("*** WHILE TRUE (FACA-ENQUANTO)  ***")
print("*** SOMA NUMEROS                ***")
print("*** Para sair do Loop, digite 0 ***")
print("***********************************\n")

soma = 0
while True:
	n = float(input("Digite um numero: "))
	soma = soma + n
	if n == 0:
		break

print(f"\n{'TOTAL:':>17} %.2f\n\n" % (soma)) #:>17 = alinha o total a direita com os outros textos


print("***********************************")
print("*** WHILE (ENQUANTO)            ***")
print("*** NOTA / MEDIA                ***")
print("***********************************\n")

msgErro = "Permitido apenas nota de 0 ate 10. Nota digitada: "


nota1 = float(input("Digite a nota 1: "))
while nota1 < 0 or nota1 > 10:
	print(f"%s%.f" % (msgErro, nota1))
	nota1 = float(input())

nota2 = float(input("Digite a nota 2: "))
while nota2 < 0 or nota2 > 10:
	print(f"%s%.f" % (msgErro, nota2))
	nota2 = float(input())


media = (nota1 + nota2) / 2
print(f"\n{'MEDIA:':>16} %.2f\n\n" % (media))

