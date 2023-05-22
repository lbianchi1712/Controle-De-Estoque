from PyQt5 import uic,QtWidgets
import sqlite3
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

def editar_dados():
    global valor_id
    tela_editar.show()

    linha = tela_listar_produtos.tableWidget.currentRow()

    banco = sqlite3.connect ('banco_produtos.db')
    cursor = banco.cursor()
    cursor.execute("SELECT Código FROM produtos")
    dados_lidos = cursor.fetchall()
    valor_código = dados_lidos[linha][0]
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM produtos WHERE Código="+ str(valor_código))
    produto = cursor.fetchall()

    valor_id = valor_código

    tela_editar.lineEdit.setText(str(produto[0][0]))
    tela_editar.lineEdit_2.setText(str(produto[0][1]))
    tela_editar.lineEdit_3.setText(str(produto[0][2]))
    tela_editar.lineEdit_4.setText(str(produto[0][3]))
    tela_editar.lineEdit_5.setText(str(produto[0][4]))

    banco.commit()

def salvar_dados_editado():
    #Pegar numero do código
    global valor_id
    #Pegar valor digitado nos LineEdit
    Código = tela_editar.lineEdit.text()
    Produto = tela_editar.lineEdit_2.text()
    Quantidade = tela_editar.lineEdit_3.text()
    Preço = tela_editar.lineEdit_4.text()
    Categoria = tela_editar.lineEdit_5.text()
    #Atualizar dados no banco
    banco = sqlite3.connect ('banco_produtos.db')
    cursor = banco.cursor()
    cursor.execute("UPDATE produtos SET Código = '{}', Produto = '{}', Quantidade = '{}', Preço = '{}', Categoria = '{}' WHERE Código = {}".format(Código, Produto, Quantidade, Preço, Categoria, valor_id))
    banco.commit()
    #Atualizando Tela
    tela_editar.close()
    tela_inicial.close()
    tela_inicial.show()
    chamar_listar_produtos()

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
tela_editar=uic.loadUi("Tela_Editar.ui")
tela_listar_produtos.pushButton_3.clicked.connect(editar_dados)
tela_editar.pushButton.clicked.connect(salvar_dados_editado)


tela_inicial.show()
app.exec()