#OPERADORES ARITIMETICOS
"""
	() - Parenteses
	** - Exponenciacao
	*  - Multiplicacao
	/  - Divisao
	// - Divisao Inteira
	%  - Resto da divisao
	+  - Adicao
	-  - Subtracao
"""

a = 2
b = 5
total = a ** b
print(f"A= %f ** B= %f \n-----------------------------\nTOTAL= %f\n\n"  % (a,b,total))

total = a * b
print(f"A= %f * B= %f  \n-----------------------------\nTOTAL= %f\n\n"  % (a,b,total))

total = b / a
print(f"A= %f / B= %f  \n-----------------------------\nTOTAL= %f\n\n"  % (a,b,total))

total = b // a
print(f"A= %f // B= %f \n-----------------------------\nTOTAL= %f\n\n"  % (a,b,total))

total = b % a
print(f"A= %f %%  B= %f   \n-----------------------------\nTOTAL= %f\n\n"  % (a,b,total))

total = a + b
print(f"A= %f + B= %f  \n-----------------------------\nTOTAL= %f\n\n"  % (a,b,total))

total = a - b
print(f"A= %f - B= %f  \n-----------------------------\nTOTAL= %f\n\n"  % (a,b,total))


print(">>>>> EXEMPLOS AULA <<<<<\n\n")
a = 10
b = 3
c = 2

total = b ** c
print(f"A=%d B=%d C=%d \nFORMULA: b ** c\n-----------------------------------\nTOTAL= %10.2f\n\n" % (a,b,c,total))


total = a + b * c
print(f"A=%d B=%d C=%d \nFORMULA: a + b * c\n-----------------------------------\nTOTAL= %10.2f\n\n" % (a,b,c,total))

total = (a + b) * c
print(f"A=%d B=%d C=%d \nFORMULA: (a + b) * c\n-----------------------------------\nTOTAL= %10.2f\n\n" % (a,b,c,total))


total = a + b + c / 3
print(f"A=%d B=%d C=%d \nFORMULA: a + b + c / 3\n-----------------------------------\nTOTAL= %10.2f\n\n" % (a,b,c,total))

total = a % b
print(f"A=%d B=%d C=%d \nFORMULA: a %% b\n-----------------------------------\nTOTAL= %10.2f\n\n" % (a,b,c,total))

total = c - b % a
print(f"A=%d B=%d C=%d \nFORMULA: c - b %% a\n-----------------------------------\nTOTAL= %10.2f\n\n" % (a,b,c,total))

total = a / b
print(f"A=%d B=%d C=%d \nFORMULA: a / b\n-----------------------------------\nTOTAL= %10.2f\n\n" % (a,b,c,total))

total = a // b
print(f"A=%d B=%d C=%d \nFORMULA: a // b\n-----------------------------------\nTOTAL= %10.2f\n\n" % (a,b,c,total))

total = a + b % c + c // b
print(f"A=%d B=%d C=%d \nFORMULA: a + b %% c + c // b\n-----------------------------------\nTOTAL= %10.2f\n\n" % (a,b,c,total))
