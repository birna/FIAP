"""
OPERADORES ARITMETICOS:
	() - Parenteses
	== - Igual
	!= - Diferente
	>  - Maior
	>= - Maior Igual
	<  - Menor
	>= - Menor Igual

"""

a = 10
b = 3
c = 2

comparacao = a==b
print(f"A=%d \nB=%d \nC=%d\nCOMPARACAO: a==b\n________________________________\nRESULTADO:%s\n\n" % (a, b, c, comparacao))

comparacao = b > c
print(f"A=%d \nB=%d \nC=%d\nCOMPARACAO: b > c\n________________________________\nRESULTADO:%s\n\n" % (a, b, c, comparacao))

comparacao = a != c
print(f"A=%d \nB=%d \nC=%d\nCOMPARACAO: a != c\n________________________________\nRESULTADO:%s\n\n" % (a, b, c, comparacao))

comparacao = a == b * c
print(f"A=%d \nB=%d \nC=%d\nCOMPARACAO: a == b * c\n________________________________\nRESULTADO:%s\n\n" % (a, b, c, comparacao))

comparacao = (a + b) <= (a // c % b)
print(f"A=%d \nB=%d \nC=%d\nCOMPARACAO: (a + b) <= (a // c %% b)\n________________________________\nRESULTADO:%s\n\n" % (a, b, c, comparacao))
