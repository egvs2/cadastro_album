from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox

def busca_ano(lista_albuns, valor_rb, cb, ttk, root_ano):
    cb1 = int(cb.get())
    valor_rb1 = valor_rb.get()
    l_presente = []
    
    if valor_rb1 == "ant":
        for i in lista_albuns:#percorre elementos da lista de albuns,
            if int(i[3]) <= cb1:#verifica se o ano(int) da lista de álbuns é menor ou igual ao ano escolhido na combobox
                l_presente.append(i)#se sim, adiciona todos os elementos da l_albuns para lista_presente
        l_presente.sort(key = lambda l:l[3])#lambda para ordenar pelo index que armazena os anos  
 
    elif valor_rb1 == "igual":
        for i in lista_albuns:
            if int(i[3]) == cb1:
                l_presente.append(i)
        l_presente.sort(key = lambda l:l[3])    

    elif valor_rb1 == "post":
        for i in lista_albuns:
            if int(i[3]) >= cb1:
                l_presente.append(i)
        l_presente.sort(key = lambda l:l[3])
            
    arvore = ttk.Treeview(root_ano, columns=("lancamento", "album", "autor", "ano"), show="headings")
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

    for a,b,c,d in l_presente:
        arvore.insert("", "end", values=(a,b,c,d))


root = Tk()
root.title("Busca por Ano")
root.geometry("1000x500")

with open("album.txt", "r") as arqv:
    lista_albuns = [linha.split(",") for linha in arqv]

valor_rb = StringVar()
anos = []

for i in range(1950, 2023):
    anos.append(i)
    anos.sort(reverse=True)

Label(root).pack()
Label(root).pack()

cb = Combobox(root, values=anos)#combobox recebe os valores da lista anos(1950 até 2023) em ordem decrescente
cb.set(anos[0])
cb.pack()

Label(root).pack()

Radiobutton(root, text="Anterior a",  value="ant", variable=valor_rb).pack()
Radiobutton(root, text="Igual a",  value="igual", variable=valor_rb).pack()
Radiobutton(root, text="Posterior a",  value="post", variable=valor_rb).pack()

Label(root).pack()

Button(root, width=10, bg="blue", fg="white", text="Procurar", font=("Calibri", 11), command=busca_ano).pack()
Button(root, width=10, bg="red", fg="white", text="Sair", font=("Calibri", 11), command=root.quit).pack()

root.mainloop()