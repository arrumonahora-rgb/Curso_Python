#encoding: utf-8
#Sua lógica de código começa aqui:

from PyQt5 import uic, QtWidgets
import mysql.connector
msql = mysql.connector.connect (
    host = 'Localhost', user = 'root', passwd = '', database = 'cadastro_produtos')


app=QtWidgets.QApplication([])
formulario=uic.loadUi('ProjetoPython/formulario.ui')
formulario.show() 
app.exec()