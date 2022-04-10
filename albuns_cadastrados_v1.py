from tkinter import *
from tkinter import ttk

root = Tk()
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

for a,b,c,d in lista:
    arvore.insert("", "end", values=(a,b,c,d))

root.mainloop()
