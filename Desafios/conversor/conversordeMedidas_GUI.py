from typing import Text
from PyQt5 import  uic,QtWidgets

#funções de calculo;
def mult1000(x):
        x *= 1000
        msg.setWindowTitle("Conversão realizada!")
        msg.setText("Resultado:{}".format(x))
        msg.exec()
def mult1000000(x):
        x *= 1000000
        msg.setWindowTitle("Conversão realizada!")
        msg.setText("Resultado:{}".format(x))
        msg.exec()
def div1000(x):
        x /= 1000
        msg.setWindowTitle("Conversão realizada!")
        msg.setText("Resultado:{}".format(x))
        msg.exec()
def div1000000(x):
        x /= 1000000
        msg.setWindowTitle("Conversão realizada!")
        msg.setText("Resultado:{}".format(x))
        msg.exec()
#Função principal; 
def funcao_principal():
        linha1 = float(formulario.quant.text())
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
#controle de erros;
        elif formulario.kg.isChecked and formulario.kg_check.isChecked():
                erro.setWindowTitle("ERRO")
                erro.setText("Você não pode converter para a mesma unidade. ;)")
                erro.exec()
        elif formulario.g.isChecked and formulario.G_check.isChecked():
                erro.setWindowTitle("ERRO")
                erro.setText("Você não pode converter para a mesma unidade. ;)")
                erro.exec()
        elif formulario.mg.isChecked and formulario.mg_check.isChecked():
                erro.setWindowTitle("ERRO")
                erro.setText("Você não pode converter para a mesma unidade. ;)")
                erro.exec()
        formulario.quant.setText("")
#Funções padronizadas;
app=QtWidgets.QApplication([])
msg = QtWidgets.QMessageBox()
erro = QtWidgets.QMessageBox
formulario=uic.loadUi("formulario2.ui")
formulario.convert.clicked.connect(funcao_principal)
formulario.show()
app.exec()