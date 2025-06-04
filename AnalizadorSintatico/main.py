from Data.TOKEN_DICT import TOKEN_DICT
from Data.NONTERMINAL_DICT import NONTERMINAL_DICT
from Data.PARSE_TABLE import PARSE_TABLE
from AnalizadorLexico.main import lexicalAnalyzer

entrada = lexicalAnalyzer("../AnalizadorLexico/codes/code2.txt")
print("Entrada: ",entrada)

pilha = ["$"] # Na verdade, é uma lista, utilizar apenas "append" e "pop";

x = None # Recebe o topo da pilha;
a = "" # Recebe o símbolo de entrada;

print(f"Pilha inicial: {pilha}")
# while x is not "$":
#     if x is "î":
#         x=pilha.pop()
#         print(f"Pop na pilha: {pilha}")
#     elif TOKEN_DICT[x] is not None :
#         if x==a :
#             pilha.pop()
#             print(f"Pop na pilha: {pilha}")
#             continue
#         else :
#             print("Erro linha 17")
#     else :
#         if PARSE_TABLE[TOKEN_DICT[x],TOKEN_DICT[a]] is not None :
#             x=pilha.pop()
#             print(f"Pop na pilha: {pilha}")
#             pilha.append(PARSE_TABLE[TOKEN_DICT[x],NONTERMINAL_DICT[a].split(" ")])
#             print(f"Appended de {PARSE_TABLE[TOKEN_DICT[x],NONTERMINAL_DICT[a]]} na pilha: {pilha}")
#         else:
#             print("Erro linha 23")
#             continue