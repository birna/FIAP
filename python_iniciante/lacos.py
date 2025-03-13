print(">> PRIMEIRO LACO")
cont = 0
while cont < 5:
	print(f"Cont= ", cont)
	cont = cont + 1
else:
	print("Laco foi executado sem interrupcao")

print(">>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<\n\n")

cont = 0
print(">> SEGUNDO LACO (CONTINUE) - EXECUTA SOMENTE ATE O CONTINUE, DEPOIS VOLTA PARA O INICIO DO LACO")
while cont < 5:
	print("Cont= ", cont)
	cont = cont +1

	print("ANTES DO CONTINUE EXECUTA")
	continue #retorna para o inicio do loop
	print("DEPOIS DO CONTINUE NAO EXECUTA")
else:
	print("Laco foi executado sem interrupcao") #quando usa o continue, o else executa normalmente

print(">>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<\n\n")

cont = 0
print(">> TERCEIRO LACO (BREAK) - EXECUTA SOMENTE UMA VEZ")
while cont < 5:
	print("Cont= ", cont)
	cont = cont + 1
	break
else:
	print("Laco foi executado sem interrupcao") #quando usa o break, o else  nao executa
print(">>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<\n\n")
