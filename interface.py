from tkinter import *
from tkinter import ttk
import operacoes as ops

def tela_cadastro():
    global root
    root = Tk()
    root.title("Cadastrar Álbum")
    root.geometry("400x400")

    global nome_album, ano, nome_criador, lancamento, mensagem
    nome_album = StringVar()
    ano = StringVar()
    nome_criador = StringVar()
    lancamento = IntVar()
    mensagem = StringVar()

    Label(root, text="Nome do álbum: ", font=("Calibri")).place(x=10, y=40)
    Entry(root, textvariable=nome_album).place(x=170, y=42)

    Label(root, text="Criador do Álbum: ", font=("Calibri")).place(x=10, y=80)
    Entry(root, textvariable=nome_criador).place(x=170, y=82)

    Label(root, text="Ano de Lançamento: ", font=("Calibri")).place(x=10, y=120)
    Entry(root, textvariable=ano).place(x=170, y=122)

    Label(root, text="Álbum de lançamento?", font=("Calibri",)).place(x=10, y=160)
    Radiobutton(root, text="Sim", variable=lancamento, value=1).place(x=170, y=160)
    Radiobutton(root, text="Não", variable=lancamento, value=0).place(x=230, y=160)

    Button(root, width=10, bg="blue", fg="white", text="Cadastar álbum", font=("Calibri", 11),
           command=lambda: ops.registro(nome_album, ano, nome_criador, lancamento)).place(
        x=140, y=240)

    Button(root, width=10, bg="red", fg="white", text="Sair", command=root.quit, font=("Calibri", 11)).place(x=140,
                                                                                                             y=280)

    Label(root, text="", textvariable=mensagem).place(x=140, y=320)

    root.mainloop()


def bandas_cadastradas():
    root.title("Álbuns Cadastrados")
    root.geometry("1000x250")

    arqv = open("album.txt", "r")
    lista = [linha.split(',') for linha in arqv.readlines()]

    arvore = ttk.Treeview(root, columns=("lancamento", "album", "autor", "ano"), show="headings")
    arvore.column("lancamento", minwidth=0, width=100)
    arvore.column("album", minwidth=0, width=270)
    arvore.column("autor", minwidth=0, width=270)
    arvore.column("ano", minwidth=0, width=200)
    arvore.column("lancamento", width=220)
    arvore.heading("lancamento", text="PRIMEIRO LANÇAMENTO?")
    arvore.heading("album", text="NOME DO ÁLBUM")
    arvore.heading("autor", text="AUTOR DO ÁLBUM")
    arvore.heading("ano", text="ANO DE LANÇAMENTO")
    arvore.pack()

    for a, b, c, d in lista:
        arvore.insert("", "end", values=(a, b, c, d))

    root.mainloop()
