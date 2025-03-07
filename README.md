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

### Procedimentos

É possível incluir um ou nenhum PROCEDIMENTO. Eles devem ser posicionados após as VARIÁVEIS e antes do BLOCO principal do programa. Um PROCEDIMENTO começa com a palavra `procedure`, seguida do identificador e dos PARÂMETROS caso houver PARÂMETROS. Após isso, há um ponto e vírgula `;` em seguida, um BLOCO contendo comandos.

Sua estrutura é:

```
procedure ident PARAMETROS ;
begin
    COMANDOS
end;

```

Exemplos:

```
procedure mostrarMensagem;
begin
    print "Olá, mundo!";
end;
```

```
procedure soma(a, b: integer);
begin
    print a + b;
end;
```


### Parametros
Um PROCEDIMENTO pode ou não receber PARÂMETROS. Caso receba, eles devem ser declarados entre parênteses `()`, seguidos do tipo. É possível declarar múltiplos parâmetros separando-os por vírgula `,`.

Sua estrutura é:

```
procedure ident ( LISTAVARIAVEIS : TIPO );
begin
    COMANDOS
end;
```

Exemplos:

```
procedure exibirNome(nome: string);
begin
    print nome;
end;
```

### Comandos
Comandos são os comandos, read, if, for, while, que são comandos que utilizam uma estrutura alguns não são obrigatoriamente utilizar o BLOCO após sua inicialização...
