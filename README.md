# Compiladores
ident = Identificador/Nome escolhido para declaração.

### Programa
Um PROGRAMA começa com a palavra `program` seguido do identificador, as DECLARAÇÕES e o BLOCO vem depois de um ponto e vírgula `;`, a declaração termina usando um ponto final `.`.

Sua estrutura é:

```
program ident ; DECLARAÇÕES BLOCO .
```

Exemplos:

```
program meuPrograma ;  .
```

### Declarações
As DECLARAÇÕES são divididas em CONSTANTES, VARIÁVEIS e PROCEDIMENTOS, que são posicionadas em ordem e sem separadores.

### Constantes
É possível incluir uma ou nenhuma CONSTANTE, devem ser posicionadas no início das DECLARAÇÕES e antes das VARIÁVEIS. Começam com a palavra `const` seguido do identificador, o tipo é separado do identificador um igual `=` e terminam com ponto e vírgula `;`. No caso de múltiplas CONSTANTES toda a estrutura deve ser copiada. Todas as CONSTANTES são **nint**.

Sua estrutura é:

```
const ident = nint;
```

Exemplos:

```
const minhaVariavel = nint;const minhaVariavel2 = nint;
```

```
const idade1 = nint;
const idade2 = nint;
```

### Variáveis
É possível incluir uma ou nenhuma VARIÁVEL, devem ser posicionadas depois das CONSTANTES e antes dos PROCEDIMENTOS. Começam com a palavra `var` seguido do identificador, o tipo é separado do identificador por dois pontos `:` e terminam com ponto e vírgula `;`. No caso de múltiplas VARIÁVEIS, é possível agrupá-las por tipo usando uma vírgula para diferenciá-las. As VARIÁVEIS podem ser dos tipos **integer**,**real** e **string**.

Sua estrutura é:

```
var ident : integer;
```

Exemplos:

```
var minhaVariavel, minhaVariavel2 : integer;
```

```
var nome : string;
var saldo : real;
```
