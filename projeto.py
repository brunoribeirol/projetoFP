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


import os
os.system('clear')

transacoes = {'Casa': 0,
              'Comida': 0,
              'Transporte': 0,
              'Salário': 0}

def pede_categoria():
    return input('Categoria: ').title()
def pede_valor():
    return input('Valor: ')
def pede_nome():
    return input('Nome: ') 

def adicao():
    global transacoes
    opcao = input('Desja inserir nova\n[c]ategoria\n[v]alor:\n-->').lower()
    if opcao == 'v':
        nome = pede_nome()
        valor = pede_valor()
        categoria = pede_categoria()
        transacoes[categoria] += float(valor)
    elif opcao == 'c':
        nova_categoria = pede_categoria()
        menu_categoria[nova_categoria] = pede_valor()
    else: 
        print('Digite uma opção válida: ')

def altera():
    global transacoes
    for categoria, valor in transacoes.items():
        print(f'{categoria} --> R$ {valor}')

    p = pede_categoria()
    if p in transacoes.keys():
        print('A alteração apagará o valor anterior.')
        transacoes[p] = pede_valor()

    else:
        print('Categoria não encontrada.\nAperte 1 para nova categoria.')
        
def apaga():
    global transacoes
    for categoria, valor in transacoes.items():
        print(f'{categoria} --> R$ {valor}')
    p = pede_categoria()
    if p in transacoes.keys():
        transacoes.pop(p)
    else:
        print('Categoria não encontrada.')
def grava():
    with open('./projeto/transacoes.csv', 'w', encoding='utf-8') as arquivo:
        for categoria, total in transacoes.items():
            arquivo.write(f'{categoria} {total} \n')
def leitura():
        categorias = list(menu_categoria.values())
        # valores = list(transacoes.values())

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



def menu_funcao():
    print('''
    \t\t-----MENU-----:
    \t\t1 - Novo 
    \t\t2 - Altera
    \t\t3 - Apaga
    \t\t4 - Lista
    \t\t5 - Grava
    \t\t6 - Lê
    
    
    \t\t0 - Sai
    ''') 
    return valida_faixa_inteiro("Escolha uma opção: ", 0, 5)
while True:
    opcao = menu_funcao()
    if opcao == 0:
        break
    elif opcao == 1:
        adicao()
    elif opcao == 2:
        altera()
    elif opcao == 3:
        apaga()
    elif opcao == 4:
        leitura()
    elif opcao == 5:
        grava()
    else:
        continue