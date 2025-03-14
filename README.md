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
