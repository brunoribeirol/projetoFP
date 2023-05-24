import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
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

    acao = input("\nEscolha uma opção: ")

    if acao == "1":
        # ler() Talvez não precise de nenhum desse ler() !!!!!!!!!!!!!!!!
        # adicao()
        input("\nPressione Enter para continuar...")

    elif acao == "2":
        # ler() Talvez não precise de nenhum desse ler() !!!!!!!!!!!!!!!!
        # extrato()
        # list_all_transactions(transactions) VER ESSA
        input("\nPressione Enter para continuar...")

    elif acao == "3":
        # ler() Talvez não precise de nenhum desse ler() !!!!!!!!!!!!!!!!
        # atualizacao()
        # list_all_transactions(transactions)
        input("\nPressione Enter para continuar...")

    elif acao == "4":
        # ler() Talvez não precise de nenhum desse ler() !!!!!!!!!!!!!!!!
        # delete()
        # list_all_transactions(transactions)
        input("\nPressione Enter para continuar...")

    elif acao == "5":
        # ler() Talvez não precise de nenhum desse ler() !!!!!!!!!!!!!!!!
        # apagarTudo()
        # FALTA VER QUAL EXTRA VOU COLOCAR
        input("\nPressione Enter para continuar...")
    
    elif acao == "6":
        # ler() Talvez não precise de nenhum desse ler() !!!!!!!!!!!!!!!!
        # print(f"Saldo Atual: {calculandoSaldo()}")
        input("\nPressione Enter para continuar...")

    elif acao == "7":
        print("Obrigado por utilizar o Sistema de Controle Financeiro!")
        break

    else:
        print("Opção inválida. Por favor, tente novamente.")
        input("\nPressione Enter para continuar...")
