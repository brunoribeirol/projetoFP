import os

planilha=[{"nome": "Nome", "categoria": "Categoria", "valor": "Valor"}]

transacao={}


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

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


# USAR ISSO PARA O CÓDIGO FINAL
def calculandoSaldo():
    saldo = 0
    for transacao in planilha:
        preco = transacao.get("valor")  # ???
        if preco:
            saldo += float(preco)  # ??????

    # Verificar se o saldo é maior ou igual a 0 e retornar com cor correspondente
    if saldo >= 0:
        saldoFinal = "\033[92mR${:.2f}\033[0m".format(saldo)  # Verde
    else:
        saldoFinal = "\033[91mR${:.2f}\033[0m".format(saldo)  # Vermelho

    return saldoFinal


# Carregar as transações existentes
planilha = ler()
# transactions = read_transactions() #TA ERRADO ler()


                                        #FALTA A FUNCAO APAGR TUDO!!!!!!!!


# Criando um def para menu para não ficar muitas linhas de código no loop principal
def menu():
    print("\033[0m")

    print("\033[1;3m--------------------------------")
    print("\033[1;3m         MENU PRINCIPAL")
    print("\033[1;3m--------------------------------")

    print("\033[0;34m 1. Adicionar Transação")
    print("\033[0;35m 2. Listar Todas as Transações")
    print("\033[0;36m 3. Atualização de uma Transação")
    print("\033[0;37m 4. Apagar uma Transação")
    print("\033[0;33m 5. Apagar TODAS as Transações")
    print("\033[0;34m 6. Ver Saldo Atual")
    print("\033[0;31m 7. Sair do Programa")
    print("\033[0m")


while True:
    clear_screen()

    menu()

    acao = input("\033[1m\nEscolha uma opção: ")

    if acao == "1":
        # ler() Talvez não precise de nenhum desse ler() !!!!!!!!!!!!!!!!
        adicao()
        input("\033[0;30m\nPressione Enter para continuar...")

    elif acao == "2":
        # ler() Talvez não precise de nenhum desse ler() !!!!!!!!!!!!!!!!
        extrato()
        # list_all_transactions(transactions) VER SE PRECISA DISSO
        input("\033[0;30m\nPressione Enter para continuar...")

    elif acao == "3":
        # ler() Talvez não precise de nenhum desse ler() !!!!!!!!!!!!!!!!
        atualizacao()
        # list_all_transactions(transactions) VER SE PRECISA DISSO
        input("\033[0;30m\nPressione Enter para continuar...")

    elif acao == "4":
        # ler() Talvez não precise de nenhum desse ler() !!!!!!!!!!!!!!!!
        delete()
        # list_all_transactions(transactions) VER SE PRECISA DISSO
        input("\033[0;30m\nPressione Enter para continuar...")
    
    elif acao == "6":
        # ler() Talvez não precise de nenhum desse ler() !!!!!!!!!!!!!!!!
        print(f"Saldo Atual: {calculandoSaldo()}")
        input("\033[0;30m\nPressione Enter para continuar...")

    elif acao == "7":
        print("\033[1m\nObrigado por utilizar o nosso Sistema de Controle Financeiro!")
        break

    else:
        print("\033[91mOpção inválida. Por favor, tente novamente.")
        input("\033[0;30m\nPressione Enter para continuar...")

    '''
    elif acao == "5":
        # ler() Talvez não precise de nenhum desse ler() !!!!!!!!!!!!!!!!
        zerar = input("\nVocê tem CERTEZA que deseja apagar TUDO? [S] ou [N]\n")
        if zerar == "S" or zerar == "s":
            apagarTudo()
        elif zerar == "N" or zerar == "n":
            continue
        else:
            print("\033[91mOpção inválida. Por favor, tente novamente.")

        input("\033[0;30m\nPressione Enter para continuar...")
    '''

    
        