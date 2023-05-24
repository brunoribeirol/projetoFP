# Menu - OK
# Método Sleep ou Clear - +-
# Cor - OK
# Saldo - +-
# Funcionalidade Extra - FALTA
# READ.me - FALTA


# ***********************LEMBRAR DE MUDAR OS PATHS
# CADA TRANSAÇÃO É UM DICIONARIO, DENTRO DE UMA LISTA DE TRASACOES
planilha = [{"nome": "Nome", "categoria": "Categoria", "valor": "Valor"}]
# NOVA TRANSACAO (EX)
transacao = {}

import os


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


#######################funcao read
def ler():
    global planilha
    try:
        with open(
            "/Users/brunoribeiro/Documents/GitHub/projetoFP/transacoes.csv", "r"
        ) as file:
            linhas = file.readlines()  # TODAS AS LINHAS VIRAM UM ITEM DE UMA LISTA
            for linha in linhas[1:]:  # ????  1 NAO PEGA O "TITULO" DO ARQUIVO
                itens = linha.strip().split(
                    ","
                )  # ITENS = LISTA QUE TEM OS DADOS DE CADA TRANSAÇÃO
                transacao = {
                    "nome": itens[0],
                    "categoria": itens[1],
                    "valor": float(itens[2]),
                }  # PEGA CADA TRANSACAO E ADICIONA NO DICIONARIO
                planilha.append(transacao)
    except FileNotFoundError:
        pass  # PESQUISAR SOBRE (BREAK SO FUNCIONA DENTRO DO WHILE, COMO É UMA FUNCAO QUE VAI SER CHAMADA NAS OUTRAS, NAO PRECISA DO WHILE)

    return planilha


##############################funcao write
def armazena():  # TRANSFORMAR O DICIONARIO TRANSACAO EM UM STRING LINHA
    with open(
        "/Users/brunoribeiro/Documents/GitHub/projetoFP/transacoes.csv",
        "w+",
        encoding="utf-8",
    ) as file:
        for i, transacao in enumerate(planilha):  # i é idice, nao usei
            itens = []
            for dados in transacao.values():
                itens.append(str(dados))
                linha = ",".join(itens)
            file.write(linha + "\n")


#############################funcao add
def adicao():
    print("***Adicionar nova transação***")
    with open(
        "//Users/brunoribeiro/Documents/GitHub/projetoFP/transacoes.csv", "w"
    ) as file:
        nome = str(input("Nome: "))
        categoria = str(input("Categoria: ")).title()
        valor = str(input("Valor: R$"))
        transacao = {"nome": nome, "categoria": categoria, "valor": valor}
        planilha.append(transacao)
        armazena()


#############################funcao delete
def delete():
    print("***Apagar transação existente***")
    with open(
        "/Users/brunoribeiro/Documents/GitHub/projetoFP/transacoes.csv", "r"
    ) as file:
        nome = str(input("Nome: "))
        categoria = str(input("Categoria: ")).title()
        valor = float(input("Valor: R$"))
        transacao_pra_achar = {"nome": nome, "categoria": categoria, "valor": valor}
        ler()
        planilha.remove(transacao_pra_achar)
        armazena()


# USAR ISSO PARA O CÓDIGO FINAL


# Função criada para calcular o saldo do usuário
def calculandoSaldo():
    saldo = 0
    for transacao in planilha:
        preco = transacao.get("valor")  # ???
        if preco:
            saldo += float(preco)  # ??????

    # Verificando se o saldo é positivo ou negativo (maior ou menor que zero), e dependendo se ele for positivo ou negativo irá retornar uma cor diferente
    if saldo >= 0:
        saldoFinal = "\033[92mR${:.2f}\033[0m".format(saldo)  # Verde
    else:
        saldoFinal = "\033[91mR${:.2f}\033[0m".format(saldo)  # Vermelho

    return saldoFinal


# Criação da funcionalidade que deleta tudo que tem no arquivo .csv
"""
def apagaTudo():
"""


# Carregar as transações existentes
planilha = ler()
# transactions = read_transactions() #TA ERRADO ler()


# Criação da função menu para diminuir o bloco de código no loop principal
def menu():
    print("\033[1;3m--------------------------------")
    print("\033[1;3m         MENU PRINCIPAL")
    print("\033[1;3m--------------------------------")

    print("\033[0;34m 1. Adicionar Transação")
    print("\033[0;35m 2. Listar Todas as Transações")
    print("\033[0;36m 3. Listar Transações por Categoria")
    print("\033[0;37m 4. Extrato de Despesas por Categoria")
    print("\033[0;33m 5. Remover Transação")
    print("\033[0;34m 6. Ver Saldo Atual")
    print("\033[0;31m 7. Sair do Programa")
    print("\033[0m")


while True:
    clear_screen()

    menu()

    acao = input("\nEscolha uma opção: ")

    if acao == "1":
        # ler() Talvez não precise de nenhum desse ler() !!!!!!!!!!!!!!!!
        adicao()
        input("\nPressione Enter para continuar...")

    elif acao == "4":
        # ler() Talvez não precise de nenhum desse ler() !!!!!!!!!!!!!!!!
        delete()
        # list_all_transactions(transactions)
        input("\nPressione Enter para continuar...")

    elif acao == "6":
        # ler() Talvez não precise de nenhum desse ler() !!!!!!!!!!!!!!!!
        print(f"Saldo Atual: {calculandoSaldo()}")
        input("\nPressione Enter para continuar...")

    elif acao == "7":
        print("Obrigado por utilizar o Sistema de Controle Financeiro!")
        break

    else:
        print("Opção inválida. Por favor, tente novamente.")
        input("\nPressione Enter para continuar...")


"""
    elif acao == "2":
        # ler() Talvez não precise de nenhum desse ler() !!!!!!!!!!!!!!!!
        extrato()
        # list_all_transactions(transactions) VER ESSA
        input("\nPressione Enter para continuar...")
    
    elif acao == "3":
        # ler() Talvez não precise de nenhum desse ler() !!!!!!!!!!!!!!!!
        atualizacao()
        # list_all_transactions(transactions)
        input("\nPressione Enter para continuar...")


        
    elif acao == "5":
        # ler() Talvez não precise de nenhum desse ler() !!!!!!!!!!!!!!!!
        apagarTudo()
        # FALTA VER QUAL EXTRA VOU COLOCAR
        input("\nPressione Enter para continuar...")
"""


"""
for transacao in planilha:
    for i in transacao.keys():
        del transacao[i]
"""
