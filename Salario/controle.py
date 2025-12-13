# coding: utf-8
# Sua lógica de código começa aqui:
# ...

from PyQt5 import uic,QtWidgets

def principal():
    salario=float(formulario.txtSalario.text())
    desconto=float(formulario.txtDesconto.text())
    resultado= salario-desconto
    formulario.lblResultado.setText(str(resultado))
    formulario.lblSalario.setText(str(salario))
    formulario.lblDesconto.setText(str(desconto))

    
    
    
    
    
    
    
    
    
    
    

app=QtWidgets.QApplication([])
formulario=uic.loadUi("Salario/tela.ui")
formulario.btnCalcular.clicked.connect(principal)
formulario.show()
app.exec_()



