import numpy as np

# entrada, geralmente vem de um arquivo texto
palavra = list(open("code.txt", "r").read())
print(palavra)
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

def singleSimbolo(currentI,currentChar,nextChar):
    if currentChar is None:
        return False
    if currentChar not in lista:
        return currentChar
    if currentChar in lista and nextChar is None:
        return dicionario[currentChar]
    if currentChar in lista and currentChar+nextChar not in listaMultiplos:
        return dicionario[currentChar]
    if currentChar+nextChar in listaMultiplos:
        return dicionario[currentChar+nextChar]
    else:
        return dicionario[currentChar]


stringStatus = False
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
    if palavra[i] in lista and stringStatus is False:
        lexema = palavra[i]
    if dicionario.get(lexema) is None:
        if palavra[i] != " " and stringStatus is False:
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
        if stringStatus is False:
            lexema = ""
    else:
        if palavra[i] == '"' or stringStatus is True:
            if palavra[i] == '"' and stringStatus is True:
                lexema = lexema + palavra[i]
                stringStatus = False
                tokens.append(dicionario["string"])
                lexemas.append(lexema)
                print(dicionario["string"])
                lexema = ""
            else:
                stringStatus = True
                if palavra[i] != '"':
                    lexema = lexema + palavra[i]

        elif dictCode is not None and (palavra[nextChar] is None or palavra[nextChar] is not None and (palavra[nextChar] in lista or palavra[nextChar] == " ")):
                tokens.append(dictCode)
                print(dictCode)
                lexemas.append(lexema)
                lexema = ""
        elif dictCode is not None and palavra[nextChar] is not None and (palavra[nextChar] not in lista):
                tokens.append(dictCode)
                print(dictCode)
                lexemas.append(lexema)
                lexema = ""
        elif dictCode is None and palavra[nextChar] is not None and (palavra[nextChar] in lista or palavra[nextChar] == " "):
                tokens.append(dicionario["ident"])
                print(dicionario["ident"])
                lexemas.append(lexema)

# Entrega do lexico - token - lexema - linha
for i in range(0, len(tokens)):
    print('Token: ' + str(tokens[i]) + ' - Lexema: ' + str(lexemas[i]) + ' - Linha: 1')

# salvar do lexico para entregar para o sintático
tokens = np.array(tokens)  # converte lista do python para numpy array

