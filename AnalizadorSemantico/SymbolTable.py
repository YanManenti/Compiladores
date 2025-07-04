class Expr:
    pass

class BinOp(Expr):
    def __init__(self, left, op, right):
        self.left = left     # Expr
        self.op = op         # str, ex: '+', '-', '*', '/'
        self.right = right   # Expr

class Literal(Expr):
    def __init__(self, value, type_):
        self.value = value
        self.type = type_

class Ident(Expr):
    def __init__(self, name):
        self.name = name

class SymbolTable:
    def __init__(self):
        self.stack = []
        self.current_level = -1
        self.has_error = False

    def reset(self):
        self.stack = []
        self.current_level = -1
        self.has_error = False

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
            self.has_error = True
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
        if line is not None:
            print(f"[Erro Semântico] Identificador '{name}' não declarado. Linha {line}")
            self.has_error = True
        return None

    def verify_assignment(self, ident_name, expr, line):
        print(f"Verificando atribuição para {ident_name} na linha {line}")
        ident_info = self.lookup(ident_name, line)
        if not ident_info:
            return

        if ident_info['categoria'] == 'constante':
            print(f"[Erro Semântico] Atribuição não permitida a constante '{ident_name}'. Linha {line}")
            self.has_error = True
            return

        expr_type = self.infer_expr_type(expr)
        if expr_type is None:
            # self.has_error = True
            return

        ident_type = ident_info['tipo']
        if self.types_compatible(ident_type, expr_type):
            return

        print(
            f"[Erro Semântico] Tipos incompatíveis na atribuição: '{ident_name}' é {ident_type}, expressão é {expr_type}. Linha {line}")
        self.has_error = True

    def types_compatible(self, tipo1, tipo2):
        if tipo1 == tipo2:
            return True
        if tipo1 == "real" and tipo2 == "inteiro":
            return True
        return False

    def infer_expr_type(self, expr):
        if isinstance(expr, Literal):
            return expr.type

        if isinstance(expr, Ident):
            info = self.lookup(expr.name, line=None)
            if info:
                return info['tipo']
            else:
                return None

        if isinstance(expr, BinOp):
            left_type = self.infer_expr_type(expr.left)
            right_type = self.infer_expr_type(expr.right)

            if left_type is None or right_type is None:
                self.has_error = True
                return None

            # TIPOS VÁLIDOS PARA OPERAÇÕES ARITMÉTICAS (exemplo)
            valid_types = {'inteiro', 'real'}

            if left_type not in valid_types or right_type not in valid_types:
                print(f"[Erro Semântico] Operação '{expr.op}' não suportada para tipos {left_type} e {right_type}")
                self.has_error = True
                return None

            if left_type == right_type:
                return left_type

            if (left_type == 'real' and right_type == 'inteiro') or (left_type == 'inteiro' and right_type == 'real'):
                return 'real'

            print(f"[Erro Semântico] Tipos incompatíveis na operação '{expr.op}': {left_type} e {right_type}")
            self.has_error = True
            return None

    def print_table(self):
        print("\n===== Tabela de Símbolos =====")
        for i, scope in enumerate(self.stack):
            print(f"\nEscopo nível {i}:")
            for name, info in scope.items():
                print(f"  Nome: {name}, Categoria: {info['categoria']}, Tipo: {info['tipo']}, Nível: {info['nivel']}")