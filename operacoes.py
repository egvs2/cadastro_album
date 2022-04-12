import interface as inter


def registro(nome_album, ano, nome_criador, lancamento):
    nome1 = nome_album.get()
    ano1 = ano.get()
    criador1 = nome_criador.get()
    lancamento1 = lancamento.get()

    if nome1 == "" or ano1 == "" or criador1 == "" or lancamento1 == "":
        pass
        inter.mensagem.set("Preencha o(s) espaço(s) em branco")
    elif len(ano1) < 4 or len(ano1) > 4:
        pass
        inter.mensagem.set("Ano inválido!")
    else:
        if lancamento1 == 1:
            with open("album.txt", "a", encoding="utf-8") as arqv:
                arqv.write(f"Sim, {nome1}, {criador1}, {ano1} \n")
        else:
            with open("album.txt", "a", encoding="utf-8") as arqv:
                arqv.write(f"Não, {nome1}, {criador1}, {ano1}\n")
        inter.mensagem.set("Dados cadastrados com sucesso!")
