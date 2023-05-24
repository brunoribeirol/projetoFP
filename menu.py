# Menu - OK
# Método Sleep ou Clear - +-
# Cor - OK
# Saldo - +-
# Funcionalidade Extra - FALTA
# READ.me - FALTA

import os


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


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
