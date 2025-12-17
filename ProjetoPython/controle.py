#encoding: utf-8
#Sua lógica de código começa aqui:

from PyQt5 import uic, QtWidgets


app=QtWidgets.QApplication([])
formulario=uic.loadUi('ProjetoPython/formulario.ui')
formulario.show() 
app.exec()