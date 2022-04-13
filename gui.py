from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
import domain

def tela_cadastro():
    root_cadastro = Tk()
    root_cadastro.title("Cadastrar Álbum")
    root_cadastro.geometry("400x400")

    nome_album = StringVar()
    ano = StringVar()
    nome_criador = StringVar()
    lancamento = IntVar()
    mensagem = StringVar()

    Label(root_cadastro, text="Nome do álbum: ", font=("Calibri")).place(x=10, y=40)
    Entry(root_cadastro, textvariable=nome_album).place(x=170, y=42)

    Label(root_cadastro, text="Criador do Álbum: ", font=("Calibri")).place(x=10, y=80)
    Entry(root_cadastro, textvariable=nome_criador).place(x=170, y=82)

    Label(root_cadastro, text="Ano de Lançamento: ", font=("Calibri")).place(x=10, y=120)
    Entry(root_cadastro, textvariable=ano).place(x=170, y=122)

    Label(root_cadastro, text="Álbum de lançamento?", font=("Calibri")).place(x=10, y=160)
    Radiobutton(root_cadastro, text="Sim", variable=lancamento, value=1).place(x=170, y=160)
    Radiobutton(root_cadastro, text="Não", variable=lancamento, value=0).place(x=230, y=160)

    Button(root_cadastro, width=10, bg="blue", fg="white", text="Cadastar álbum", font=("Calibri", 11),
    command=lambda:domain.registro(nome_album, ano, nome_criador, lancamento, mensagem)).place(x=140, y=240)   
        
    Button(root_cadastro, width=10, bg="red", fg="white", text="Sair", command=root_cadastro.destroy, font=("Calibri", 11)).place(x=140,  y=280)
                                                                                                            
    Label(root_cadastro, text="", textvariable=mensagem).place(x=140, y=320)

    root_cadastro.mainloop()



def tela_albuns():
    global root_albuns
    root_albuns = Tk()
    root_albuns.title("Álbuns Cadastrados")
    root_albuns.geometry("1000x250")

    arqv = open("album.txt", "r", encoding="utf-8")
    lista = [linha.split(',') for linha in arqv.readlines()]

    arvore = ttk.Treeview(root_albuns, columns=("lancamento", "album", "autor", "ano"), show="headings")
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

    root_albuns.mainloop()

def limpar():
   for i in arvore.get_children():
    arvore.delete(i)

def tela_nome():
    global root_nome
    root_nome = Tk()
    root_nome.title("Busca por Nome")
    root_nome.geometry("1000x500")

    nome_artista = StringVar()
    mensagem = StringVar()
    
    Label(root_nome, text="Insira o nome do artista/banda:").pack()
    Entry(root_nome, textvariable=nome_artista).pack()
    
    Label(root_nome).pack()

    Button(root_nome, width=10, bg="blue", fg="white", text="Procurar", font=("Calibri", 11),
    command=lambda: domain.busca_nome(nome_artista, mensagem, root_nome, tela_nomes_presentes)).pack()
    Button(root_nome, width=10, bg="blue", fg="white", text="Limpar", font=("Calibri", 11), command=limpar).pack()
    Button(root_nome, width=10, bg="red", fg="white", text="Sair", font=("Calibri", 11), command=root_nome.destroy).pack()
    Label(root_nome, textvariable=mensagem).pack()

    global arvore
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

    root_nome.mainloop()

def tela_nomes_presentes(l_nomes):

    for a,b,c,d in l_nomes:
        arvore.insert("", "end", values=(a,b,c,d))

def tela_ano():
    global root_ano, ttk, valor_rb, cb
    root_ano = Tk()
    root_ano.title("Busca por Ano")
    root_ano.geometry("1000x500")

    with open("album.txt", "r", encoding="utf-8") as arqv:
        lista_albuns = [linha.split(",") for linha in arqv]

    valor_rb = StringVar()
    anos = []

    for i in range(1950, 2023):
        anos.append(i)
        anos.sort(reverse=True)

    Label(root_ano).pack()
    Label(root_ano).pack()

    cb = Combobox(root_ano, values=anos)#combobox recebe os valores da lista anos(1950 até 2023) em ordem decrescente
    cb.set(anos[0])
    cb.pack()

    Label(root_ano).pack()

    Radiobutton(root_ano, text="Anterior a",  value="ant", variable=valor_rb).pack()
    Radiobutton(root_ano, text="Igual a",  value="igual", variable=valor_rb).pack()
    Radiobutton(root_ano, text="Posterior a",  value="post", variable=valor_rb).pack()
    Radiobutton

    Label(root_ano).pack()

    Button(root_ano, width=10, bg="blue", fg="white", text="Procurar", font=("Calibri", 11), 
    command=lambda: domain.busca_ano(lista_albuns, valor_rb, cb, tela_anos_presentes)).pack()
    Button(root_ano, width=10, bg="blue", fg="white", text="Limpar", font=("Calibri", 11), command=limpar).pack()
    Button(root_ano, width=10, bg="red", fg="white", text="Sair", font=("Calibri", 11), command=root_ano.quit).pack()
    Label(root_ano).pack()

    global arvore
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
    root_ano.mainloop()

def tela_anos_presentes(l_presente):

    for a,b,c,d in l_presente:
        arvore.insert("", "end", values=(a,b,c,d))
