def registro(nome_album, ano, nome_criador, lancamento, mensagem):
    nome1 = nome_album.get()
    ano1 = ano.get()
    criador1 = nome_criador.get()
    lancamento1 = lancamento.get()

    if nome1 == "" or ano1 == "" or criador1 == "" or lancamento1 == "":
        pass
        mensagem.set("Preencha o(s) espaço(s) em branco")
    elif len(ano1) < 4 or len(ano1) > 4:
        pass
        mensagem.set("Ano inválido!")
    else:
        if lancamento1 == 1:
            with open("album.txt", "a", encoding="utf-8") as arqv:
                arqv.write(f"Sim, {nome1}, {criador1}, {ano1} \n")
        else:
            with open("album.txt", "a", encoding="utf-8") as arqv:
                arqv.write(f"Não, {nome1}, {criador1}, {ano1}\n")
        mensagem.set("Dados cadastrados com sucesso!")

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

            
       
