import re
import pathlib
from Compiladores.Data.TOKEN_DICT import TOKEN_DICT


def lexicalRules(type,strValue,line):
    if type == TOKEN_DICT['integer']:
        try:
            value = int(strValue)
            if value < -20000000000:
                print(f"Erro Léxico: Integer menor que -20000000000, linha {line}.")
            if value > 20000000000:
                print(f"Erro Léxico: Integer maior que 20000000000, linha {line}.")
        except:
            return

    if type == TOKEN_DICT['real']:
        try:
            value = float(strValue)
            if value < -20000000000.00:
                print(f"Erro Léxico: Real menor que -20000000000.00, linha {line}.")
            if value > 20000000000.00:
                print(f"Erro Léxico: Real maior que 20000000000.00, linha {line}.")
        except:
            return
    if type == TOKEN_DICT['string']:
        value = strValue
        if value == "string":
            return
        if value[0] != '"' and value[-1] != '"':
            print(f"Erro Léxico: String não está encapsulado com aspas duplas (\"), linha {line}.")
    if type == TOKEN_DICT['literal']:
        value = strValue
        if value[0] != "'" and value[-1] != "'":
            print(f"Erro Léxico: Literal não está encapsulada com aspas simples (\'), linha {line}.")
    if type == TOKEN_DICT['ident']:
        value = strValue
        regexNumbers = re.compile(r'[0-9]')
        match = regexNumbers.match(value)
        if match:
            print(f"Erro Léxico: Ident possui números no inicío, linha {line}.")
        regexCaracteres = re.compile('[^a-zA-Z0-9]')
        match = regexCaracteres.match(value)
        if match:
            print(f"Erro Léxico: Ident possui caracteres especiais, linha {line}.")
        regexLength = re.compile(r'.{51,}')
        match = regexLength.match(value)
        if match:
            print(f"Erro Léxico: Ident possui mais de 50 caracteres, linha {line}.")


# Token regex patterns
TOKEN_REGEX = [
    (r'##', '##'),                     # comentário de linha
    (r'#\*', '#*'),                    # início de comentário de bloco
    (r'\*#', '*#'),                    # fim de comentário de bloco
    (r'\".*?\"', 'string'),
    (r'\'.*?\'', 'literal'),
    (r'\d*[a-zA-Z_]\w*', 'ident'),
    (r'\d+\.\d+', 'real'),
    (r'\d+', 'integer'),
    (r'>=|<=|<>|:=|[+\-*/=<>;:.,(){}]', None),
    (r'\s+', None)
]

def tokenize(code):
    lines = 1
    tokenList = []
    position = 0

    while position < len(code):
        match = None
        for pattern, type_hint in TOKEN_REGEX:
            regex = re.compile(pattern)
            match = regex.match(code, position)
            if match:
                value = match.group(0)

                # Trata token #* e *#
                if value == '#*':
                    token_type = TOKEN_DICT.get(value)
                    tokenList.append((value, token_type, lines))

                    end_comment = code.find('*#', match.end())
                    if end_comment == -1:
                        raise SyntaxError(f"Comentário de bloco iniciado na linha {lines} sem fechamento '*#'.")

                    comment_content = code[match.end():end_comment]
                    lines += comment_content.count('\n')

                    tokenList.append(('*#', TOKEN_DICT['*#'], lines))
                    position = end_comment + 2
                    continue

                # Trata token ##
                if value == '##':
                    token_type = TOKEN_DICT.get(value)
                    tokenList.append((value, token_type, lines))

                    end_of_line = code.find('\n', match.end())
                    if end_of_line == -1:
                        position = len(code)
                    else:
                        position = end_of_line + 1
                        lines += 1
                    continue

                if type_hint:  # It's a literal, ident, etc.
                    token_type = TOKEN_DICT.get(value, TOKEN_DICT.get(type_hint))
                    if not token_type:
                        token_type = TOKEN_DICT.get(type_hint)
                    if token_type is None:
                        raise TypeError(f"Tipo de token não encontrado para valor: {value}")
                    lexicalRules(token_type, value, lines)
                else:  # Reserved word or symbol
                    token_type = TOKEN_DICT.get(value)
                    # if not token_type and value.strip():  # maybe identifier
                    #     token_type = TOKEN_DICT.get('ident')
                    if not token_type and value.strip():
                        print(f"DEBUG: Failed to get token_type for value={value}, pattern={pattern}")
                        raise TypeError("Tipo de token não encontrado.")
                if token_type:
                    for key in TOKEN_DICT:
                        if TOKEN_DICT[key] == token_type:
                            tokenList.append((key, token_type, lines))
                break
        if not match:
            raise SyntaxError(f"Token desconhecido: {code[position]}")
        else:
            lines += code[position:match.end()].count('\n')
            position = match.end()

    return tokenList

def folderLexicalAnalyzer(filePath):

    for txt_file in pathlib.Path(filePath).glob('*.txt'):
        print(f"\n-------------- Analizador Léxico para o arquivo {txt_file.name} --------------\n")

        # Read source file
        with open(filePath+txt_file.name, 'r', encoding='utf-8') as f:
            source_code = f.read()

        # Lexical analysis
        tokens = tokenize(source_code)

        print()

        # Output
        for token in tokens:
            print(f"Token: {token[0]:>15} - Código: {token[1]:2} - Linha: {token[2]:2}")

folderLexicalAnalyzer('codes/')

def lexicalAnalyzer(filePath):

        print(f"\n-------------- Mudança de Tokens para o arquivo {filePath} --------------\n")


        # Read source file
        with open(filePath, 'r', encoding='utf-8') as f:
            source_code = f.read()

        # Lexical analysis
        tokens = tokenize(source_code)

        # newTokens = []
        # # Trocando a ordem pq TOKEN_DICT vaid dar problema e eu não vou mudar ele;
        # for token in tokens:
        #     for key in TOKEN_DICT:
        #         if TOKEN_DICT[key] == token[1]:
        #             print("Hitting TOKEN_DICT[key] == token[1] para {}, com key {}".format(TOKEN_DICT[key], key))
        #             tempTuple = (key, token[1], token[2])
        #             print(token)
        #         else:
        #             tempTuple= token
        #
        # print(newTokens)
        # Output
        # for token in tokens:
        #     print(f"Token: {token[0]:>15} - Código: {token[1]:2} - Linha: {token[2]:2}")

        # Pegando apenas os tokens e depois invertendo a lista.
        entrada=[]
        for token in tokens:
            entrada.append(token[0])

        return entrada

#lexicalAnalyzer('codes/')