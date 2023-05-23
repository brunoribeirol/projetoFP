#CADA TRANSAÇÃO É UM DICIONARIO, DENTRO DE UMA LISTA DE TRASACOES
planilha=[{"nome": "uber", "categoria": "transporte", "valor": 30 }, {"nome": "racao", "categoria": "casa", "valor": 60,}]
#NOVA TRANSACAO (EX)
transacao={"nome": "uber", "categoria": "transporte", "valor": "input"}
#PRA ADICONAR NOVO, FAZ ALGO ASSIM
planilha.append(transacao)
planilha=[]
#######################funcao read
def ler():
    global planilha
    try:
        with open("/Users/vinicius/Documents/GitHub/projetoFP/petri.csv", "r") as file:
            linhas=file.readlines() #TODAS AS LINHAS VIRAM UM ITEM DE UMA LISTA
            for linha in linhas[1:]: #????  1 NAO PEGA O "TITULO" DO ARQUIVO
                itens=linha.strip().split(",") #ITENS = LISTA QUE TEM OS DADOS DE CADA TRANSAÇÃO
                transacao={"nome": itens[0], "categoria": itens[1], "valor": float(itens[2])} #PEGA CADA TRANSACAO E ADICIONA NO DICIONARIO
                planilha.append(transacao)
    except FileNotFoundError:
        pass #PESQUISAR SOBRE (BREAK SO FUNCIONA DENTRO DO WHILE, COMO É UMA FUNCAO QUE VAI SER CHAMADA NAS OUTRAS, NAO PRECISA DO WHILE)

    return planilha

def armazena(planilha): #TRANSFORMAR O DICIONARIO TRANSACAO EM UM STRING LINHA 
    with open("/Users/vinicius/Documents/GitHub/projetoFP/petri.csv", "w") as file:
        cabecalho=["Nome", "Categoria", "Valor"]
        titulos=",".join(cabecalho) #ARMAZENA O CABECALHO COMO STRING, SEPARADO POR VIRGULA
        file.write(titulos+"\n")

        
        for i, transacao in enumerate(planilha):
            itens=[]
            for dados in transacao.values():
                itens.append(str(dados))
                linha = ','.join(itens)
            file.write(linha+"\n")

        

'''
for linhas in file:
    transacoes_existentes=linhas.split(",") #TRANSACOES_EXISTENTE É UMA LISTA EM QUE CADA ITEM É UM ELEMENTO DA TRANSACAO
    indices.append(transacoes_existentes[0])
    nomes.append(transacoes_existentes[1])
    categorias.append(transacoes_existentes[2])
    valores.append(transacoes_existentes[3])
file.close()
'''
##############################funcao write

#############################funcao add
def adicao():
    ler()
    nome=input()
    categoria=input()
    valor=float(input())
    transacao={"nome": nome, "categoria": categoria, "valor": valor}
    transacoes.append(transacao)