from SymbolTable import SymbolTable, Literal, Ident, BinOp
from AnalizadorLexico.main import lexicalAnalyzer
from Data.TOKEN_DICT import TOKEN_DICT
from Data.PARSE_TABLE import PARSE_TABLE
from Data.NONTERMINAL_DICT import NONTERMINAL_DICT
import pathlib

symbol_table = SymbolTable()

def handle_semantic_action(production, tokens, i, verificados):
    if production.startswith("const"):
        if i+1 < len(tokens) and tokens[i+1][0] == 'ident':
            lexema = tokens[i+1][3]
            linha = tokens[i+1][2]
            tipo_token = tokens[i+3][0] if i+3 < len(tokens) else None

            if tipo_token != "integer":
                print(f"[Erro Semântico] Constante '{lexema}' deve ser do tipo inteiro. Linha {linha}")
                symbol_table.has_error = True
            else:
                symbol_table.insert(name=lexema, category="constante", type_="inteiro", line=linha)

    elif production.startswith("var"):
        j = i + 1
        identifiers = []
        while j < len(tokens) and tokens[j][0] != ':':
            if tokens[j][0] == 'ident':
                lexema = tokens[j][3]
                linha = tokens[j][2]
                identifiers.append((lexema, linha))
            j += 1

        tipo_token = tokens[j + 1][0] if j + 1 < len(tokens) else None
        tipo = "inteiro" if tipo_token == "integer" else ("real" if tipo_token == "real" else "string")

        for lexema, linha in identifiers:
            symbol_table.insert(name=lexema, category="variável", type_=tipo, line=linha)

    elif production.startswith("procedure"):
        if i+1 < len(tokens) and tokens[i+1][0] == 'ident':
            lexema = tokens[i + 1][3]
            linha = tokens[i+1][2]
            symbol_table.insert(name=lexema, category="procedure", type_="procedure", line=linha)
            symbol_table.enter_scope()

    elif production == "begin COMANDOS end":
        symbol_table.enter_scope()

    elif production == "î" and tokens[i][0] == "end":
        symbol_table.exit_scope()

    # Verificação de atribuição só quando realmente encontrar ident := …
    elif tokens[i][0] == 'ident' and i + 1 < len(tokens) and tokens[i + 1][0] == ':=':
        ident_name = tokens[i][3]
        line = tokens[i][2]

        if (ident_name, line) in verificados:
            return
        verificados.add((ident_name, line))

        j = i + 2
        lhs = None
        op = None
        rhs = None

        # primeiro operando
        token = tokens[j]
        if token[0] == 'integer':
            lhs = Literal(token[3], 'inteiro')
        elif token[0] == 'real':
            lhs = Literal(token[3], 'real')
        elif token[0] == 'literal':
            lhs = Literal(token[3], 'string')
        elif token[0] == 'ident':
            lhs = Ident(token[3])
        j += 1

        # operador opcional
        if j < len(tokens) and tokens[j][0] in ['+', '-', '*', '/']:
            op = tokens[j][3]
            j += 1

            token = tokens[j]
            if token[0] == 'integer':
                rhs = Literal(token[3], 'inteiro')
            elif token[0] == 'real':
                rhs = Literal(token[3], 'real')
            elif token[0] == 'literal':
                rhs = Literal(token[3], 'string')
            elif token[0] == 'ident':
                rhs = Ident(token[3])

            j += 1
            expr = BinOp(lhs, op, rhs)
        else:
            expr = lhs

        symbol_table.verify_assignment(ident_name, expr, line)

def semanticAnalyzer(folderPath, starter):
    for txt_file in pathlib.Path(folderPath).glob('*.txt'):
        print(f"\n-------------- Análise Semântica do arquivo {txt_file.name} --------------\n")

        entrada = lexicalAnalyzer(folderPath+txt_file.name)
        print("Tokens:", entrada)

        symbol_table.reset()
        symbol_table.enter_scope()

        verificados = set()

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
                    handle_semantic_action(prod, entrada, i, verificados)
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