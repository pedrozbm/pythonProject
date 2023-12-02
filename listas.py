"""
Listas

Listas em python funcionam como vetores ou matrizes (arrays) em outras linguagens
São DINÂMICAS e permitem a adição de QUALQUER tipo de dado.

linguagens C/Java: Arrays
   - Possuem tamanho e tipo de dado fixo;
   Ou seja, nestas linguagens se você criar um array do tipo int e com tamanho 5, este array
   será SEMPRE do tipo inteito e poderá ter SEMPRE no Máximo 5 valores.

Já em Pyton:

    -Dinâmico: Não possui tamanho fixo; Ou seja, podemos criar a Lista e simplesmente ir adicionando elementos;
    - Qualquer tipo de dado: Não possuem tipo de dado fixo; ou seja, qualquer dado

As listas em python são representadas por colchetes: []
"""

type([])

lista1 = [1, 2 , 5 , 7, 44]

lista2 = ['G', 'e', 'e','k',' ', 'U','n','i','v','e','r','s','i','t','y']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')

#Podemos checar se determinado valor está na lista

num = 7
if num in lista1:
    print(f'encontrei o {num}')
else:
    print(f"não encontrei o {num}")
i = 0

if 'e' in lista5:
    print("Encontrei a letra e")
    i += 1
    print(i)
else:
    print("Não encontrei a letra e")

# Podemos facilmente cordenar uma lista

lista1.sort() #Ordena os dados da lista
print(lista1)

print(lista5.count('e')) #Conta o número de ocorrência

#Adcicionar elementos em listas

"""
Para adicionar elemntos em listaas, utilizamos a função append
OBS: Com append é adicionado somente um elemento por vez
"""
lista1.append(48) #adicona o elemento 48 a lista
print(lista1)

lista1.append([1, 5 , 8]) #Podemos adicionar outra lista na lista! Porém como elemento único

lista1.extend([123, 44, 67]) #Adiciona os valores listados a essa lista
print(lista1)

#Podemos iserir um novo elemento na posição que quisermos
lista1.insert(2, "novo valor")
print(lista1)

"""
#Podemos juntar duas listas
lista6 = lista1 + lista2
print(lista6)
ou
lista1.extend(lista2)
"""
#Podemos inverter uma lista
lista1.reverse()
print(lista1)
#Também podemos usar o Slice para isso
print(lista1[::-1])

#Podemos Copiar uma lista
lista6 = lista2.copy()
print(lista6)

#Podemos contar quantos elementos tem uma Lista
print(len(lista1))

#Podemos remover facilmente o último elemento de uma lista
print(lista5)
lista5.pop() #O não somemnte remoe o ultimo elemnento mas também o retorna
print(lista5)

#Podemos remover um elemento pelo índice
lista5.pop(2)
print(lista5)

#Podemos limpar uma lista(Remover todos seus elementos)
lista5.clear()
print(lista5)

#Podemos repetir elementos em uma lista
nova = [1, 2, 3]
nova = nova*3
print(nova)

#Podemos conververter uma String para uma Lista
curso  = "Programaçao em Python: Essencial"
print(curso)
curso = curso.split() #Por padrão o Slpit separa os elementos pelos espaços e os transforma em lista
print(curso)
#Também Podemos definir o parametro de separação do Split
curso = "Programação,em,python:,Essencial"
curso = curso.split(",")
print(curso)

#Converter uma lista em uma String
lista6 = ["Programação", 'em', 'python:', 'essencial']
print(lista6)
curso = ' '.join(lista6) #Adicionamos espaço entre cada elemento e tranformamos em String
print(curso)

#Iterando sobre listas
soma = 0
for i in lista3:
    print(i)
""""
carrinho = []
produto = ""
while produto != 'sair':
    print('Adicione um produto na lista ou digite "sair" para sair: ')
    produto = input()
    if produto != "sair":
        carrinho.append(produto)
for produto in carrinho:
    print(produto)


cores = ["verde", "amarelo", "azul", "branco"]

for cor in cores:
    print(cor)

index = 0
while index < len(cores): # O comando 'len' representa o tamanho da lista
    print(cores[index])
    index = index+1

# Gerar indice em um for
for index, cor in enumerate(cores): # Faz com que a lista seja enumerada
    print(index, cor)

# Encontrar o indice de um elemnto na lista

# Em qual indice está o valor chamado
#OBS: RETORNA O INDICE DO PRIMEIRO VALOR ENCONTRADO
numeros = [5, 6, 7, 8, 9, 10]
print(numeros.index(10))

# Podemos fazer busca dentro de um range, ou seja, qual indice começar a buscar
print(numeros.index(7, 2)) # index( numero a ser buscado, inicio da busca)

print(numeros.index(6, 2, 5)) # Busca o numero 6 entre os indices 2 e 5

"""
# Revisão de Slicing

# lista[inicio : fim :passo]
# range [inicio: fim: passo]

# Trabalhando com slice de lista com o parâmetro 'inicio'
lista = [1, 2, 3, 4]
print(lista[1:]) # Iniciando no indice 1 e pegando todos os elementos restantes

# Trabalhando com Slice de lista com o parametro 'fim'
print(lista[:3]) # Começa em 0, pega até o índice 3

# Definindo incio e final
print(lista[1:3]) # Começa no indice 1 e termina no 3

# Trabalhando com o parâmetro 'passo'
print(lista[1::2]) #começa em 1, vai até o final, de 2 em 2
