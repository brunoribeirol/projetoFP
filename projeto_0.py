#***********************LEMBRAR DE MUDAR OS PATHS
#CADA TRANSAÇÃO É UM DICIONARIO, DENTRO DE UMA LISTA DE TRASACOES
planilha=[{"nome": "Nome", "categoria": "Categoria", "valor": "Valor"}]
#NOVA TRANSACAO (EX)
transacao={}

#######################funcao read
def ler():
    global planilha
    try:
        with open("/Users/vinicius/Desktop/CESAR/fund. programação/listas de exercício/PROJETINHU/bancodedados.csv", "r") as file:
            linhas=file.readlines() #TODAS AS LINHAS VIRAM UM ITEM DE UMA LISTA
            for linha in linhas[1:]: #????  1 NAO PEGA O "TITULO" DO ARQUIVO
                itens=linha.strip().split(",") #ITENS = LISTA QUE TEM OS DADOS DE CADA TRANSAÇÃO
                transacao={"nome": itens[0], "categoria": itens[1], "valor": float(itens[2])} #PEGA CADA TRANSACAO E ADICIONA NO DICIONARIO
                planilha.append(transacao)
    except FileNotFoundError:
        pass #PESQUISAR SOBRE (BREAK SO FUNCIONA DENTRO DO WHILE, COMO É UMA FUNCAO QUE VAI SER CHAMADA NAS OUTRAS, NAO PRECISA DO WHILE)

    return planilha

##############################funcao write
def armazena(): #TRANSFORMAR O DICIONARIO TRANSACAO EM UM STRING LINHA 
    with open("/Users/vinicius/Desktop/CESAR/fund. programação/listas de exercício/PROJETINHU/bancodedados.csv", "w+", encoding='utf-8') as file:
        for i, transacao in enumerate(planilha): #i é idice, nao usei
            itens=[]
            for dados in transacao.values():
                itens.append(str(dados))
                linha = ",".join(itens)
            file.write(linha+"\n")

#############################funcao add
def adicao():
    print("***Adicionar nova transação***")
    with open("/Users/vinicius/Desktop/CESAR/fund. programação/listas de exercício/PROJETINHU/bancodedados.csv", "w") as file:
        nome=str(input("Nome: "))
        categoria=str(input("Categoria: ")).title()
        valor=str(input("Valor: R$"))
        transacao={"nome": nome, "categoria": categoria, "valor": valor}
        planilha.append(transacao)
        armazena()

#############################funcao delete
def delete():
    print("***Apagar transação existente***")
    with open("/Users/vinicius/Desktop/CESAR/fund. programação/listas de exercício/PROJETINHU/bancodedados.csv", "r") as file:
        nome=str(input("Nome: "))
        categoria=str(input("Categoria: ")).title()
        valor=float(input("Valor: R$"))
        transacao_pra_achar={"nome": nome, "categoria": categoria, "valor": valor}
        ler()
        planilha.remove(transacao_pra_achar)
        armazena()

###########menu prototipo
option=int(input("\ninforme a opcao desejada: \n[1]-adição\n[2]-remoção\n"))
if option==1:
    ler()
    adicao()
    print("Transação adicionada.")

elif option==2:
    delete()
    print("Transação removida.")