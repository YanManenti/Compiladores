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
program meuPrograma ;  .
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

### ListaVariáveis
LISTAVARIAVEIS pode ser um, nenhum, ou múltiplos `ident` divididos por vírgula `,`. São usados para agrupar VARIAVEIS por tipo.

### Variáveis
É possível criar uma, nenhuma ou múltiplas VARIÁVEIS, devem ser posicionadas depois das CONSTANTES e antes dos PROCEDIMENTOS. Começam com a palavra `var` seguido do identificador, o tipo é separado do identificador por dois pontos `:` e terminam com ponto e vírgula `;`. No caso de múltiplas VARIÁVEIS, é possível agrupá-las por tipo usando uma vírgula para diferenciá-las. As VARIÁVEIS podem ser dos tipos **integer**, **real** e **string**.

Sintaxe:

```
var ident : TIPO;
```

Exemplos:

```
var minhaVariavel, minhaVariavel2 : integer;
```

```
var nome : string;
var saldo : real;
```

### Procedimentos
É possível criar um, nenhum ou múltiplos PROCEDIMENTOS, devem ser o último não terminal em DECLARAÇÕES e vir antes do BLOCO de PROGRAMA. Começam com a palavra `procedure` seguido por `ident` e PARAMENTROS, ponto e vírgula `;` são utilizados para separar PARAMETROS e BLOCO para terminar a declaração.

Sintaxe:

```
procedure nomeProcedimento PARAMETROS ; BLOCO ;
```

Exemplos:

```
procedure nomeProcedimento PARAMETROS ; BLOCO ;
```

```
procedure nomeProcedimento1 PARAMETROS ; BLOCO ;
procedure nomeProcedimento2 PARAMETROS ; BLOCO ;
```

### Parametros
É possível criar um ou nenhum PARAMETRO, deve vir depois do `ident` em PROCEDIMENTOS e antes do ponto e vírgula `;`. Começam com um abre parêntesis `(`, seguido de uma LISTAVARIAVEIS e dois pontos `:`, depois o TIPO é especificado e a declaração termina com um fecha parêntesis `)`.

Sintaxe:

```
( LISTAVARIAVEIS : TIPO )
```

Exemplos:

```
( variavel1 : integer )
```

```
( variavel1, variavel2 : integer )
( variavel1, variavel2 : integer, variavel3 : real )
```

### ListaParâmetros
LISTAPARAMETROS começa com abre parêntesis `(,` pode ser um, nenhum, ou múltiplos **ident**, **nint**, **nreal**, **vstring** ou **literal** divididos por vírgula `,` e termina com fecha parêntesis `)`.

### ExpRelacional
É possivel criar uma EXPRELACIONAL, começa e termina com uma EXPRESSÃO, entre elas está uma operação relacional, podem ser elas `=`, `<>`, `>`, `<`, `>=` e `<=`, representando igual, diferente, maior que, menor que, maior ou igual e menor ou igual em ordem.

