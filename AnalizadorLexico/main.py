import numpy as np

# entrada, geralmente vem de um arquivo texto
palavra = open("code.txt", "r").read()

# variavel para armazenar o lexema
lexema = ''

# variavel para armazenar a lista de tokes (que ira alimentar o sintatico)
tokens = []
lexemas = []
dicionario = {
    "void" : 2,
    "main" : 11,
    "}" : 38,
    "{" : 39,
    "inicio": 15,
    "fim": 20,
    ";": 40
}
lista = ["{","}",";"]
for i in range(len(palavra)):  # percorre a entrada
    # if palavra[i] == '{':
    #     lexema = palavra[i]
    # elif palavra[i] != ' ':  # se nao for espaço... aqui tem q colocar
    #     # outros caracters como pontuacao e parentização
    #     lexema = lexema + palavra[i]
    # else:
    #     lexema = ''
    if palavra[i] in lista:
        lexema = palavra[i]
    elif palavra[i] != " ":
        lexema = lexema + palavra[i]
    else:
        lexema = ""

    print(lexema)  # print opcional para ver o andamento

    dictCode = dicionario.get(lexema)
    if dictCode is not None:
        tokens.append(dictCode)
        lexemas.append(lexema)
        lexema = ""

    # if lexema == 'void':  # classifica o lexema em token conforme a gramatica
    #     tokens.append(2)  # obrigatorio salvar o cod do token
    #     lexemas.append(lexema)  # opcional salvar, pode somente mostrar
    # elif lexema == 'main':
    #     tokens.append(11)
    #     lexemas.append(lexema)
    # elif lexema == '}':
    #     tokens.append(38)
    #     lexemas.append(lexema)
    # elif lexema == '{':
    #     tokens.append(39)
    #     lexemas.append(lexema)
    #     lexema = ''
    # elif lexema == 'inicio':
    #     tokens.append(15)
    #     lexemas.append(lexema)
    # elif lexema == 'fim':
    #     tokens.append(20)
    #     lexemas.append(lexema)
    # elif lexema == ';':
    #     tokens.append(40)
    #     lexemas.append(lexema)

# Entrega do lexico - token - lexema - linha
for i in range(0, len(tokens)):
    print('Token: ' + str(tokens[i]) + ' - Lexema: ' + str(lexemas[i]) + ' - Linha: 1')

# print(tokens) # [2, 11, 39, 15, 40, 20, 38]

# salvar do lexico para entregar para o sintático
tokens = np.array(tokens)  # converte lista do python para numpy array

