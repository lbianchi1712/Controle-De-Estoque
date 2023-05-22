from PyQt5 import  uic,QtWidgets
import sqlite3

def chama_segunda_tela():
    primeira_tela.label_3.setText("")
    nome_usuario = primeira_tela.lineEdit.text()
    senha = primeira_tela.lineEdit_2.text()
    #Chamar o banco de dados
    banco = sqlite3.connect('banco_cadastro.db')
    cursor = banco.cursor()
    try:
        #Faz um select em Cadastro na parte de Login
        cursor.execute("SELECT senha FROM cadastro WHERE login = '{}'".format(nome_usuario))
        senha_db = cursor.fetchall()
        print(senha_db[0][0])
        banco.close()
    except:
        print("Erro na validação do login")

    if senha == senha_db[0][0]:
        primeira_tela.close()
        segunda_tela.show()
    else :
        primeira_tela.label_3.setText("                         Senha Incorreta!")


def abre_tela_cadastro():
    tela_cadastro.show()


app=QtWidgets.QApplication([])
primeira_tela=uic.loadUi("Tela_de_Login.ui")
segunda_tela = uic.loadUi("Tela_Inicial.ui")
tela_cadastro = uic.loadUi("tela_cadastro.ui")
primeira_tela.pushButton.clicked.connect(chama_segunda_tela)
primeira_tela.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
primeira_tela.pushButton_2.clicked.connect(abre_tela_cadastro)
#tela_cadastro.pushButton.clicked.connect(cadastrar)


primeira_tela.show()
app.exec()


