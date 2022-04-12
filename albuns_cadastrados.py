from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Álbuns Cadastrados")
root.geometry("1000x250")

with open("album.txt", "r", encoding="utf-8") as arqv:
    lista = [linha.split(',') for linha in arqv]

#widget treeview para alocar uma lista de itens
arvore = ttk.Treeview(root, columns=("lancamento", "album", "autor", "ano"), show="headings")
arvore.column("lancamento", width=100)
arvore.column("album", width=270)
arvore.column("autor", width=270)
arvore.column("ano", width=200)
arvore.column("lancamento", width=220)
arvore.heading("lancamento", text="PRIMEIRO LANÇAMENTO?")
arvore.heading("album", text="NOME DO ÁLBUM")
arvore.heading("autor", text="AUTOR DO ÁLBUM")
arvore.heading("ano", text="ANO DE LANÇAMENTO")
arvore.pack()

for a,b,c,d in lista:#adiciona item à arvore a cada lançamento, álbum, autor e ano da lista
    arvore.insert("", "end", values=(a,b,c,d))

root.mainloop()