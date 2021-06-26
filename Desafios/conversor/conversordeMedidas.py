import os
print('___________Olá! bem vindo ao conversor de medidas.___________')
#Irei separar as grandezas para ficar mais facil! ao longo do tempo vou ajustando.
print("Medidas de massa:\n1-KG  2-g\n 3-mg")
op1 = ""
op2 = ""
sinal = ""
medida1 = float(input("Qual medida você deseja:"))
quant = float(input("Quanto você quer converter dessa medida:"))
if medida1 == 1:
    op1 = "KG"
elif medida1 == 2:
    op1 = "Gramas"
elif medida1 == 3:
    op1 = "Miligramas"
medida2 = int(input("Deseja converter {} para:".format(op1)))
if medida2 == 1:
    op2 = "KG"
elif medida2 == 2:
    op2 = "Gramas"
elif medida2 == 3:
    op2 = "Miligramas"
#calculo das conversões de KG para as outras medidas
if medida1 == 1 and medida2 == 2:
    quant = quant * 1000
elif medida1 == 1 and medida2 == 3:
    quant = quant * 1000000
#calculo das conversões de G para as outras medidas
if medida1 == 2 and medida2 == 1:
    quant = quant / 1000
elif medida1 == 2 and medida2 == 3:
    quant = quant * 1000
#calculo das conversões de miligramas para as outras medidas
if medida1 == 3 and medida2 == 1:
    quant = quant / 100000
elif medida1 == 3 and medida2 == 2:
    quant = quant / 1000
os.system("cls")
print("{} para {}={} {}".format(op1,op2,quant,op2))
