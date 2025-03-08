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

### Blocos

Todo bloco se inicia com begin e termina com end.

```
begin
  COMANDOS
end
```

### Comandos
Em meio aos blocos eu adiciono comandos, e existem alguns tipos de comandos que posso adicionar ao bloco.

Entrada de dados:
```
ident := expressão


Exemplo:

mediaNotas := (nota1 + nota2 + nota3) / 3
```

Chamada de procedimentos:
```
ident(parâmetros)


Exemplo:

var nota1, nota2, nota3  : real
nota1 := 8.3
nota2 := 5.2
nota3 := 6.7
calculoMedia(nota1, nota2, nota3)
```

Escrever:
```
print{ITEMSAIDA REPITEM}


Exemplo:

print{'Olá mundo!'}
```

Estruturas relacionais:
```
if EXPRELACIONAL then BLOCO

ou

if EXPRELACIONAL then BLOCO else BLOCO


Exemplo:
if idade >= 18 then begin
  print{'Maior de idade'}
end else begin
  print{'Menor de idade'}
end
```

Estruturas de repetição for:
```
for ident := EXPRESSAO to EXPRESSAO do BLOCO


Exemplo:

for i := 0 to 10 do begin
  i := i + 1;
  print{i}
end
```

Estruturas de repetição while:
```
while EXPRELACIONAL do BLOCO


Exemplo:

while repetir = 'S' do begin
  repetir := 'N'
end
```

Leitura de dados.
```
read(ident)


Exemplo:

var nome : string
print{'Informe o seu nome'}
read(nome)
```
