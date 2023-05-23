#CADA TRANSAÇÃO É UM DICIONARIO, DENTRO DE UMA LISTA DE TRASACOES
transacoes=[{"nome": "uber", "categoria": "transporte", "valor": 30 }, {"nome": "racao", "categoria": "casa", "valor": 60,}]
#NOVA TRANSACAO (EX)
transacao={"nome": "input", "categoria": "input", "valor": "input"}
#PRA ADICONAR NOVO, FAZ ALGO ASSIM
transacoes.append(transacao)

#######################funcao read
def lerArquivo():
    file=open("/Users/vinicius/Documents/GitHub/projetoFP/petri.csv", "r", encoding="utf8")
    linhas=file.readlines().split()
    transacao={"nome":}

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
def escrever():
    file=open("/Users/vinicius/Documents/GitHub/projetoFP/petri.csv", "w+", encoding="utf8")
    transacoes=[]
    for i in transacoes:
        file.write(i)
#############################funcao add
def adicao():
    lerArquivo()
    nome=input()
    categoria=input()
    valor=float(input())
    transacao={"nome": nome, "categoria": categoria, "valor": valor}
    transacoes.append(transacao)
