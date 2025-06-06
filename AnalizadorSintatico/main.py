import pathlib

from Data.TOKEN_DICT import TOKEN_DICT
from Data.NONTERMINAL_DICT import NONTERMINAL_DICT
from Data.PARSE_TABLE import PARSE_TABLE
from AnalizadorLexico.main import lexicalAnalyzer


def handleError(str,pilha):
    if str == "$":
        return False
    print(f"ERRO: SÍMBOLO INVÁLIDO NO TOPO DA PILHA: {str}")
    print(f"REMOVENDO {str} DO TOPO DA PILHA")
    pilha.pop()
    print(f"Pilha: {pilha}")
    return True

def syntaxAnalizer(folderPath, starter):
    for txt_file in pathlib.Path(folderPath).glob('*.txt'):
        print(f"\n-------------- Analizador Sintático para o arquivo {folderPath+txt_file.name} --------------\n")

        entrada = lexicalAnalyzer(folderPath+txt_file.name)
        print("Entrada: ",entrada)

        pilha = ["$", starter]  # Exemplo de inicialização
        x = entrada[0][0]  # Primeiro token da entrada
        i = 0

        while pilha:
            a = pilha[-1]
            print(f'a {a} : {x}')

            if a == x:
                if a == "$":
                    break
                pilha.pop()
                print(f"Consumido Token: '{x}', Código: {TOKEN_DICT[x]}, Linha: {entrada[i][2]} da pilha.")
                print(f"Pilha: {pilha}")
                i += 1
                x = entrada[i][0] if i < len(entrada) else "$"

            elif x == '##':
                print(f"Ignorando comentário de linha: {x} : {a}")
                i += 1
                x = entrada[i][0]
                continue

            elif x == '#*':
                print(f"Início de comentário de bloco encontrado: {x} : {a}")
                i += 1
                x = entrada[i][0]

            elif x == '*#':
                print(f"Final de comentário de bloco encontrado {x} : {a}")
                i += 1
                x = entrada[i][0]

                continue

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
                    if handleError(a, pilha):
                        continue
                    break
            else:
                if handleError(a, pilha):
                    continue
                break

        if x == "$" and pilha == ["$"]:
            print("Análise sintática concluída com sucesso.")
        else:
            print("Erro ao final da análise.")

syntaxAnalizer("../AnalizadorLexico/codes/","PROGRAMA")

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