valor = 8475.567
valor2 = 45.1345
valor3 = 45.1346

# Raiz
print(valor, valor2)

#format
#10  na formatacao equivale a 10 Bytes
#v1  equivale a um pseudonimo 
print("Valor 1={v1:10.2f} \nValor 2={v2:10.3f} \nValor 3={v3:10.3f}".format(v1=valor, v2=valor2, v3=valor3))
print("*******")
print(f"Valor 1 ={valor} \n Valor 2 = {valor2}")
print("\n")

inteiro1 = int(8475.333333)
print("*** 5 Bytes para inteiro ****")
print(f"Valor 1 = {inteiro1:5d} \n mascarando com float {inteiro1:5.2f}")
print(f"Valor preenchendo com mascara de numero, onde adiciono 0 nas 9 posicoes de Bytes \n>>{inteiro1:09d}")

print("\n************")
print("Aprendendo com percentual")
print(">>%o = Octal\n>>%d=Decimal\n>>%f=Float/real")

num0=0
num1=1
num2=2
num3=3
num4=4
num5=5
num6=6
num7=7
num8=8
num9=9
num10=10
num11=11
num100=100
num1000=1000
num10000=10000

print("DECIMAL PARA OCTAL")
print(f">>DECIMAL: %d, %d, %d -> OCTAL: %o, %o, %o;" % (num0, num1, num2, num0, num1, num2))
print(f">>DECIMAL: %d, %d, %d -> OCTAL: %o, %o, %o;" % (num3, num4, num5, num3, num4, num5))
print(f">>DECIMAL: %d, %d, %d -> OCTAL: %o, %o, %o;" % (num6, num7, num8, num6, num7, num8))
print(f">>DECIMAL: %d, %d, %d -> OCTAL: %o, %o, %o;" % (num9, num10, num11, num9, num10, num11))
print(f">>DECIMAL: %d, %d, %d -> OCTAL: %o, %o, %o;" % (num100, num1000, num10000, num100, num1000, num10000))



print("\n\n>>>FIM DO ARQUIVO<<<")
