from PyQt5 import uic,QtWidgets
import sqlite3
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

valor_id = 0

def funcao_principal():
    Código = tela_inicial.lineEdit.text() #Linha do Código
    Produto = tela_inicial.lineEdit_2.text() #Linha do Produto
    Quantidade = tela_inicial.lineEdit_3.text() #Linha da Quantidade de Produto
    Preço = tela_inicial.lineEdit_4.text() #Linha do Preço
    
    print("Código:",Código)
    print("Produto:",Produto)
    print("Quantidade: ",Quantidade)
    print("Preço:",Preço)
 

    Categoria = ""

    if tela_inicial.radioButton.isChecked() :
        print("Produto da catégoria Informática foi adicionado")
        Categoria = "Informática"
    elif tela_inicial.radioButton_2.isChecked() :
        print("Produto da catégoria Alimentos foi adicionado")
        Categoria = "Alimentos"
    elif tela_inicial.radioButton_3.isChecked() :
        print("Produto da catégoria Bebidas foi adicionado")
        Categoria = "Bebidas"
    elif tela_inicial.radioButton_4.isChecked() :
        print("Produto da catégoria Papelaria foi adicionado")
        Categoria = "Papelaria"
    elif tela_inicial.radioButton_5.isChecked() :
        print("Produto da catégoria Eletrônicos foi adicionado")
        Categoria = "Eletrônico"

    #Criando e conectando o banco
    banco = sqlite3.connect ('banco_produtos.db')
    cursor= banco.cursor ()
    cursor.execute("CREATE TABLE IF NOT EXISTS produtos (Código int PRIMARY KEY,Produto text,Preço real,Quantidade real,Categoria text,ValorTotal real)")
    #cursor.execute("INSERT INTO produtos VALUES ('"+Código+"','"+Produto+"','"+Preço+"','"+Quantidade+"','"+Categoria+"','"+Preço_Total+"')")
    cursor.execute("INSERT INTO produtos VALUES (?,?,?,?,?,?)", (Código,Produto,Quantidade,Preço,Categoria,float(Preço)*int(Quantidade)))
    banco.commit() 
    banco.close()

    #Limpando os campos
    tela_inicial.lineEdit.setText("")
    tela_inicial.lineEdit_2.setText("")
    tela_inicial.lineEdit_3.setText("")
    tela_inicial.lineEdit_4.setText("")




app=QtWidgets.QApplication([])
tela_inicial=uic.loadUi("Tela_Inicial.ui")
tela_inicial.pushButton.clicked.connect(funcao_principal)
tela_listar_produtos=uic.loadUi("Tela_Listar_Produtos.ui")


tela_inicial.show()
app.exec()