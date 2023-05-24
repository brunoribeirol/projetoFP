#READ & UPDATE
planilha=[{"nome": "Nome", "categoria": "Categoria", "valor": "Valor"}]

transacao={}
#path=input()
def ler():
    global planilha
    try:
        with open("/Users/vinicius/Documents/GitHub/projetoFP/petri.csv", "r") as file:
            linhas=file.readlines() 
            for linha in linhas[1:]: 
                itens=linha.strip().split(",") 
                transacao={"nome": itens[0], "categoria": itens[1], "valor": float(itens[2])} 
                planilha.append(transacao)
    except FileNotFoundError:
        pass 

    return planilha


def armazena():
    global planilha
    with open("/Users/vinicius/Documents/GitHub/projetoFP/petri.csv", "w+", encoding='utf-8') as file:
        for i, transacao in enumerate(planilha): 
            itens=[]
            for dados in transacao.values():
                itens.append(str(dados))
                linha = ",".join(itens)
            file.write(linha+"\n")

def adicao():
    print("***Adicionar nova transação***")
    with open("/Users/vinicius/Documents/GitHub/projetoFP/petri.csv", "w") as file:
        nome=str(input("Nome: ")).title() #Acho mais bonito quando inicia com maiúsculo kkk
        categoria=str(input("Categoria: ")).title()
        valor=str(input("Valor: R$"))
        transacao={"nome": nome, "categoria": categoria, "valor": valor}
        planilha.append(transacao)
        armazena()


def delete():
    print("***Apagar transação existente***")
    with open("/Users/vinicius/Documents/GitHub/projetoFP/petri.csv", "r") as file:
        nome=str(input("Nome: ")).title() #Acho mais bonito quando inicia com maiúsculo kkk
        categoria=str(input("Categoria: ")).title()
        valor=float(input("Valor: R$"))
        transacao_pra_achar={"nome": nome, "categoria": categoria, "valor": valor}
        ler()
        planilha.remove(transacao_pra_achar)
        armazena()
        ############# OUTRA OPÇÃO PRA DELETAR PELO ÍNDICE ############
    # global planilha
    # extrato()
    # ler()
    # with open("/Users/vinicius/Documents/GitHub/projetoFP/petri.csv", "w") as file:
        # opcao = int(input('Digite a transação que deseja apagar: '))
        # planilha.pop(opcao)
        # armazena()

def extrato():
    tabela = []
    with open("/Users/vinicius/Documents/GitHub/projetoFP/petri.csv", "r+") as file:
        for linha in file.readlines():
            tabela.append(linha)
        for i, v in enumerate(tabela):
            separar = v.split(',')
            
            if i == 0: 
                continue
            else:                
                print(f"\nTransação {i}:")
                print(f"Nome: {separar[0]}")
                print(f"Categoria: {separar[1]}")
                print(f"Quantidade de Dinheiro: R${separar[2]}")



def atualizacao():
    global planilha
    extrato()
    ler()
    with open("/Users/vinicius/Documents/GitHub/projetoFP/petri.csv", "w") as file:
        nmr_transacao = int(input('Digite a transação que deseja atualizar: '))
        for i, v in enumerate(planilha):
            if nmr_transacao == i:
                opcao = input('Digite o que quer alterar: ')
                if opcao in v.keys():
                    v.update({opcao: input('Digite a atualização: ')})
                armazena()
                
######## QUANDO UMA FUNCAO USANDO WITH OPEN FECHA POR ERRO, APAGA OS DADOS DO ARQUIVO.CSV ###########


while True:
    
    option=int(input("\ninforme a opcao desejada: \n[1]-adição\n[2]-remoção\n[3]-extrato\n[4]-atualização\n-->"))

    if option==1:
        adicao()
        armazena()
        print("Transação adicionada.")

    elif option==2:
        delete()
        armazena()
        print("Transação removida.")
    elif option==3:
        extrato()
    elif option==4:
        atualizacao()