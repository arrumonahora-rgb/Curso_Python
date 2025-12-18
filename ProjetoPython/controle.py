# -*- coding: utf-8 -*-
from PySide6 import QtWidgets, QtUiTools
import mysql.connector
import sys

# Tente conectar ao banco
try:
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='cadastro_produtos'
    )
    print("Conexão estabelecida com sucesso!")
except Exception as e:
    print(f"Erro ao conectar ao banco: {e}")
    sys.exit(1) # Encerra o programa se não houver banco
   
# Função para inserir um produto    
def inserir():
    # Coletando os dados (Correção do nome 'formulario')
    produto = formulario.txtProduto.text()
    preco = formulario.txtPreco.text()
    estoque = formulario.txtEstoque.text()

    try:
        cursor = conexao.cursor()
        comando_SQL = 'INSERT INTO produtos (produto, preco, estoque) VALUES (%s, %s, %s)'
        dados = (produto, preco, estoque)    
        cursor.execute(comando_SQL, dados)
        conexao.commit()
        
        # Limpar os campos após o cadastro
        formulario.txtProduto.setText("")
        formulario.txtPreco.setText("")
        formulario.txtEstoque.setText("")
        print("Produto cadastrado com sucesso!")
        
    except Exception as e:
        print(f"Erro ao inserir dados: {e}")

app = QtWidgets.QApplication(sys.argv)

# Carregamento do arquivo .ui
loader = QtUiTools.QUiLoader()
formulario = loader.load('formulario.ui', None)

if formulario:
    btn = formulario.findChild(QtWidgets.QPushButton, 'btnCadastrar')
    if btn:
        btn.clicked.connect(inserir)
    else:
        print("Widget 'btnCadastrar' não encontrado no formulário.")
    formulario.show()
    sys.exit(app.exec())
else:
    print("Não foi possível carregar o arquivo formulario.ui")