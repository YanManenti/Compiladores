# AnalisadorSemantico/SymbolTable.py

class SymbolTable:
    def __init__(self):
        self.stack = []  # lista de escopos, cada escopo é um dicionário
        self.current_level = -1

    def enter_scope(self):
        self.stack.append({})
        self.current_level += 1
        print(f"[Tabela de Símbolos] Entrando no nível {self.current_level}")

    def exit_scope(self):
        if self.stack:
            print(f"[Tabela de Símbolos] Saindo do nível {self.current_level}")
            self.stack.pop()
            self.current_level -= 1

    def insert(self, name, category, type_, line):
        current_scope = self.stack[-1] if self.stack else {}
        if name in current_scope:
            print(f"[Erro Semântico] Identificador '{name}' já declarado neste escopo. Linha {line}")
            return False
        current_scope[name] = {
            "categoria": category,
            "tipo": type_,
            "nivel": self.current_level
        }
        print(f"[Tabela de Símbolos] Inserido: Nome: {name}, Categoria: {category}, Tipo: {type_}, Nível: {self.current_level}")
        return True

    def lookup(self, name, line):
        for scope in reversed(self.stack):
            if name in scope:
                return scope[name]
        print(f"[Erro Semântico] Identificador '{name}' não declarado. Linha {line}")
        return None

    def verify_assignment(self, ident_token, expression_token):
        ident_name, ident_line = ident_token[0], ident_token[2]
        expr_value, expr_line = expression_token[0], expression_token[2]

        ident_info = self.lookup(ident_name, ident_line)
        if not ident_info:
            return

        if ident_info["categoria"] == "constante":
            print(f"[Erro Semântico] Atribuição não permitida a constante '{ident_name}'. Linha {ident_line}")
            return

        ident_type = ident_info["tipo"]

        # Inferir tipo do lado direito (pode ser literal ou outro ident)
        expr_type = None
        if expr_value.isdigit():
            expr_type = "inteiro"
        elif expr_value.replace('.', '', 1).isdigit():
            expr_type = "real"
        elif expr_value.startswith("'") and expr_value.endswith("'"):
            expr_type = "string"
        elif expr_value.startswith('"') and expr_value.endswith('"'):
            expr_type = "string"
        else:
            expr_info = self.lookup(expr_value, expr_line)
            if expr_info:
                expr_type = expr_info["tipo"]

        if expr_type and not self.types_compatible(ident_type, expr_type):
            print(f"[Erro Semântico] Tipos incompatíveis na atribuição: '{ident_name}' é {ident_type}, expressão é {expr_type}. Linha {ident_line}")

    def types_compatible(self, tipo1, tipo2):
        if tipo1 == tipo2:
            return True
        if tipo1 == "real" and tipo2 == "inteiro":
            return True
        return False

    def print_table(self):
        print("\n===== Tabela de Símbolos =====")
        for i, scope in enumerate(self.stack):
            print(f"\nEscopo nível {i}:")
            for name, info in scope.items():
                print(f"  Nome: {name}, Categoria: {info['categoria']}, Tipo: {info['tipo']}, Nível: {info['nivel']}")
