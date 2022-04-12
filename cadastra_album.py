from tkinter import *

def cadastro():
    nome1 = nome_album.get()
    ano1 = ano.get()
    criador1 = nome_criador.get()
    lancamento1 = lancamento.get()

    if nome1 == "" or ano1 == "" or criador1 == "" or lancamento1 == "":
        mensagem.set("Preencha o(s) espaço(s) em branco")#set usado para não criar uma label para cada mensagem

    elif len(ano1) != 4:
          mensagem.set("Ano inválido!")

    else:#condicional para responder "álbum de lançamento?"
        with open("album.txt", "a", encoding="utf-8") as arqv: #context manager para assegurar que o arquivo sempre será fechado
            #jeito mais "pythonic" com operador  ternário
            arqv.write(f"Sim, {nome1}, {criador1}, {ano1}\n") if lancamento1 == 1 else arqv.write(f"Não, {nome1}, {criador1}, {ano1}\n")
        mensagem.set("Dados cadastrados com sucesso!")

root = Tk()
root.title("Cadastrar Álbum")
root.geometry("400x400")

nome_album = StringVar()
ano = StringVar()
nome_criador = StringVar()
lancamento = IntVar()#variável inteira porque os valores dos radiobuttons são 1 e 0
mensagem = StringVar()

Label(root, text="Nome do álbum: ", font=("Calibri")).place(x=10, y=40)
Entry(root, textvariable=nome_album).place(x=185, y=42)

Label(root, text="Criador do álbum: ", font=("Calibri")).place(x=10, y=80)
Entry(root, textvariable=nome_criador).place(x=185, y=82)

Label(root, text="Ano de lançamento: ", font=("Calibri")).place(x=10, y=120)
Entry(root, textvariable=ano).place(x=185, y=122)

Label(root, text="Álbum de lançamento?", font=("Calibri",)).place(x=10, y=160)
Radiobutton(root, text="Sim", variable=lancamento, value=1).place(x=200,y=160)
Radiobutton(root, text="Não", variable=lancamento, value=0).place(x=260, y=160)

Button(root, width=10, bg="blue", fg="white", text="Cadastar álbum", font=("Calibri", 11), command=cadastro).place(x=140,y=240)

Button(root, width=10, bg="red", fg="white", text="Sair", command=root.quit, font=("Calibri", 11)).place(x=140,y=280)

Label(root, text="", textvariable=mensagem).place(x=140,y=320)

root.mainloop()