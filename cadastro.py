from tkinter import *
from tirarFoto import tirarFoto
import tela
import sqlite3
import os



def foto():
    nome_foto = nome_cadastro.get()
    tirarFoto(nome_foto)    


def cadastroUsuario():
    nomeC = nome_cadastro.get()
    senhaC = senha_cadastro.get()
    nivelC = nivel_cadastro.get()

    path = "./img/"
    for raiz, diretorios, arquivos in os.walk(path):
        for file in arquivos:
            if file == nomeC + '.png':
                caminho_destino = file


    banco = sqlite3.connect('banco_cadastro.db') 
    cursor = banco.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS cadastro (nome text,senha text, nivel text, caminho_destino text)")
    cursor.execute("INSERT INTO cadastro VALUES ('"+nomeC+"','"+senhaC+"', '"+nivelC+"', '"+caminho_destino+"')")

    banco.commit() 
    banco.close()
    print("Usuario cadastrado com sucesso")

  




def telaDeCadastro():    
    global master_cadastro
    master_cadastro = Tk()
    master_cadastro.title("Sistema de login")
    master_cadastro.geometry("490x560+610+153")
    master_cadastro.resizable(width=1, height=1)
            
    #importar imagens
    img_fundo = PhotoImage(file="imgTela/cadastro.png")
    img_botao = PhotoImage(file="imgTela/cadastrar.png")
    img_rf = PhotoImage(file="imgTela/rf.png")
    img_voltar = PhotoImage(file="imgTela/voltar.png")

    #criacao de labels
    lab_fundo = Label(master_cadastro, image=img_fundo)
    #manter o rediconar para ficar no centro
    lab_fundo.pack()

    global nome_cadastro
    global senha_cadastro
    global nivel_cadastro

    #criacao de caixas de entrada
    nome_cadastro = Entry(master_cadastro, bd=2, font=("Calibri", 15), justify=LEFT, background="#F8F8F8", borderwidth=0 )
    nome_cadastro.place(width=400, height=60, x=50, y=178 )

    senha_cadastro = Entry(master_cadastro, bd=2, font=("Calibri", 15), justify=LEFT, background="#F8F8F8",  borderwidth=0, show="*")
    senha_cadastro.place(width=190, height=60, x=50, y=295 )

    nivel_cadastro = Entry(master_cadastro, bd=2, font=("Calibri", 15), justify=LEFT, background="#F8F8F8",  borderwidth=0, )
    nivel_cadastro.place(width=190, height=60, x=260, y=295 )

    #criacao de botoes
    botao = Button(master_cadastro, bd=0, image=img_botao, command=cadastroUsuario)
    botao.place(width=195, height=80, x=95, y=428)

    botao = Button(master_cadastro, bd=0, image=img_rf, command=foto )
    botao.place(width=95, height=80, x=300, y=428)

    botao = Button(master_cadastro, bd=0, image=img_voltar, command=voltarLogin)
    botao.place(width=180, height=27, x=155, y=520)

    master_cadastro.mainloop()
    
def voltarLogin():
   master_cadastro.destroy()
   tela.telaPrincipal()
    
    
    





