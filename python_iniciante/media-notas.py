nota1 = float(input("Digite a nota 1:"))
nota2 = float(input("Digite a nota 2:"))
nota3 = float(input("Digite a nota 3:"))

total = (nota1 + nota2 + nota3) / 3
print("\n\n>>    LOG")
print(f">>Nota1: %2.2f\n>>Nota2: %2.2f\n>>Nota3: %2.2f\n__________________ \n>>Media: %2.2f" % (nota1, nota2, nota3, total))
