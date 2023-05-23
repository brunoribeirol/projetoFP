planilha = [{'nome': 'uber', 'valor': 30, 'categoria': 'transporte'},
              {'nome': 'racao', 'valor': 60, 'categoria': 'casa'}]

transacao = {'nome': 'input', 'categoria': 'input', 'valor': 'input'}

def ler():
    global planilha
    try:
        with open('./projeto_02/transacoes.csv', 'r') as file:
            linhas=file.readlines() #TODAS AS LINHAS VIRAM UM ITEM DE UMA LISTA
            for linha in linhas[1:]: #????  1 NAO PEGA O "TITULO" DO ARQUIVO
                itens=linha.strip().split(",") #ITENS = LISTA QUE TEM OS DADOS DE CADA TRANSAÇÃO
                transacao={"nome": itens[0], "categoria": itens[1], "valor": float(itens[2])} #PEGA CADA TRANSACAO E ADICIONA NO DICIONARIO
                planilha.append(transacao)
    except FileNotFoundError:
        pass #PESQUISAR SOBRE (BREAK SO FUNCIONA DENTRO DO WHILE, COMO É UMA FUNCAO QUE VAI SER CHAMADA NAS OUTRAS, NAO PRECISA DO WHILE)

    return planilha

def armazena(planilha): #TRANSFORMAR O DICIONARIO TRANSACAO EM UM STRING LINHA 
    with open('./projeto_02/transacoes.csv', 'w') as file:
        cabecalho=["Nome", "Categoria", "Valor"]
        titulos=",".join(cabecalho) #ARMAZENA O CABECALHO COMO STRING, SEPARADO POR VIRGULA
        file.write(titulos+"\n")

        
        for i, transacao in enumerate(planilha):
            itens=[]
            for dados in transacao.values():
                itens.append(str(dados))
                linha = ','.join(itens)
            file.write(linha+"\n")

armazena(planilha)