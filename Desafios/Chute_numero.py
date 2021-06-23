import random
import os


numerof = random.randint(0,100)

op= False
while op == False:
    print("_____Chute o numero entre 0 e 100_____")
    numeroI = int(input("Chute um numero:"))
    if numeroI < numerof:
        print("Chutou baixo... ;)")
    elif numeroI > numerof:
        print("Chutou alto... ;)")
    elif numerof == numeroI:
        print("Parabéns!! Você acertou. ;)")
    else:
        print("Só chute numeros entre 0 e 100")
    op = input("Deseja tentar novamente?(y/n):")
    if op == "y":
        op = False
        os.system("cls")
    elif op == "n":
        op = True
        os.system("cls")
    else :
        print("Escolha entre y/n. ;)")
        os.system("cls")





