#CREATE & DELETE

''''
REQUISITOS FUNCIONAIS:
    1. transações, que guardam (pelo menos) informações sobre o nome, uma categoria (exemplo: Casa, comida, transporte, etc...) 
    e a quantidade de dinheiro envolvida. Vale lembrar que o sistema deve rastrear entradas e saídas de dinheiro!
    2. Deve permitir o CRUD (Adição, leitura, atualização e deleção) de transações manualmente com a utilização de um menu.
        a. O programa deve também permitir leitura de transações filtradas por categoria.
    3. Deve guardar as informações adicionadas em um "banco de dados", para que estas persistam além da execução do programa. 
    Então, se o usuário rodar o programa uma vez, adicionar 2 transações e acabar a execução do programa, ao abrir o programa 
    novamente e listar as transações, as duas adicionadas anteriormente devem aparecer.
    4. Deve ser possível mostrar um extrato do sistema agrupando despesas por categoria.
    5. Ter pelo menos uma outra funcionalidade a mais que não está descrita aqui neste documento. Sejam criativos e divirtam-se!

REQUISITOS NÃO FUNCIONAIS:
    1. Deve ser feito em Python sem o uso de bibliotecas adicionais.
        a. Utilizar a linha de comando para entrada e saída;
    2. Os dados devem ser salvos em um arquivo no formato .csv Comma-separated values, valores separados por vírgulas)
        a. Perceba que o formato deste arquivo define que os valores estão separados por vírgula. Então, o que acontece quando 
        o usuário quiser adicionar um nome de uma transferência com vírgula?
    4. O código deve estar organizado, portanto, deve conter:
        a. Funções para dividir o código de forma lógica e evitar repetições;
        b. Tratamento de exceções, para garantir que seu código está pronto para tratar casos inesperados
        c. Legibilidade do código, incluindo nomeação de variáveis e funções.
    5. Deve ser feito um manual do usuário, explicando como utilizar a ferramenta e restrições gerais que a aplicação tenha.
        a. Fiquem à vontade para escolher como será feito esse manual. Pode ser um pdf, site, vídeo, carta...
'''


import os
os.system('clear')
indices=[0] ##INDICE 0 SÃO OS TÍTULOS DA COLUNA
nomes=["Nomes"]
categorias=["Categorias"]
valores=["Valores"]
menu_categoria={"indice": indices, 'nome': nomes, 'categoria': categorias, 'valor': valores}

##LER O ARQUIVO COM LAÇO FOR
file=open("/Users/vinicius/Documents/GitHub/projetoFP/petri.csv", "r", encoding="utf8")
for linhas in file:
    transacoes_existentes=linhas.split(",") #TRANSACOES_EXISTENTE É UMA LISTA EM QUE CADA ITEM É UM ELEMENTO DA TRANSACAO
    indices.append(transacoes_existentes[0])
    nomes.append(transacoes_existentes[1])
    categorias.append(transacoes_existentes[2])
    valores.append(transacoes_existentes[3])
file.close()


def det_indice(): ##DETERMINA O ÍNDICE DA PRÓXIMA LINHA
    return len(indices)
def pede_nome():
    return str(input('Nome: '))
def pede_categoria():
    return input('Categoria: ').title()
def pede_valor():
    return float(input('Valor: '))

def adicao(): ##FUNÇÃO 1 -> ADICIONA UMA TRANSAÇÃO NO FIM DO ARQUIVO
    indice_novo=det_indice()
    nome_novo = pede_nome()
    valor_novo = pede_valor()
    categoria_nova = pede_categoria()

    indices.append(indice_novo)  ##ADICIONA CADA ITEM DA TRANSAÇÃONAS LISTAS
    nomes.append(nome_novo)
    categorias.append(categoria_nova)
    valores.append(valor_novo)

    file=open("/Users/vinicius/Documents/GitHub/projetoFP/petri.csv", "w+") ##ESCREVE O ARQUIVO DE NOVO 
    for i in range (0, len(indices)):
        file.write(str(indices[i]) +","+ nomes[i] +","+ categorias[i] +","+ str(valores[i])+"\n") #TENTAR FAZER COM "a+" , sem for -> file.write(indice_novo +","+ nome_novo +","+ categoria_nova +","+ valor_novo+"\n")
    file.close() 

def apaga():
    file=open("/Users/vinicius/Documents/GitHub/projetoFP/petri.csv", "r", encoding="utf8")
    print("Digite o nome da transação que deseja apagar")
    nome_apagar = pede_nome()
    indice_apagar=nomes.index(nome_apagar)
    transacoes=file.readlines()
    for i in range(len(transacoes)):
        transacoes[i]=transacoes[i].split()
        if nome_apagar in transacoes[i]:
            indices.pop(indice_apagar)
            nomes.pop(indice_apagar)
            categorias.pop(indice_apagar)
            valores.pop(indice_apagar)
    file.close()
    file=open("/Users/vinicius/Documents/GitHub/projetoFP/petri.csv", "w+", encoding="utf8")
    for i in range (0, len(indices)):
        file.write(str(indices[i]) +","+ nomes[i] +","+ categorias[i] +","+ str(valores[i])+"\n")
    file.close()
    

'''
# Imprimir o cabeçalho da tabela
        #for categoria in categorias:
            #print('{:<20}'.format(categoria), end='')
        #print()

# Imprimir o separador entre o cabeçalho e as linhas de dados
    for _ in range(len(categorias)):
        print('-'*20, end='')
        print()
# 
# Imprimir as linhas de dados
        # for linha in transacoes.values():
            # print()
            # for coluna in range(len(categorias)):
                # print('{:<20}'.format(valores[coluna][linha]), end='')
        # print()
'''
def valida_faixa_inteiro(pergunta, inicio, fim):
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor <= fim:
                return valor
        except ValueError:
            print(f'Valor inválido, favor digitar entre {inicio} e {fim}')
# função novo criada
# colocar função para apagar a última função realizada, caso o usuário erre
# colocar função para ler uma categoria específica

os.system("clear")

def menu_funcao():
    print('''
    1 - Adicao
    2 - Atualização
    3 - Deleção
    4 - Leitura
    
    0 - Sai
    ''') 
    return valida_faixa_inteiro("Escolha uma opção: ", 0, 5)
while True:
    opcao = menu_funcao()
    if opcao == 0:
        break
    elif opcao == 1:
        adicao()
    elif opcao == 3:
        apaga()
    else:
        continue
