numero = int(input("Digite um numero: "))
multiplo = int(input("Digite o multiplo desejado: "))

proximo = numero // multiplo * multiplo + multiplo 

print(">>     LOG")
print(f"O Proximo multiplo disponive: %d" % (proximo))
