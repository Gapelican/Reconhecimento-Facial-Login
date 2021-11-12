
from sqlite3.dbapi2 import Cursor
from tkinter import *
from webcam import webcam
import cadastro
import sqlite3



def janela():
    master_tela_principal.destroy()
    master = Tk()
    master.title("Nova janela nivel - 1")
    master.geometry("490x560+200+153")
    master.resizable(width=1, height=1)    

    img_fundo = PhotoImage(file="imgTela/nivelUm.png")
    
    #criacao de labels
    lab_fundo = Label(master, image=img_fundo)
    #manter o rediconar para ficar no centro
    lab_fundo.pack()    
    master.mainloop()


    

def janela2():
    master_tela_principal.destroy()
    master = Tk()
    master.title("Nova janela nivel - 2")
    master.geometry("490x560+200+153")
    master.resizable(width=1, height=1)    
    img_fundo = PhotoImage(file="imgTela/nivelDois.png")
    lab_fundo = Label(master, image=img_fundo)
    lab_fundo.pack()    
    master.mainloop()


def janela3():
    master_tela_principal.destroy()
    master = Tk()
    master.title("Nova janela nivel - 3")
    master.geometry("490x560+200+153")
    master.resizable(width=1, height=1)    
    img_fundo = PhotoImage(file="imgTela/nivelTres.png")
    lab_fundo = Label(master, image=img_fundo)
    lab_fundo.pack()    
    master.mainloop()

def telaPrincipal():
    #tela
    global master_tela_principal
    master_tela_principal = Tk()
    master_tela_principal.title("Sistema de login")
    master_tela_principal.geometry("490x560+610+153")
    master_tela_principal.resizable(width=1, height=1)
            
    #importar imagens
    img_fundo = PhotoImage(file="imgTela/fundo.png")
    img_botao = PhotoImage(file="imgTela/botao.png")
    img_rf = PhotoImage(file="imgTela/rf.png")
    img_cadastrarT = PhotoImage(file="imgTela/cadastrarT.png")


    #criacao de labels
    lab_fundo = Label(master_tela_principal, image=img_fundo)
    #manter o rediconar para ficar no centro
    lab_fundo.pack()


    # varial global
    global nome_login
    global senha_login
    #criacao de caixas de entrada
    nome_login = Entry(master_tela_principal, bd=2, font=("Calibri", 15), justify=LEFT, background="#F8F8F8", borderwidth=0 )
    nome_login.place(width=400, height=60, x=50, y=178 )

    senha_login = Entry(master_tela_principal, bd=2, font=("Calibri", 15), justify=LEFT, background="#F8F8F8",  borderwidth=0, show="*")
    senha_login.place(width=400, height=60, x=50, y=299 )

    #criacao de botoes
    botao = Button(master_tela_principal, bd=0, image=img_botao, command=verificaSenha)
    botao.place(width=195, height=80, x=95, y=428)

    botao = Button(master_tela_principal, bd=0, image=img_rf, command=cam)
    botao.place(width=95, height=80, x=300, y=428)

    botao = Button(master_tela_principal, bd=0, image=img_cadastrarT, command=irParaCadastro)
    botao.place(width=180, height=27, x=155, y=520)

    master_tela_principal.mainloop()

def cam():
    resultado = webcam()
    print(resultado)
    if resultado[0] == True:
        janela()
    if resultado[1] == True:
        janela2()
    if resultado[2] == True:
        janela3()

def verificaSenha():
    nomeR = nome_login.get()
    senhaR = str(senha_login.get())

    banco = sqlite3.connect('banco_cadastro.db') 
    cursor = banco.cursor()
    cursor.execute("SELECT nome, senha, nivel FROM cadastro WHERE nome == :nomeinput and senha == :senhainput", {"nomeinput": nomeR, "senhainput": senhaR})
    
    rows = cursor.fetchall()

    for row in rows:
        print(rows)
        nome_banco = row[0]
        senha_banco = row[1]
        nivel_banco = row[2]

    print(nome_banco)
    print(senha_banco)
    print(nivel_banco)
    

    if (nomeR == nome_banco and senhaR == senha_banco and nivel_banco == '1'):
        janela()
    if(nomeR == nome_banco and senhaR == senha_banco and nivel_banco == '2'):
        janela2()
    if(nomeR == nome_banco and senhaR == senha_banco and nivel_banco == '3'):
        janela3()

def irParaCadastro():
    master_tela_principal.destroy()   
    cadastro.telaDeCadastro()
    



    



