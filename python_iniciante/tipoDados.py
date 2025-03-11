"""
inteiro = int
real = float
texto = str
logica = bool
"""
nome       = "Guilherme Urbinatti"
idade      = 33
salario    = 1500.00 
casado     = False
maiorIdade = True

print("Tipo de Dados")
print(">>NOME:" + "Guilherme Urbinatti  Type: STR")
print(">>IDADE:", idade, "TYPE: INT" )
print(">>SALARIO:", salario, "TYPE: FLOAT")
print(">>CASADO:", casado, "TYPE: BOOL")
print(">>+18:", maiorIdade, "TYPE: BOOL")

print(f"\nFUNCTION type(variable) \n%s %s %s %s %s" % (type(nome), type(idade), type(salario), type(casado), type(maiorIdade)))

casting = "Variavel casting com valor de texto"
print("\n\n****CASTING")
print(f"Valor da variavel: %s TYPE: %s" % (casting, type(casting)))

casting = 1
print(f"Valor da variavel: %d TYPE: %s" % ( casting, type(casting)))

casting = 1.1
print(f"Valor da variavel: %f TYPE: %s" % ( casting, type(casting)))

casting = True
print(f"Valor da variavel: %s TYPE: %s" % ( casting, type(casting)))


num1 = 10 #Qualquer numero diferente de 0 retorna true para boolean
num2 = 0 #Somente o 0 retorna falso para casting boolean

casting = bool(num1)
print(f"Value: %s Type: %s" % ( casting, type(casting)))
casting = bool(num2)
print(f"Value: %s Type: %s" % ( casting, type(casting)))
