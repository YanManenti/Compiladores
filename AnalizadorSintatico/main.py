from Compiladores.Data.TOKEN_DICT import TOKEN_DICT
from Compiladores.Data.NONTERMINAL_DICT import NONTERMINAL_DICT
from Compiladores.Data.PARSE_TABLE import PARSE_TABLE
from Compiladores.AnalizadorLexico.main import lexicalAnalyzer

entrada = lexicalAnalyzer("../AnalizadorLexico/codes/code2.txt")
#print("Entrada: ",entrada)

pilha = ["$", "PROGRAMA"]  # Exemplo de inicialização
x = entrada[0]  # Primeiro token da entrada
i = 0

def handleError(str,errors):
    if str == "$":
        return False
    print(f"Erro: símbolo inválido no topo da pilha: {str}")
    print(f"Removendo {a} do topo da pilha")
    pilha.pop()
    print(f"Pilha: {pilha}")
    return True

while pilha:
    a = pilha[-1]

    if a == x:
        pilha.pop()
        print(f"Consumido terminal '{x}' da pilha.")
        print(f"Pilha: {pilha}")
        i += 1
        x = entrada[i] if i < len(entrada) else "$"

    elif a in NONTERMINAL_DICT:
        prod = PARSE_TABLE[NONTERMINAL_DICT[a]][TOKEN_DICT[x]]
        if prod:
            pilha.pop()
            symbols = prod.split(" ")
            if symbols != ["î"]:  # Produção vazia
                pilha.extend(reversed(symbols))
            print(f"Aplicada produção: {a} → {prod}")
            print(f"Pilha: {pilha}")
        else:
            print(f"Erro de sintaxe: não há produção para ({a}, {x})")
            # print(f"Removendo {a} do topo da pilha")
            # pilha.pop()
            # print(f"Pilha: {pilha}")
            # if handleError(a, errors):
            #     continue
            break

    else:
        print(f"Erro: símbolo inválido no topo da pilha: {a}")
        # print(f"Removendo {a} do topo da pilha")
        # pilha.pop()
        # print(f"Pilha: {pilha}")
        # if handleError(a,errors):
        #     continue
        break

if x == "$" and pilha == ["$"]:
    print("Análise sintática concluída com sucesso.")
else:
    print("Erro ao final da análise.")



# pilha = ["$"]  # Na verdade, é uma lista, utilizar apenas "append" e "pop";
# pilha.extend(entrada)
#
# x = pilha.pop() # Recebe o topo da pilha;
# a = "PROGRAMA" # Recebe o símbolo de entrada;
# print(f"Pilha inicial: {pilha}")
# print(f"x: {x}")
# print(f"a: {a}")
#
# while x != "$":
#     if x == "î":
#         x=pilha.pop()
#         print(f"Pop na pilha: {pilha}")
#     else:
#         print(f"TOKEN_DICT[x]: {TOKEN_DICT[x]}")
#         if TOKEN_DICT[x] is not None :
#             if x==a :
#                 pilha.pop()
#                 print(f"Pop na pilha: {pilha}")
#                 continue
#             else :
#                 print("Erro linha 17")
#         else :
#             print(f"PARSE_TABLE[{NONTERMINAL_DICT[a]}][{TOKEN_DICT[x]}] = {PARSE_TABLE[NONTERMINAL_DICT[a]][TOKEN_DICT[x]]}")
#             print(f"Pilha inicial: {pilha}")
#             print(f"x: {x}")
#             print(f"a: {a}")
#             if PARSE_TABLE[NONTERMINAL_DICT[a]][TOKEN_DICT[x]] is not None:
#                 x=pilha.pop()
#                 print(f"Pop na pilha: {pilha}")
#                 pilha.append(PARSE_TABLE[NONTERMINAL_DICT[a]][TOKEN_DICT[x]].split(" "))
#                 print(f"Appended de {PARSE_TABLE[TOKEN_DICT[x],NONTERMINAL_DICT[a]]} na pilha: {pilha}")
#             else:
#                 print("Erro linha 23")
#                 continue
# print("Ended")