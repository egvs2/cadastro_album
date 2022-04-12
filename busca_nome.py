from tkinter import *
from tkinter import ttk 
from tkinter.ttk import Combobox


def busca_nome(nome_artista, mensagem, ttk, root_nome):

    with open("album.txt", "r") as arqv:
        lista_albuns = [linha.split(",") for linha in arqv]

    nome_artista1 = nome_artista.get()
    l_nomes = []

    if nome_artista1 == "":
        mensagem.set("Nome inválido!")
    else:
        for i in lista_albuns:
            if nome_artista1.upper() in i[2].upper():
                l_nomes.append(i)
            l_nomes.sort(key=lambda l:l[2])

    arvore = ttk.Treeview(root_nome, columns=("lancamento", "album", "autor", "ano"), show="headings")
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

    for a,b,c,d in l_nomes:
        arvore.insert("", "end", values=(a,b,c,d))




global nome_artista, lista_albuns, root_nome, mensagem
root_nome = Tk()
root_nome.title("Busca por Nome")
root_nome.geometry("1000x500")

nome_artista = StringVar()
mensagem = StringVar()

Label(root_nome, text="Insira o nome do artista/banda:").pack()
Entry(root_nome, textvariable=nome_artista).pack()

Label(root_nome).pack()

Button(root_nome, width=10, bg="blue", fg="white", text="Procurar", font=("Calibri", 11), command=busca_nome).pack()
Button(root_nome, width=10, bg="red", fg="white", text="Sair", font=("Calibri", 11), command=root_nome.destroy).pack()
Label(root_nome, textvariable=mensagem).pack()

root_nome.mainloop()