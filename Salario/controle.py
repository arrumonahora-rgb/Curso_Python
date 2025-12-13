# coding: utf-8
# Sua lógica de código começa aqui:
# ...

from PyQt5 import uic,QtWidgets

def principal():
    salario=float(input("digite o salario"))
    desconto=float(input("Ditite o desconto"))
    resultado=salario-desconto
    formulario=txtSalario.setText(str(salario))
    formulario=txtDesconto.setText(str(desconto))
    formulario=lblResultado.setText(str(resultado))


app=QtWidgets.QApplication([])
formulario=uic.loadUi("Salario/tela.ui")
formulario.show()
app.exec_()



