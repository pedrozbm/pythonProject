"""
Conjuntos

- Conjuntos em qualquer linguagem de programação, estamos fazendo referência a Teoria
dos conjuntos da matematica.

- Aqui no Python, os conjuntos são chamados de Sets.

Dito isto, da mesma forma que na matemática:

- Sets não possuem valores duplicados;
- Sets não possuem valores ordenados;
- Elementos não são acessados via índice, ou seja, conjuntos são indexados;

Conkuntos são bons para se utilizar quando precisamos armazenar elementos
mas não nos importamos com a ordenação deles. Quando não precisamos se preocupar com chaves, valores e itens duplicados.

Os conjuntos (sets) são referênciados em Python com chaves {}

Diferença entre Conjuntos {Set} e Mapas {Dicionarios} em Python:
    - Um Dicionário tem chave/valor;
    - Um conjunto tem apenas valor;
"""

# Definindo um conjunto

# Forma 1

s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3}) # Repare que temos valores repetidos

print(s)
print(type(s))

# OBS: Ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo
# será ignorado sem gerar error e não fará parte do conjunto

# Forma 2 - Mais comum

s = {1, 2, 3, 4, 5}
print(s)
print(type(s))

# Podemos verificar se determinado elemento está no conjunto
if 3 in s:
    print('tem o 3')
else:
    print('não tem o 3')

# Importante lembrar que além de não termos valores duplicados,
# Também não temos ordem
