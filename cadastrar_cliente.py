from PyQt5 import  uic,QtWidgets
import sqlite3


def cadastrar():
    nome = tela_cadastro.lineEdit.text()
    login = tela_cadastro.lineEdit_2.text()
    senha = tela_cadastro.lineEdit_3.text()
    r_senha = tela_cadastro.lineEdit_4.text()

    if (senha == r_senha):
        try:
            #Faz um connect no db
            banco = sqlite3.connect('banco_cadastro.db') 
            cursor = banco.cursor()
            #Cria uma tabala com nome Cadastro com nome, login e senha
            cursor.execute("CREATE TABLE IF NOT EXISTS cadastro (nome text,login text,senha text)")
            #Insere os valores na tabela Cadastro
            #cursor.execute("INSERT INTO cadastro VALUES ('"+nome+"','"+login+"','"+senha+"')")
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
tela_cadastro = uic.loadUi("tela_cadastro.ui")
tela_cadastro.pushButton.clicked.connect(cadastrar)

tela_cadastro.show()
app.exec()