# Compiladores
ident = Identificador/Nome escolhido para declaração.

### Programa
Um PROGRAMA começa com a palavra `program` seguido do identificador, as DECLARAÇÕES e o BLOCO vem depois de um ponto e vírgula `;`, a declaração termina usando um ponto final `.`.

Sintaxe:

```
program ident ; DECLARAÇÕES BLOCO .
```

Exemplos:

```
program meuPrograma ; DECLARAÇÕES BLOCO .
```

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

### Tipagem

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
É possível criar um, nenhum ou múltiplos PROCEDIMENTOS, devem ser o último não terminal em DECLARAÇÕES e vir antes do BLOCO de PROGRAMA. Começam com a palavra `procedure` seguido por `ident` e PARAMENTROS, ponto e vírgula `;` são utilizados para separar PARAMETROS, BLOCO  e para terminar a declaração.

Sintaxe:

```
procedure nomeProcedimento PARAMETROS ; BLOCO ;
```

##### Parâmetros em Procedimentos
É possível criar um ou nenhum PARAMETRO, deve vir depois do `ident` em PROCEDIMENTOS e antes do ponto e vírgula `;`. Começam com um abre parêntesis `(`, seguido de uma LISTAVARIAVEIS e dois pontos `:`, depois o TIPO é especificado e a declaração termina com um fecha parêntesis `)`.

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

### Comandos
Os COMANDOS possibilitam o uso de `print`, estruturas de condição, estruturas de repetição e atribuição para `ident`.

##### Atribuição de dados

Sintaxe:

```
ident := EXPRESSÃO
```

Exemplo:

```
mediaNotas := (nota1 + nota2 + nota3) / 3
```

##### Chamada de procedimentos

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

##### Escrever na tela
Escreve na tela a EXPRESSÃO em ITEMSAIDA.

Sintaxe:

```
print{ITEMSAIDA}
```

Exemplo:

```
print{'Olá mundo!'}
```

##### Estruturas de condição
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

##### Estruturas de repetição FOR
O `ident` é usando como um contador, toda vez que o bloco é executado o contador aumenta em um, a repetição para quando a primeira EXPRESSÃO for maior que a segunda.

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

##### Estruturas de repetição WHILE
Enquanto a EXPRELACIONAL for verdadeira, o BLOCO será executado.

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

##### Leitura de dados
Atribui a entrada vinda do usuário para o `ident` dentro dos parentêsis.

Sintaxe:

```
read(ident)
```

Exemplo:

```
var nome : string
read(nome)
```
