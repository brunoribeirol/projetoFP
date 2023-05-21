''''
REQUISITOS FUNCIONAIS:
    1. O sistema deve ser baseado em transações, que guardam (pelo menos) informações sobre o nome, uma categoria (exemplo: Casa, comida, transporte, etc...) e a quantidade de dinheiro envolvida. Vale lembrar que o sistema deve rastrear entradas e saídas de dinheiro!
    2. Deve permitir o CRUD (Adição, leitura, atualização e deleção) de transações manualmente com a utilização de um menu.
        a. O programa deve também permitir leitura de transações filtradas por categoria.
    3. Deve guardar as informações adicionadas em um "banco de dados", para que estas persistam além da execução do programa. Então, se o usuário rodar o programa uma vez, adicionar 2 transações e acabar a execução do programa, ao abrir o programa novamente e listar as transações, as duas adicionadas anteriormente devem aparecer.
    4. Deve ser possível mostrar um extrato do sistema agrupando despesas por categoria.
    5. Ter pelo menos uma outra funcionalidade a mais que não está descrita aqui neste documento. Sejam criativos e divirtam-se!

REQUISITOS NÃO FUNCIONAIS:
    1. Deve ser feito em Python sem o uso de bibliotecas adicionais.
        a. Utilizar a linha de comando para entrada e saída;
        b. Exceções de bibliotecas:
            ■ os -> os.system("clear") ou “cls”
    2. Os dados devem ser salvos em um arquivo no formato .csv Comma-separated values, valores separados por vírgulas)
        a. Perceba que o formato deste arquivo define que os valores estão separados por vírgula. Então, o que acontece quando o usuário quiser adicionar um nome de uma transferência com vírgula?
    4. O código deve estar organizado, portanto, deve conter:
        a. Funções para dividir o código de forma lógica e evitar repetições;
        b. Tratamento de exceções, para garantir que seu código está pronto para tratar casos inesperados
        c. Legibilidade do código, incluindo nomeação de variáveis e funções.
    5. Deve ser feito um manual do usuário, explicando como utilizar a ferramenta e restrições gerais que a aplicação tenha.
        a. Fiquem à vontade para escolher como será feito esse manual. Pode ser um pdf, site, vídeo, carta...
'''

import os
os.system('clear')

print("Olá Natália! Seja bem-vinda ao seu rastreador de despesas pessoais.\n")

transacoes = {'Casa': 0,
              'Comida': 0,
              'Transporte': 0,
              'Salário': 0}

def pede_categoria():
    return input('Categoria: ').title()
def pede_valor():
    return input('Valor: ') 
def pede_nome_arquivo():
    return input('Nome do arquivo: ') #Precisamos pensar em uma forma mais fácil para o usuário
def novo():
    global transacoes
    opcao = input('Desja inserir nova\n[c]ategoria\n[v]alor:\n-->').lower()
    if opcao == 'v':
        valor = pede_valor()
        categoria = pede_categoria()
        transacoes[categoria] += float(valor)
    elif opcao == 'c':
        nova_categoria = pede_categoria()
        transacoes[nova_categoria] = pede_valor()
    else: 
        print('Digite uma opção válida: ')

def grava():
    nome_arquivo = pede_nome_arquivo()
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        for categoria, total in transacoes.items():
            arquivo.write(f'{categoria} {total} \n')
def lista():
        categorias = list(transacoes.keys())
        valores = list(transacoes.values())

# Imprimir o cabeçalho da tabela
        for categoria in categorias:
            print('{:<20}'.format(categoria), end='')
        print()

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

def menu():
    print('''
    1 - Novo 
    2 - Altera
    3 - Apaga
    4 - Lista
    5 - Grava
    6 - Lê
    
    0 - Sai
    ''') 
    return valida_faixa_inteiro("Escolha uma opção: ", 0, 5)

while True:
    opcao = menu()
    if opcao == 0:
        break
    elif opcao == 1:
        novo()
    elif opcao == 4:
        lista()
    elif opcao == 5:
        grava()
    else:
        continue

# Não consegui imprimir os valores do dicionário como tabela, por favor, tentem modificar - opção '4'