from PyQt5 import  uic,QtWidgets

def funcao_principal():
    print("Hello world")
    
    
app=QtWidgets.QApplication([])
formulario=uic.loadUi("formulario.ui")
formulario.pushButton.clicked.connect(funcao_principal)

formulario.show()
app.exec()  