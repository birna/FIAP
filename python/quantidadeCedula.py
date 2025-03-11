valor = int(input("Digite o valor do SAQUE: R$ "))

cedula100  = valor // 100
valor = valor % 100

cedula50   = valor // 50
valor   = valor % 50

cedula20  = valor // 20
valor  = valor % 20

cedula10  = valor // 10
valor  = valor % 10

cedula5   = valor // 5
valor  = valor % 5

print(">>    LOG")
print(f"R$ 100.00 : %3d" % (cedula100))
print(f"R$  50.00 : %3d" % (cedula50))
print(f"R$  20.00 : %3d" % (cedula20))
print(f"R$  10.00 : %3d" % (cedula10))
print(f"R$   5.00 : %3d" % (cedula5))
