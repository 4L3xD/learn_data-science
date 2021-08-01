print('Vamos jogar um jogo!\nObserve:')

# Loops

## variável a recebe um array de strings, cada string é um letra do alfabeto.
# O array é o conjunto das letras do alfabeto. Este é um array de strings.
alfabeto = [' ', 'a', 'b', 'c', '...']

# a função format formata a variável a  na posição entre chaves da string.
print('→ alfabeto = {}'.format(alfabeto))
# \n representa a quebra de linha (pular uma linha). A barra é chamada escape.
print('\n')

# imprime os elementos de índice 0, 1, 2 e 3 do array a. 
print(alfabeto[0], alfabeto[1], alfabeto[2], alfabeto[3])

# a estrutura de repetição for ITERA em y com alcance no comprimento de a
for y in range(len(alfabeto)):
    # IDENTAÇÃO é o páragrafo que ordena o código dentro de suas respectivas funções.
    # print é a função que imprime. Aqui ela imprime o índice y de cada elemento do array a.
    print(y)

input('\nA variável alfabeto é do tipo array de strings e tem como elemento cada letra do alfabeto.\nDigite ENTER para continuar!')

print('\nColuna alternada com elementos do array e seus respectivos índices.')
for y in range(len(alfabeto)):
# imprime cada elemento x no comprimento do array a.
    print(alfabeto[y])
    print(y)
    # alfabeto[0] == ' ', isso quer dizer que o elemento de índice 0 do array alfabeto é o elemento ' ' (espaço)
    # alfabeto[1] == 'a', isso quer dizer que o elemento de índice 1 do array alfabeto é o elemento 'a' (letra a)
    # alfabeto[2] == 'b', isso quer dizer que o elemento de índice 2 do array alfabeto é o elemento 'b' (letra b)
print("""\nObserve que o elemento ' ' tem como sucessor seu próprio índice 0 na coluna.
    Assim como a tem como sucessor seu próprio índice, o número 1 pois a é o segundo elemento do array.""")

input('Digite ENTER  para voltarmos a nossa tabela de colunas com elementos do alfabeto e linha com seus índices!!!')

# vamos criar uma função chamada tabela
# nossa função imprimirá as linhas e colunas da tabela
def Coluna():
    # imprime os elementos de índice 0, 1, 2 e 3 do array a. 
    print('\n')
    print(alfabeto[0], alfabeto[1], alfabeto[2], alfabeto[3], alfabeto[4])

def Linha():
    # a estrutura de repetição for ITERA com alcance no comprimento de a
    for y in range(len(alfabeto)):
        # IDENTAÇÃO é o páragrafo que ordena o código dentro de suas respectivas funções.
        # print é a função que imprime. Aqui ela imprime o índice de cada elemento do array a.
        print(y)

print('\n\nOlha que belezinha nossas funções:\n')
print(Linha)
print(Coluna)

print('\n\nNa coluna a, linha 0 podemos adicionar o primeiro elemento de uma lista.')
# criando a lista/ array
lista = ['an', 'b']
# Arrays são listas

# imprimindo a lista para o usuário
print('→ lista = {}'.format(lista))

# impressão da tabela para o usuário
## executando as funções Coluna() e Linha()
Coluna()
Linha()

# a é elemento do eixo comumemente chamado de x, linha horizontal do plano cartesiano.
## Ou seja, a é elemento de alfabeto que é nosso eixo x.
# 0 é elemento do eixo comumente chamado de y, ou eixo vertical.
## O eixo vertical é o eixo de índices dos elementos do array alfabeto.


input('\nVamos encaixar o primeiro elemento da lista na coluna a, linha 0? ')
# imprimindo o primeiro elemento da lista na coordenada (a,0) da tabela.
Coluna()

# incluindo uma estrutura condicional if(): {} else na função Linha()
def Linha():
    for y in range(len(alfabeto)):
        # haverá apenas uma simples alteração
        # para que SE o índice de alfabeto for igual à 0:
        ## ENTÃO seja impresso na mesma linha o elemento de índice 0 da lista junto ao seu respectivo índice.
        # SENÃO seja impresso apenas o valor do índice
        if (y == 0):
            print(y, lista[0])
        else: print(y)
# Executando a função
Linha()


# Podemos criar uma função justamente para reaproveitar outros códigos.
## Podemos tornar a função menos hardcoded 
# e generalizá-la para que seja possível imprimir cada elemento da lista relativo a uma linha e uma coluna
print('\n\nEncaixando os demais elementos da lista!')

def Tabela():
    def Linha():
        for indice in range(len(lista)):
            for y in range( len( alfabeto ) ):
                #print(count)
                if ( y == indice ):
                    print( y, lista[ indice ] )
    Coluna()
    Linha()

Tabela()
print('\n')


# Dicionários
a = {"Colunas": alfabeto, "Quantidade de colunas": len(alfabeto)}
print(a)

b = {"Linhas": [l for l in range(len(lista))], "Quantidade de linhas": len(lista)}
print(b)

c = {"Linhas": lista, "Quantidade de elementos na lista": len(lista)}
print(c)


print( 'Matriz: {} x {}.'.format( a["Quantidade de colunas"], b[ "Quantidade de linhas" ] ) )


array_tabela = [ a["Colunas"], b["Linhas"] ]
print('Tabela:', array_tabela)