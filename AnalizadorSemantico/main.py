from SymbolTable import SymbolTable
from AnalizadorLexico.main import lexicalAnalyzer
from Data.TOKEN_DICT import TOKEN_DICT
from Data.PARSE_TABLE import PARSE_TABLE
from Data.NONTERMINAL_DICT import NONTERMINAL_DICT
import pathlib

symbol_table = SymbolTable()

def handle_semantic_action(production, tokens, i):
    if production.startswith("const"):
        # Ex: const nome = valor ;
        if i+1 < len(tokens) and tokens[i+1][0] == 'ident':
            nome = tokens[i+1][0]
            lexema = tokens[i+1][3]
            linha = tokens[i+1][2]
            tipo_token = tokens[i+3][0] if i+3 < len(tokens) else None
            tipo = "inteiro" if tipo_token == "integer" else ("real" if tipo_token == "real" else "string")
            symbol_table.insert(name=lexema, category="constante", type_=tipo, line=linha)

    # elif production.startswith("var"):
    #     j = i + 1
    #     while j < len(tokens) and tokens[j][0] != ':':
    #         if tokens[j][0] == 'ident':
    #             nome = tokens[j][0]
    #             lexema = tokens[j][3]
    #             linha = tokens[j][2]
    #             tipo_token = tokens[j+2][0] if j+2 < len(tokens) else None
    #             tipo = "inteiro" if tipo_token == "integer" else ("real" if tipo_token == "real" else "string")
    #             symbol_table.insert(name=lexema, category="variável", type_=tipo, line=linha)
    #         j += 1
    elif production.startswith("var"):
        j = i + 1
        identifiers = []

        # Coleta todos os identificadores até encontrar ':'
        while j < len(tokens) and tokens[j][0] != ':':
            if tokens[j][0] == 'ident':
                lexema = tokens[j][3]
                linha = tokens[j][2]
                identifiers.append((lexema, linha))
            j += 1

        # Pega o tipo após ':'
        tipo_token = tokens[j + 1][0] if j + 1 < len(tokens) else None
        tipo = "inteiro" if tipo_token == "integer" else ("real" if tipo_token == "real" else "string")

        # Insere cada identificador com o tipo
        for lexema, linha in identifiers:
            symbol_table.insert(name=lexema, category="variável", type_=tipo, line=linha)

    elif production.startswith("procedure"):
        if i+1 < len(tokens) and tokens[i+1][0] == 'ident':
            nome = tokens[i+1][0]
            lexema = tokens[i + 1][3]
            linha = tokens[i+1][2]
            symbol_table.insert(name=lexema, category="procedure", type_="-", line=linha)
            symbol_table.enter_scope()

    elif production == "begin COMANDOS end":
        symbol_table.enter_scope()

    elif production == "î" and tokens[i][0] == "end":
        symbol_table.exit_scope()

    # Atribuições: verificar se constante está sendo modificada e se os tipos batem
    elif tokens[i][0] == 'ident' and i+1 < len(tokens) and tokens[i+1][0] == ':=':
        symbol_table.verify_assignment(tokens[i], tokens[i+2])

def semanticAnalyzer(folderPath, starter):
    for txt_file in pathlib.Path(folderPath).glob('*.txt'):
        print(f"\n-------------- Análise Semântica do arquivo {txt_file.name} --------------\n")

        entrada = lexicalAnalyzer(folderPath+txt_file.name)
        print("Tokens:", entrada)

        symbol_table.reset()
        symbol_table.enter_scope()

        pilha = ["$", starter]
        x = entrada[0][0]
        i = 0

        while pilha:
            a = pilha[-1]

            if a == x:
                if a == "$":
                    break
                pilha.pop()
                i += 1
                x = entrada[i][0] if i < len(entrada) else "$"

            elif x in ["##", "#*", "*#"]:
                i += 1
                x = entrada[i][0] if i < len(entrada) else "$"
                continue

            elif a in NONTERMINAL_DICT:
                try:
                    prod = PARSE_TABLE[NONTERMINAL_DICT[a]][TOKEN_DICT[x]]
                except:
                    print(f"[Erro Sintático] Produção inválida para {a} com token {x}, linha {entrada[i][2]}")
                    return

                if prod:
                    handle_semantic_action(prod, entrada, i)
                    pilha.pop()
                    symbols = prod.split(" ")
                    if symbols != ["î"]:
                        pilha.extend(reversed(symbols))
                else:
                    print(f"[Erro Sintático] Produção inexistente: {a} -> {x}, linha {entrada[i][2]}")
                    return

            else:
                print(f"[Erro Sintático] Símbolo terminal inesperado: {a}, linha {entrada[i][2]}")
                pilha.pop()

        if x == "$" and pilha == ["$"]:
            print("Análise semântica concluída com sucesso.")
        else:
            print("Erro ao final da análise.")

        symbol_table.print_table()

if __name__ == '__main__':
    semanticAnalyzer("../AnalizadorLexico/codes/", "PROGRAMA")