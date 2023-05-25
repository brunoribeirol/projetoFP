import os

planilha=[{"nome": "Nome", "categoria": "Categoria", "valor": "Valor"}]

transacao={}

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

print('\nSeja bem vindo ao Rastreador de Despesas Pessoais.')
path = input('Por favor, insira o caminho para o arquivo.csv criado.\n')

def ler():
    global planilha
    try:
        with open(path, "r") as file:
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
    with open(path, "w+", encoding='utf-8') as file:
        for i, transacao in enumerate(planilha): 
            itens=[]
            for dados in transacao.values():
                itens.append(str(dados))
                linha = ",".join(itens)
            file.write(linha+"\n")

def adicao():
    print("***Adicionar nova transação***")
    with open(path, "w") as file:
        while True:
            try:
                sinal = input("A transação foi receita ou gasto? [R] ou [G]\n").upper()
                if sinal != "G" and sinal != "R":
                    print("Opção inválida, tente novamente")
                    continue

                nome = str(input("Nome: ")).title()
                categoria = str(input("Categoria: ")).title()

                if sinal == "G":
                    valor = float("-" + input("Valor: R$"))
                else:
                    valor = float("+" + input("Valor: R$"))

                transacao = {"nome": nome, "categoria": categoria, "valor": valor}
                planilha.append(transacao)
                armazena()
                
            except ValueError as e:
                print("Erro:", str(e))
                print("Digite uma opção válida.")
            break

def delete():
    print("***Apagar transação existente***")
    with open(path, "r") as file:
        while True:
            try:
                opcao = int(input('Digite o número da transação que deseja apagar: '))
                if opcao < 0 or opcao >= len(planilha):
                    print("Transação não existe")
                    continue
            except ValueError:
                print("Digite um número válido.")
                continue
            except IndexError as e:
                print("Erro:", str(e))
                print("A transação não existe.")
            break
        for i in range(len(planilha)):
            if i == opcao:
                planilha.pop(opcao)
        armazena() 
                
def apagarTudo():
    print("***Limpar TODAS as transações***")
    with open(path, "r") as file:
        opcao = 1
        for i in range(1, len(planilha)+1, 1):
            if i != opcao:
                planilha.pop(opcao)
        armazena()  

def extrato():
    tabela = []
    with open(path, "r+") as file:
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

def transacoesCategoria():
    print("***Listar Transações por Categoria***")
    
    while True:
        try:
            categoria = input("Digite a categoria desejada: ").title()

            transacoes_encontradas = []
            for transacao in planilha:
                if transacao["categoria"] == categoria:
                    transacoes_encontradas.append(transacao)

            if transacoes_encontradas:
                print(f"\nTransações na categoria '{categoria}':")
                for i, transacao in enumerate(transacoes_encontradas, start=1):
                    print(f"\nTransação {i}:")
                    print(f"Nome: {transacao['nome']}")
                    print(f"Valor: R${transacao['valor']}")
                
                break  # Transações encontradas, sair do loop
            else:
                raise ValueError(f"Nenhuma transação encontrada na categoria '{categoria}'")
        except ValueError as e:
            print("Erro:", str(e))
            print("Digite uma categoria válida.\n")


def extratoCategoria():
    print("***Extrato de Despesas por Categoria***")
    
    while True:
        try:
            categoria = input("Digite a categoria desejada: ").title()

            total_despesas = 0
            for transacao in planilha:
                if transacao["categoria"] == categoria and transacao["valor"] < 0:
                    total_despesas += transacao["valor"]

            print(f"\nTotal de despesas na categoria '{categoria}': R${total_despesas:.2f}")
            
            break  # Saímos do loop se não ocorrerem erros
        except Exception as e:
            print("Ocorreu um erro:", str(e))
            print("Digite uma categoria válida.\n")


def atualizacao():
    global planilha
    extrato()
    
    while True:
        try:
            nmr_transacao = int(input("Digite o número da transação que deseja atualizar: ")) - 1
            if nmr_transacao < 0 or nmr_transacao >= len(planilha[1:]):
                print("Transação inválida.")
                return

            opcao = input("Digite o que quer alterar: ").lower()
            if opcao not in planilha[nmr_transacao + 1]:
                print("Opção inválida.")
                return

            if opcao == "valor":
                sinal=input("A transação foi receita ou gasto? [R] ou [G]\n").upper()
                if sinal != "G" and sinal != "R":
                    print("Opção inválida, tente novamente")
                if sinal=="G":
                    novo_valor=float("-"+input("Digite novo valor: R$"))
                elif sinal == 'R':
                    novo_valor=float("+"+input("Digite novo valor: R$"))
                planilha[nmr_transacao + 1][opcao] = novo_valor
                print("Transação atualizada.")
                armazena()
                break
            else:
                novo_valor = input("Digite a atualização: ").title()
                planilha[nmr_transacao + 1][opcao] = novo_valor
                print("Transação atualizada.")
                armazena()
                break
        except ValueError:
            print("Opção inválida, tente novamente.")


def calculandoSaldo():
    saldo = 0
    for transacao in planilha:
        preco = transacao.get("valor") #"valor" é a key
        if preco!= "Valor": #value do cabecalho para key "valor" é "Valor"
            saldo += float(preco)

    # Verificar se o saldo é maior ou igual a 0 e retornar com cor correspondente
    if saldo >= 0:
        saldoFinal = "\033[92mR${:.2f}\033[0m".format(saldo)  # Verde
    else:
        saldoFinal = "\033[91mR${:.2f}\033[0m".format(saldo)  # Vermelho

    return saldoFinal



planilha = ler() #NAO ZERA A PLANILHA QUANDO VC ENCERRA O PROGRAMA E INICIA DE NOVO


# Criando um def para menu para não ficar muitas linhas de código no loop principal
def menu():
    print("\033[0m")

    print("\033[1;3m--------------------------------")
    print("\033[1;3m         MENU PRINCIPAL")
    print("\033[1;3m--------------------------------")

    print("\033[0;34m 1. Adicionar Transação")
    print("\033[0;35m 2. Listar Todas as Transações")
    print("\033[0;30m 3. Listar Transações por Categoria")
    print("\033[0;91m 4. Extrato por Categoria")
    print("\033[0;36m 5. Atualização de uma Transação")
    print("\033[0;37m 6. Apagar uma Transação")
    print("\033[0;33m 7. Apagar TODAS as Transações")
    print("\033[0;32m 8. Ver Saldo Atual")
    print("\033[0;31m 9. Sair do Programa")
    print("\033[0m")


while True:
    clear_screen()

    menu()

    acao = input("\033[1m\nEscolha uma opção: ")

    if acao == "1":
        adicao()
        input("\033[0;30m\nPressione Enter para continuar...")

    elif acao == "2":
        extrato()
        input("\033[0;30m\nPressione Enter para continuar...")

    elif acao == "3":
        transacoesCategoria()
        input("\033[0;30m\nPressione Enter para continuar...")

    elif acao == "4":
        extratoCategoria()
        input("\033[0;30m\nPressione Enter para continuar...")

    elif acao == "5":
        atualizacao()
        input("\033[0;30m\nPressione Enter para continuar...")

    elif acao == "6":
        extrato()
        delete()
        input("\033[0;30m\nPressione Enter para continuar...")

    elif acao == "7":
        zerar = input("\nVocê tem CERTEZA que deseja apagar TUDO? [S] ou [N]\n").upper()
        if zerar == "S":
            apagarTudo()
        elif zerar == "N":
            continue
        else:
            print("\033[91mOpção inválida. Por favor, tente novamente.")

        input("\033[0;30m\nPressione Enter para continuar...")

    elif acao == "8":
        print(f"Saldo Atual: {calculandoSaldo()}")
        input("\033[0;30m\nPressione Enter para continuar...")

    elif acao == "9":
        print("\033[1m\nObrigado por utilizar o nosso Sistema de Controle Financeiro!")
        break

    else:
        print("\033[91mOpção inválida. Por favor, tente novamente.")
        input("\033[0;30m\nPressione Enter para continuar...")