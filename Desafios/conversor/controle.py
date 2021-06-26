from typing import Text
from PyQt5 import  uic,QtWidgets

def mult1000(x):
    x *= 1000
    print(x)
def mult1000000(x):
        x = x * 1000000
        print(x)
def div1000(x):
        x /= 1000
        print(x)

def div1000000(x):
        x /= 1000000
        print(x)
#Função principal 

def funcao_principal():
    linha1 = float(formulario.quant.text())

    print("Quantidade:{}".format(linha1))
#formula principal
    if formulario.kg.isChecked and formulario.G_check.isChecked():
            mult1000(linha1)
    elif formulario.kg.isChecked and formulario.mg_check.isChecked():
            mult1000000(linha1)
    elif formulario.g.isChecked and formulario.kg_check.isChecked():
            div1000(linha1)
    elif formulario.g.isChecked and formulario.mg_check.isChecked():
            div1000(linha1)
    elif formulario.mg.isChecked and formulario.kg_check.isChecked():
            div1000000(linha1)
    elif formulario.mg.isChecked and formulario.G_check.isChecked():
            div1000(linha1)

#controle de erro
    elif formulario.kg.isChecked and formulario.kg_check.isChecked():
        print("Você não pode selecionar a mesma opção para converter. ;)")
    elif formulario.g.isChecked and formulario.G_check.isChecked():
        print("Você não pode selecionar a mesma opção para converter. ;)")
    elif formulario.mg.isChecked and formulario.mg_check.isChecked():
        print("Você não pode selecionar a mesma opção para converter. ;)")


app=QtWidgets.QApplication([])
formulario=uic.loadUi("formulario2.ui")
formulario.convert.clicked.connect(funcao_principal)

formulario.show()
app.exec()