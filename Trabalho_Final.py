from PyQt5 import  uic,QtWidgets
import sqlite3
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from PyQt5.QtWidgets import QDialog, QApplication

valor_id = 0

def funcao_principal():
    Código = tela_inicial.lineEdit.text()
    Produto = tela_inicial.lineEdit_2.text()
    Preço = tela_inicial.lineEdit_3.text()
    Quantidade = tela_inicial.lineEdit_4.text()
    
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

    banco = sqlite3.connect ('banco_produtos.db')
    cursor= banco.cursor ()
    cursor.execute("CREATE TABLE IF NOT EXISTS produtos (Código int PRIMARY KEY,Produto text,Preço real,Quantidade int,Categoria text,ValorTotal real)")
    cursor.execute("INSERT INTO produtos VALUES (?,?,?,?,?,?)", (Código,Produto,Preço,Quantidade,Categoria,float(Preço)*int(Quantidade)))
    banco.commit() 
    banco.close()

    tela_inicial.lineEdit.setText("")
    tela_inicial.lineEdit_2.setText("")
    tela_inicial.lineEdit_3.setText("")
    tela_inicial.lineEdit_4.setText("")

def chamar_listar_produtos() :
    tela_listar_produtos.show()

    banco = sqlite3.connect ('banco_produtos.db')
    cursor = banco.cursor ()
    comando_SQL = "SELECT * FROM produtos ORDER BY Código ASC"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    
    tela_listar_produtos.tableWidget.setRowCount(len(dados_lidos))
    tela_listar_produtos.tableWidget.setColumnCount(6)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 6):
            tela_listar_produtos.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

def excluir_dados():
    linha = tela_listar_produtos.tableWidget.currentRow()
    tela_listar_produtos.tableWidget.removeRow(linha)

    banco = sqlite3.connect ('banco_produtos.db')
    cursor = banco.cursor()
    cursor.execute("SELECT Código FROM produtos")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor = banco.cursor()
    cursor.execute("DELETE FROM produtos WHERE Código="+ str(valor_id))
    banco.commit()

def gerar_pdf():
    banco = sqlite3.connect ('banco_produtos.db')
    cursor = banco.cursor ()
    comando_SQL = "SELECT * FROM produtos ORDER BY Código ASC"
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
    print("PDF Gerado com sucesso")

def editar_dados():
    global valor_id
    tela_editar.show()

    linha = tela_listar_produtos.tableWidget.currentRow()

    banco = sqlite3.connect ('banco_produtos.db')
    cursor = banco.cursor()
    cursor.execute("SELECT Código FROM produtos ORDER BY Código ASC")
    dados_lidos = cursor.fetchall()
    print(linha)
    print(dados_lidos)
    valor_código = dados_lidos[linha][0]
    print(valor_código)
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
    global valor_id

    Código = tela_editar.lineEdit.text()
    Produto = tela_editar.lineEdit_2.text()
    Preço = tela_editar.lineEdit_3.text()
    Quantidade = tela_editar.lineEdit_4.text()
    Categoria = tela_editar.lineEdit_5.text()
    
    banco = sqlite3.connect ('banco_produtos.db')
    cursor = banco.cursor()
    cursor.execute("UPDATE produtos SET Código = '{}', Produto = '{}', Preço = '{}', Quantidade = '{}', Categoria = '{}', ValorTotal = '{}'  WHERE Código = {}".format(Código, Produto, Preço, Quantidade, Categoria, (float(Preço)*int(Quantidade)), valor_id))
    banco.commit()
    
    tela_editar.close()
    tela_inicial.close()
    tela_inicial.show()
    chamar_listar_produtos()

def chama_segunda_tela():
    tela_login.label_3.setText("")
    nome_usuario = tela_login.lineEdit.text()
    senha = tela_login.lineEdit_2.text()
    banco = sqlite3.connect('banco_cadastro.db')
    cursor = banco.cursor()
    try:
        cursor.execute("SELECT senha FROM cadastro WHERE login = '{}'".format(nome_usuario))
        senha_db = cursor.fetchone()
        banco.close()         
    except:
        print("Erro na validação do login")

    if senha_db and senha == senha_db[0]:
        tela_login.close()
        tela_inicial.show()
    else :
        tela_login.label_3.setText("                Dados de login incorretos!")

def abre_tela_cadastro():
    tela_cadastro.show()

def cadastrar():
    nome = tela_cadastro.lineEdit.text()
    login = tela_cadastro.lineEdit_2.text()
    senha = tela_cadastro.lineEdit_3.text()
    r_senha = tela_cadastro.lineEdit_4.text()

    if (senha == r_senha):
        try:
            banco = sqlite3.connect('banco_cadastro.db') 
            cursor = banco.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS cadastro (nome text,login text,senha text)")
            cursor.execute("INSERT INTO cadastro VALUES (?,?,?)", (nome,login,senha))

            banco.commit() 
            banco.close()
            tela_cadastro.label.setText("Usuario cadastrado com sucesso")

        except sqlite3.Error as erro:
            print("Erro ao inserir os dados: ",erro)
    else:
        tela_cadastro.label.setText("As senhas digitadas estão diferentes")
    tela_cadastro.close()

app=QtWidgets.QApplication([])
tela_login = uic.loadUi("Tela_de_Login.ui")
tela_cadastro = uic.loadUi("Tela_Cadastro.ui")
tela_login.pushButton.clicked.connect(chama_segunda_tela)
tela_login.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
tela_login.pushButton_2.clicked.connect(abre_tela_cadastro)
tela_cadastro.pushButton.clicked.connect(cadastrar)
tela_inicial=uic.loadUi("tela_inicial.ui")
tela_inicial.pushButton.clicked.connect(funcao_principal)
tela_listar_produtos=uic.loadUi("Tela_Listar_Produtos.ui")
tela_inicial.pushButton_2.clicked.connect(chamar_listar_produtos)
tela_listar_produtos.pushButton.clicked.connect(gerar_pdf)
tela_listar_produtos.pushButton_2.clicked.connect(excluir_dados)
tela_editar=uic.loadUi("Tela_Editar.ui")
tela_listar_produtos.pushButton_3.clicked.connect(editar_dados)
tela_editar.pushButton.clicked.connect(salvar_dados_editado)

tela_login.show()
app.exec()