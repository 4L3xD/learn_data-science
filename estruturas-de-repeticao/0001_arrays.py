print('A inovação não percorre caminhos conhecidos.\nVamos brincar com os índices do nosso array.')

lista = ['an', '_b']
print('→ lista = ' + str(lista))

concatenacao = lista[1] + lista[0] + lista[0] + lista[0]
print('\n\'' + concatenacao + '\'' + ' é a concatenação dos elementos de índice [1, 0, 0, 0] do array lista.\n')

#___________________________
bananan = concatenacao
#___________________________
tupla = tuple(bananan)
print('TUPLA:' + str(tupla))

elementos = [ elemento for elemento in bananan ]
print('ITERAÇÃO dos elementos do array por meio da Estrutura de Repetição FOR:\n' + str(elementos))

baaa = [ letra for letra in bananan if letra != bananan[-1]]
print('\nITERAÇÃO do FOR com Estrutura Condicional IF: \n' + str(baaa))

print('\nNós concatenamos os elementos de índice [1, 0, 0, 0] do array → {}: {}.'.format(lista, bananan))
# junção dos elementos do array
str_bananan = ''.join(bananan)
banana = str_bananan[1:-1]
print("""\nApós realizar a junção dos elementos do array,
    podemos delimitar os parâmetros de INÍCIO e FIM com os índices [1:-1] e obtemos: \'{}\'.""".format(banana))

aeiou = '-'.join(map(str, banana))
print('\nVamos juntar os elementos do array e adicionar hífens entre eles, que agora são elementos da string:\n' + aeiou)


print('\nTambém podemos coletar os elementos formando sílabas:')
be_a_ba = ''.join(map(str, banana[::3]))
ba = be_a_ba
print(ba)

be_a_ba = ''.join(map(str, banana[2::3]))
na = be_a_ba
print(na)

be_a_ba = ''.join(map(str, banana[4::]))
na_ = be_a_ba
print(na_)

print('\nE novamente formar a palavra:')
print(ba + na + na)

