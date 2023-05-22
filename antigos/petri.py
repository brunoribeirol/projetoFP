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

casa={}; comida={}; transporte={}; lazer={}; ganhos={}
menu={1:casa, 2:comida, 3:transporte, 4:lazer, 5:ganhos}

#def adicao():
    

import os
os.system('clear')
print("Olá Natália! Seja bem-vinda ao seu rastreador de despesas pessoais.\n")

file=open("petri.csv", "a+")

def adicao():
    nova_linha=file.write("\n"+map(input()))
    return nova_linha
file.seek(0)
lines=file.read()
print(lines)
