# Compiladores
**Grupo:** Micael Mendes, Misael Mendes e Yan Manenti.

## Terminais Codificados

| Cód | Token    |
|-----|---------|
| 1   | while   |
| 2   | var     |
| 3   | to      |
| 4   | then    |
| 5   | string  |
| 6   | real    |
| 7   | read    |
| 8   | program |
| 9  | procedure |
| 10  | print   |
| 11  | nreal   |
| 12  | nint     |
| 13  | literal |
| 14  | integer |
| 15  | if      |
| 16  | ident   |
| 17  | for     |
| 18  | end      |
| 19  | else    |
| 20  | do    |
| 21  | const   |
| 22  | begin   |
| 23  | vstring |
| 24  | >=      |
| 25  | >     |
| 26  | =      |
| 27  | <>       |
| 28  | <=       |
| 29  | <       |
| 30  | +       |
| 31  | ;       |
| 32  | :=       |
| 33  | :      |
| 34  | /       |
| 35  | .       |
| 36  | ,       |
| 37  | *       |
| 38  | )       |
| 39  | (       |
| 40  | {       |
| 41  | }       |
| 42  | -       |
| 43  | $       |
| 44  | î       |

## Não-terminais Codificados

| Cód | Símbolos         |
|-----|------------------|
| 45  | PROGRAMA         |
| 46  | DECLARACOES      |
| 47  | BLOCO           |
| 48  | CONSTANTES      |
| 49  | VARIAVEIS       |
| 50  | PROCEDIMENTOS   |
| 51  | COMANDOS        |
| 52  | LISTAVARIAVEIS  |
| 53  | TIPO   |
| 54  | LDVAR            |
| 55  | REPIDENT           |
| 56  | PARAMETROS           |
| 57  | REPPARAMETROS      |
| 58  | COMANDO   |
| 59  | ITEMSAIDA         |
| 60  | REPITEM         |
| 61  | EXPRESSAO         |
| 62  | TERMO       |
| 63  | EXPR           |
| 64  | FATOR            |
| 65  | TER           |
| 66  | EXPRELACIONAL      |
| 67  | ELSEOPC           |
| 68  | OPREL     |
| 69  | CHAMADAPROC           |
| 70  | LISTAPARAMETROS     |
| 71  | PAR             |
| 72  | REPPAR          |

### Comentários
Comentários são usados para ajudar na compreemsão do código. Comentários em linha serão iniciados por dois sinais numéricos `#`, e comentários de bloco (englobam várias linhas) por um sinal numérico seguido por um asterisco `*`. 

Sintaxe de linha:

```
## Comentário de linha
```

Sintaxe de bloco:

```
#*
Comentário de bloco
*#
```

### Programa
Um PROGRAMA começa com a palavra `program` seguido do identificador, as DECLARAÇÕES e o BLOCO vem depois de um ponto e vírgula `;`, a declaração termina usando um ponto final `.`. As DECLARAÇÕES e o BLOCO são o corpo do PROGRAMA.

Sintaxe:

```
program ident ; DECLARAÇÕES BLOCO .
```

Exemplos:

```
program meuPrograma ;
    begin
        print{"Hello World!"}
    end
.
```

### Declarações
As DECLARAÇÕES são divididas em CONSTANTES, VARIÁVEIS e PROCEDIMENTOS, que são posicionadas em ordem e sem separadores.

### Constantes
É possível criar uma, nenhuma ou múltiplas CONSTANTES, devem ser posicionadas no início das DECLARAÇÕES e antes das VARIÁVEIS. Começam com a palavra `const` seguido do identificador, o tipo é separado do identificador um igual `=` e terminam com ponto e vírgula `;`. No caso de múltiplas CONSTANTES toda a estrutura deve ser copiada. Todas as CONSTANTES são **nint**.

Sintaxe:

```
const ident = nint;
```

Exemplos:

```
const minhaVariavel = 1;const minhaVariavel2 = 2;
```

```
const idade1 = 18;
const idade2 = 50;
```

### Variáveis
É possível criar uma, nenhuma ou múltiplas VARIÁVEIS, devem ser posicionadas depois das CONSTANTES e antes dos PROCEDIMENTOS. Começam com a palavra `var` seguido do identificador, o tipo é separado do identificador por dois pontos `:` e terminam com ponto e vírgula `;`. No caso de múltiplas VARIÁVEIS, é possível agrupá-las por tipo usando uma vírgula para diferenciá-las, chamada de LISTAVARIAVEIS. As VARIÁVEIS podem ser dos tipos **integer**, **real** e **string**.

Sintaxe:

```
var ident : TIPO;
```

Exemplos:

```
var minhaVariavel : string;
var minhaVariavel, minhaVariavel2 : integer;
```

```
var nome : string;
var saldo : real;
```

### Procedimentos
É possível criar um, nenhum ou múltiplos PROCEDIMENTOS, devem ser o último não terminal em DECLARAÇÕES e vir antes do BLOCO de PROGRAMA. Começam com a palavra `procedure` seguido pelo identificador `ident` e PARAMENTROS, ponto e vírgula `;` são utilizados para separar PARAMETROS, BLOCO  e para terminar a declaração.

Sintaxe:

```
procedure nomeProcedimento PARAMETROS ; BLOCO ;
```

#### Parâmetros em Procedimentos
É possível criar um ou nenhum PARAMETRO, deve vir depois do identificador `ident` em PROCEDIMENTOS e antes do ponto e vírgula `;`. Começam com um abre parêntesis `(`, seguido de uma LISTAVARIAVEIS e dois pontos `:`, depois o TIPO é especificado e a declaração termina com um fecha parêntesis `)`.

Sintaxe:

```
( LISTAVARIAVEIS : TIPO )
```

Exemplos:

```
procedure nomeProcedimento (variavel1 : integer) ;
    begin
        COMANDOS
    end
```

```
procedure nomeProcedimento1 (variavel1 : integer, variavel2 : string) ;
    begin
        COMANDOS
    end

procedure nomeProcedimento2 (variavel1, variavel2 : integer, variavel3 : string) ;
    begin
        COMANDOS
    end
```

### Expressão
É um conjunto de operadores matemáticos `+`, `-`, `*` e `/` que utilizam `ident`, `nreal`, `nint`, `literal`, `vstring` e outras EXPRESSÕES entre parênteses como dados entre sí. Pode ser atribuído a um `ident`, usado em `print` e comparado com outra EXPRESSÃO usando operadores relacionais.

Sintaxe:
```
ident := EXPRESSÃO ;
print { EXPRESSÃO } ;
if EXPRESSÃO <> EXPRESSÃO then
```

Exemplo:

```
soma := 1 + 1 ;
saldo := 100.00 - 8.50 ;
contador := contador + 1 ;
```

### Blocos
Todo bloco se inicia com begin e termina com end. São usados para manipulação de dados. Estão localizados depois de DECLARAÇÕES em PROGRAMA, depois de PARÂMETROS em PROCEDIMENTOS, depois do `then` e `else` na estrutura de condição e depois do `do` nas duas estruturas de repetição.

Sintaxe:
```
begin
    COMANDOS
end
```

Exemplo:

```
begin
    print{"Hello World!"}
end
```

### Comandos
Os COMANDOS possibilitam o uso de `print`, estruturas de condição, estruturas de repetição e atribuição para o identificador `ident`.

##### Atribuição de expressão

Sintaxe:

```
ident := EXPRESSÃO
```

Exemplo:

```
mediaNotas := (nota1 + nota2 + nota3) / 3
```

#### Chamada de procedimentos

Lista Parâmetros
LISTAPARAMETROS pode ser um, nenhum, ou múltiplos **ident**, **nint**, **nreal**, **vstring** ou **literal** divididos por vírgula `,`.

Sintaxe:

```
ident(LISTAPARAMETROS)
```

Exemplo:

```
begin
    nota1 := 8.3
    nota2 := 5.2
    nota3 := 6.7
    calculoMedia(nota1, nota2, nota3)
end
```

#### Escrever na tela
Escreve na tela a EXPRESSÃO em ITEMSAIDA.

Sintaxe:

```
print{ITEMSAIDA}
```

Exemplo:

```
print{'Olá mundo!'}
```

#### Estruturas de condição
É uma estrutura que executa código dependendo de uma condição, caso verdadeira o bloco em `then`  é executado, caso falso o bloco em `else` é executado. A condição utiliza EXPRESSÕES e OPERADORES RELACIONAIS para verificar lógica.

Expressão Relacional
É possivel criar uma EXPRESSÃO RELACIONAL, começa e termina com uma EXPRESSÃO, entre elas está uma operação relacional(OPREL), podem ser elas "igual" `=`, "diferente" `<>`, "maior que" `>`, "menor que" `<`, "maior ou igual" `>=` e " menor ou igual" `<=`.

Sintaxe:

```
if EXPRESSÃO OPREL EXPRESSÃO then BLOCO

ou

if EXPRESSÃO OPREL EXPRESSÃO then BLOCO else BLOCO
```

Exemplo sem else:

```
idade := 18
if idade >= 18 then
    begin
        print{'Maior de idade'}
    end
```

Exemplo com else:

```
idade := 18
if idade >= 18 then
    begin
        print{'Maior de idade'}
    end
 else
    begin
        print{'Menor de idade'}
    end
```

#### Estruturas de repetição FOR
O identificador `ident` é usando como um contador, toda vez que o bloco é executado o contador aumenta em um, a repetição para quando o contador for maior que a segunda EXPRESSÃO.

Sintaxe:

```
for ident := EXPRESSAO to EXPRESSAO do BLOCO
```

Exemplo:

```
for i := 0 to 10 do
    begin
        print{i}
    end
```

#### Estruturas de repetição WHILE
Começam com a palavra `while` seguida por uma EXPRELACIONAL, enquanto for verdadeira, o BLOCO depois de `do` será executado.

Sintaxe:
```
while EXPRELACIONAL do BLOCO
```

Exemplo:

```
contador := 1
while contador <= 10 do
    begin
        print{contador}
        contador := contador + 1
    end
```

#### Leitura de dados
Atribui a entrada vinda do usuário para o identificador `ident` dentro dos parênteses.

Sintaxe:

```
read(ident)
```

Exemplo:

```
var nome : string
read(nome)
```

# Regras Léxicas

1. Dados do tipo `integer` aceitam números de -20000000000 até 20000000000.
2. Dados do tipo `real` aceitam números de -20000000000.00 até 20000000000.00. Se a parte decimal for diferente de 0, deve conter duas casas depois de um ponto `.`.
3. Dados do tipo `string` aceitam um único ou uma cadeia de caracteres dentro de aspas duplas `"`.
4. Dados do tipo `literal` aceitam os outros tipos de dado do programa, podem ser escritos diretamente no código sem nenhuma pontuação adiional.
5. Identificadores `ident` não podem conter caracteres especiais, espaços ou iniciar com números, devem ter no máximo 50 caracteres.
6. Comentários de linha devem começar usando `##` e comentários com mais de uma linha devem começar com `#*` e terminar com `*#`.

# Erros Léxicos

1. Dados do tipo `integer` maiores que 20000000000 ou menores que -20000000000.
2. Dados do tipo `real` maiores que 20000000000 ou menores que -20000000000, ou que usam um símbolo diferente de `.` para marcar a parte decimal.
3. Dados do tipo `string` que não usam aspas duplas `"` no começo, fim ou ambos.
4. Identificadores que contenham caracteres especiais, iniciam com números, contenham espaços ou mais de 50 caracteres.
5. Comentários de linha que não começem com `##` e comentário com mais de uma linha que não começem com `#*`, não terminem com `*#` ou ambos.
