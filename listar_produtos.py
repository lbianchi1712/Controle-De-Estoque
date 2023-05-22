from PyQt5 import uic,QtWidgets
import sqlite3
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

def chamar_listar_produtos() :
    tela_listar_produtos.show()

    banco = sqlite3.connect ('banco_produtos.db')
    cursor = banco.cursor ()
    comando_SQL = "SELECT * FROM produtos"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    
    tela_listar_produtos.tableWidget.setRowCount(len(dados_lidos))
    tela_listar_produtos.tableWidget.setColumnCount(6)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 6):
            tela_listar_produtos.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


app=QtWidgets.QApplication([])
tela_inicial=uic.loadUi("Tela_Inicial.ui")
tela_listar_produtos=uic.loadUi("Tela_Listar_Produtos.ui")
tela_inicial.pushButton_2.clicked.connect(chamar_listar_produtos)



tela_inicial.show()
app.exec()