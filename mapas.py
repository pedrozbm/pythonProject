"""
Mapas -> Conhecidos em python como Dicionários
são repensentados por chaves {}

"""
from builtins import sum

receita = {'janeiro': 100, 'fevereiro': 250, 'mar': 400}

# Iterar sobre dicionários
for chave in receita:
    print(chave)  # Imprime as chaves

for chave in receita:
    print(receita[chave])  # Imprime os valores

for chave in receita:
    print(f'no mês de {chave} recebi {receita[chave]}')

print(receita.keys())

for chave in receita.keys():
    print(receita[chave])

# Acessando valores

print(receita.values())

for valor in receita.values():
    print(valor)

# Desenpacotamento de dicionários

for chave, valor in receita.items():
    print(f'chave = {chave} e valor = {valor}')

# Soma*, Valor máximo*, Valor mínimo*, Tamanho

# * Se os valores forem todos inteiros ou reais

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))
