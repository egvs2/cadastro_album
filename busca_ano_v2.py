from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox



def funcao():
    cb1 = int(cb.get())
    valor_rb1 = valor_rb.get()
    l = []
    
    if valor_rb1 == "ant":
        for i in lista_albuns:
            if int(i[3]) <= cb1:
                l.append(i)
        l.sort(key = lambda l:l[3])
 
    elif valor_rb1 == "igual":
        for i in lista_albuns:
            if int(i[3]) == cb1:
                l.append(i)
        l.sort(key = lambda l:l[3])    

    elif valor_rb1 == "post":
        for i in lista_albuns:
            if int(i[3]) >= cb1:
                l.append(i)
        l.sort(key = lambda l:l[3])
            
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

    for a,b,c,d in l:
        arvore.insert("", "end", values=(a,b,c,d))

root = Tk()
root.title("Busca por Ano")
root.geometry("1000x500")

arqv = open("album.txt", "r")

lista_albuns = [linha.split(',') for linha in arqv.readlines()]

valor_rb = StringVar()
anos = []


for i in range(2000, 2023):
    anos.append(i)
    anos.sort(reverse=True)

Label(root).pack()
Label(root).pack()


cb = Combobox(root, values=anos)
cb.set(anos[0])
cb.pack()

Label(root).pack()

Radiobutton(root, text="Anterior a",  value="ant", variable=valor_rb).pack()

Radiobutton(root, text="Igual a",  value="igual", variable=valor_rb).pack()

Radiobutton(root, text="Posterior a",  value="post", variable=valor_rb).pack()

Label(root).pack()


Button(root, width=10, bg="blue", fg="white", text="Procurar", font=("Calibri", 11), command=funcao).pack()
Button(root, width=10, bg="red", fg="white", text="Sair", font=("Calibri", 11), command=root.quit).pack()



root.mainloop()
