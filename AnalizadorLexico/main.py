import numpy as np

# entrada, geralmente vem de um arquivo texto
palavra = open("code.txt", "r").read()

# variavel para armazenar o lexema
lexema = ''

# variavel para armazenar a lista de tokes (que ira alimentar o sintatico)
tokens = []
lexemas = []
dicionario = {
    "while":1,
    "var":2,
    "to":3,
    "then":4,
    "string":5,
    "real":6,
    "read":7,
    "program":8,
    "procedure":9,
    "print":10,
    #"nreal":11,
    #"nint":12,
    "literal":13,
    "integer":14,
    "if":15,
    "ident":16,
    "for":17,
    "end":18,
    "else":19,
    "do":20,
    "const":21,
    "begin":22,
    #"vstring":23,
    ">=":24,
    ">":25,
    "=":26,
    "<>":27,
    "<=":28,
    "<":29,
    "+":30,
    ";":31,
    ":=":32,
    ":":33,
    "/":34,
    ".":35,
    ",":36,
    "*":37,
    ")":38,
    "(":39,
    "{":40,
    "}":41,
    "-":42,
    "##":43,
    "#*":44,
    "*#":45,
    "\n":46,
    '"':47
}

lista = [">","=","<","+",";",":","/",".",",","*",")","(","{","}","-"," ","#",'"']

listaMultiplos = [">=","<>","<=",":=""##","#*","*#"]

def singleSimbolo(texto0,texto1):
    if texto0 is None:
        return False
    if texto0 not in lista:
        return texto0
    if texto0 in lista and texto1 is None:
        return dicionario[texto0]
    if texto0 in lista and texto0+texto1 not in listaMultiplos:
        return dicionario[texto0]
    if texto0+texto1 in listaMultiplos:
        return dicionario[texto0+texto1]
    else:
        return dicionario[texto0]



for i in range(len(palavra)):
    # if palavra[i] in lista:
    #     lexema = palavra[i]
    # elif palavra[i] != " ":
    #     lexema = lexema + palavra[i]
    # else:
    #     lexema = ""

    ####
    # simbolo = singleSimbolo(palavra[i],palavra[i])
    # if simbolo is not False:
    #     lexema += palavra[i]

    ####
    if palavra[i] in lista:
        lexema = palavra[i]
    if dicionario.get(lexema) is None:
        if palavra[i] != " ":
            lexema = lexema + palavra[i]
    # else:
    #     lexema = ""

    print(lexema)  # print opcional para ver o andamento

    if i != len(palavra)-1:
        nextChar = i + 1
    else:
        nextChar = i

    dictCode = dicionario.get(lexema)
    if lexema == " " or lexema == "" or lexema == "\n":
        lexema = ""
    else:
        if dictCode is not None and (palavra[nextChar] is None or palavra[nextChar] is not None and (palavra[nextChar] in lista or palavra[nextChar] == " ")):
                tokens.append(dictCode)
                print(dictCode)
                lexemas.append(lexema)
                lexema = ""
        if dictCode is not None and palavra[nextChar] is not None and (palavra[nextChar] not in lista):
                tokens.append(dictCode)
                print(dictCode)
                lexemas.append(lexema)
                lexema = ""
        if dictCode is None and palavra[nextChar] is not None and (palavra[nextChar] in lista or palavra[nextChar] == " "):
                tokens.append(dicionario["ident"])
                print(dicionario["ident"])
                lexemas.append(lexema)

# Entrega do lexico - token - lexema - linha
for i in range(0, len(tokens)):
    print('Token: ' + str(tokens[i]) + ' - Lexema: ' + str(lexemas[i]) + ' - Linha: 1')

# salvar do lexico para entregar para o sintático
tokens = np.array(tokens)  # converte lista do python para numpy array

