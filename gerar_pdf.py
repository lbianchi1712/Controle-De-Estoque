from PyQt5 import uic,QtWidgets
import sqlite3
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4



def gerar_pdf():
    banco = sqlite3.connect ('banco_produtos.db')
    cursor = banco.cursor ()
    comando_SQL = "SELECT * FROM produtos"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()

    y = 0
    pdf = canvas.Canvas("Produtos_Cadastrado.pdf",pagesize=A4)
    pdf.drawString(200,800,"Produtos Cadastrado")
    pdf.drawString(10,750, "Código")
    pdf.drawString(110,750, "Produto")
    pdf.drawString(210,750, "Quantidade")
    pdf.drawString(310,750, "Preço")
    pdf.drawString(410,750, "Catégoria")
    pdf.drawString(510,750, "Preço Total")

    for i in range(0, len(dados_lidos)):
        y = y + 50
        pdf.drawString(10,750 - y, str(dados_lidos[i][0]))
        pdf.drawString(110,750 - y, str(dados_lidos[i][1]))
        pdf.drawString(210,750 - y, str(dados_lidos[i][2]))
        pdf.drawString(310,750 - y, str(dados_lidos[i][3]))
        pdf.drawString(410,750 - y, str(dados_lidos[i][4]))
        pdf.drawString(510,750 - y, str(dados_lidos[i][5]))

    pdf.save()
    print("PDF")


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
tela_inicial=uic.loadUi("tela_inicial.ui")
tela_listar_produtos=uic.loadUi("Tela_Listar_Produtos.ui")
tela_inicial.pushButton_2.clicked.connect(chamar_listar_produtos)
tela_listar_produtos.pushButton.clicked.connect(gerar_pdf)


tela_inicial.show()
app.exec()