planilha=[{"nome": "Nome", "categoria": "Categoria", "valor": "Valor"}]

transacao={}

def ler():
    global planilha
    try:
        with open("/home/vesf/Desktop/FP01/projeto_03/transacoes.csv", "r") as file:
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
    with open("/home/vesf/Desktop/FP01/projeto_03/transacoes.csv", "w+", encoding='utf-8') as file:
        for i, transacao in enumerate(planilha): 
            itens=[]
            for dados in transacao.values():
                itens.append(str(dados))
                linha = ",".join(itens)
            file.write(linha+"\n")

def adicao():
    print("***Adicionar nova transação***")
    with open("/home/vesf/Desktop/FP01/projeto_03/transacoes.csv", "w") as file:
        nome=str(input("Nome: ")).title() #Acho mais bonito quando inicia com maiúsculo kkk
        categoria=str(input("Categoria: ")).title()
        valor=float(input("Valor: R$"))
        transacao={"nome": nome, "categoria": categoria, "valor": valor}
        planilha.append(transacao)
        armazena()


def delete():
    print("***Apagar transação existente***")
    with open("/home/vesf/Desktop/FP01/projeto_03/transacoes.csv", "r") as file:
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
    # with open("/home/vesf/Desktop/FP01/projeto_02/transacoes.csv", "w") as file:
        # opcao = int(input('Digite a transação que deseja apagar: '))
        # planilha.pop(opcao)
        # armazena()

def extrato():
    tabela = []
    with open("/home/vesf/Desktop/FP01/projeto_03/transacoes.csv", "r+") as file:
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
                print(f"Valor: R${separar[2]}")



def atualizacao():
    global planilha
    extrato()
    ler()
    with open("/home/vesf/Desktop/FP01/projeto_03/transacoes.csv", "w") as file:
        nmr_transacao = int(input('Digite a transação que deseja atualizar: '))
    
        for i, v in enumerate(planilha):
            if nmr_transacao == i:
                opcao = input('Digite o que quer alterar: ').lower()
                if opcao in v.keys() and opcao == 'valor':
                    v[opcao] = float(input('Digite o valor atualizado: '))
                else:
                    v[opcao] = input('Digite o nome atualizado: ')
                armazena()
                break
            else:
                print('Digite uma transação válida.')