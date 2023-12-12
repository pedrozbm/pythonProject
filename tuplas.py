"""
Tuplas (tuple)

Existem duas diferenças básicas entre tuplas e listas

1 - As tuplas são representadas por parenteses ()

2 - As tuplas são IMUTÁVEIS, ao se criar uma tupla ela não muda
Toda a operação com uma tupla gera uma nova tupla


# As tuplas sao representadas por (), mas também podem não ter:
tupla = 1, 2, 3, 4
print(type(tupla))

# Tuplas com um elemento
tupla_falsa = 4  # Não é uma tupla
print(type(tupla_falsa))
tupla_real = (4,)  # É uma tupla!
print(type(tupla_real))
# Podemos concluir que tuplas são definidas pela virgula, não pelos parenteses

# Podemos gerar uma Tupla com range(inicio, fim, passo)

tupla = tuple(range(11))
print(tupla)
print(type(tupla))

# Desempacotamento de Tupla

tupla = ('Geek University', 'Programação em Python: Essencial')
escola, curso = tupla

print(escola)
print(curso)
# Lembrando que, o n° de variaveis deve ser igual ao n° de elementos

# Métodos para adição e remoção de elementos nas tuplas não existem, pois são IMUTÁVEIS
# Soma, Max, Min e Tamanho ainda funcionam se os valores forem inteiros ou reais
tupla = 1, 2, 3, 4
print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))
# Concatenação de tuplas
tupla1 = (1, 2, 3)
print(tupla1)

tupla2 = (4, 5, 6)
print(tupla2)
print(tupla1 + tupla2)

# Sobrescrevendo o valor da tupla
tupla1 = tupla1 + tupla2 # Apesar de imutáveis, podemos sobrescrever
print(tupla1)

# Verificar se determinado elemento está na tupla
print(3 in tupla)
# Iterando sobre uma tupla

tupla = (1, 2 ,3)
for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)

# Contando elementos dentro de uma tupla

tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')
print(tupla.count('a'))

escola = tuple('Geek University')
print(escola)
print(escola.count('e'))
# Dicas no uso de tuplas

# Devemos utilizar sempre que não precisamos modificar os dados contidos em uma coleção

# Exemplo 1
meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
print(len(meses))

# O acesso a elementos de uma Tupla também é semelhante a de uma lista

print(meses[5])

# Iterar com while
i = 0

while  i < len(meses):
    print(meses[i])
    i = i+1
# Verificamos em qual indice um elemento está na tupla
print(meses.index('Março'))

# Slicing
# Tupla[Inicio:Fim:Passo]
print(meses[5:9])

# Por quê utilizar tuplas?

# Tuplas são mais rápidas do que listas.
# Tuplas deixam seu código mais seguro, devido sua imutabilidade
"""
# Copiando uma tupla para outra
tupla = (1, 2, 3)
print(tupla)

nova = tupla # Na tupla não temos o problema de Shallow copy

print(nova)
print(tupla)

outra = (4, 5, 6)
nova = nova + outra

print(nova)
print(tupla)