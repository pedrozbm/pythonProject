"""
Dicionarios

OBS: Em algumas linguagens de programação, os dicionários Python
são conhecidos como mapas

Dicionários são coleções do tipo chave/valor.

Dicionários são representados por chaves {}.

OBS:
    - Chave e valor são separados por dois pontos (chave: valor);
    - Tanto a chave quanto o valor podem ser de qualquer tipo de dado;
    - Podemos misturar tios de dados

print(type({}))

# Forma mais comun para a criação de dicionários
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

print(paises)
print(type(paises))

# Forma menos comum para a criação

paises = dict(br= 'Brasil', eua = 'Estados Unidos', py= 'Paraguay')
print(paises)
print(type(paises))

# Acessando elementos

# Forma 1 - Acessando via chave, da mesma forma que lista/tupla
print(paises['br'])

# print(paises['py'])
# OBS: Caso tentamos fazer um acesso utilizando uma chave que não existe, teremos o erro KeyError

# Forma 2 - Acessando via get - Recomendada

print(paises.get('br'))
print(paises.get('ru'))

russia = paises.get('ru')
pais = paises.get(input('Digite o prefixo do pais \n'))

if pais:
    print(f'Encontrei o país {pais}')
else:
    print('Não encontrei o país')

pais = paises.get('py', 'Não encontrado') # Caso não ache o país , retorna 'Não encontrado'
print(f'Encontrei o país {pais}')

# Verificando se determinada chave existe no Dicionário
print('br' in paises)
print('ru' in paises)

if 'ru' in paises:
    russia = paises['ru']

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

# Podemos utilizar qualquer tipo de dado, inclusive lista, tupla, dicionários como chaves de dicionários

# Tuplas por exemplo são interessantes como chaves em dicionários, pois as mesma são imutáveis
localidades = {
    (35.6895 , 39.6170): 'Escritório em Tóquio', # Tupla como uma chave
    (40.7128, 74.0068): 'Escritório em Nova York',
    (37.7749, 122.14): "Escritório em São Paulo",
}
print(localidades)
print(type(localidades))

# Adcionar elementos em um dicionário

receita = {'Jan': 100, 'fev': 120, 'mar': 300}

print(receita)
print(type(receita))

# Forma 1

receita['abr'] = 350

print(receita)

# Forma 2

novo_dado = {'Mai': 500}

receita.update(novo_dado)
# Ou
# receita.update({'Mai':500})

print(receita)

# Atualizando dados em um dicionário

# Forma 1

receita['Mai'] = 550

print(receita)

# Forma 2

receita.update({'Mai': 600})

print(receita)

# Conclusão 1 - A forma de adicionar ou atualizar novos elementos em um dicionário é a mesma
# Conclusão 2 - Em dicionários  NÃO podemos ter chaves repetidas.


# Remover dados de um dicionário

receita = {'Jan': 100, 'fev': 120, 'mar': 300}

print(receita)
# Forma 1
ret  = receita.pop('mar')
print(ret)
print(receita)
# OBS: Aqui precisamos sempre informar a chave, e caso não encontre o elemento um KeyError é retornado
# OBS 2: Ao removermos um objeto, o valor deste objeto é sempre retornado

# Forma 2

del receita['fev']
print(receita)

# Se a chave não existir será gerado um KeyError
# OBS: Neste caso o valor removido não é retornado
"""
# Imagine que você tenha um e-Commerce, onde temos um carrinho de compras na qual adcionamos produtos
"""
Carrrinho de compras: 
    Produto 1:
        - nome;
        - quantidade;
        - preço;
    Produto 2:
        - nome;
        -quantidade;        
        - preço;

# 1 - Poderiamos utilizar uma lista para isso? SIM

carrinho = []

produto1 = ['playstation 4', 1, 2300.00]
produto2 = ['God of War 4', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Teriamos que saber qual é o indice de cada informação no produto

# 2 - Poderiamos utilizar uma tupla para isso? SIM

produto1 = ('Playstation 4', 1, 2300.00)
produto2 = ('God of War 4', 1, 150.00)

carrinho = (produto1, produto2)

print(carrinho)

# 3 - Poderiamos utilizar um dicionário para isso? SIM
carrinho = []
produto1 = {'nome': 'Playstation 4', 'Qauntidade': 1, 'preço': 2300.00}
produto2 = {'nome': 'God of War 4', 'Qauntidade': 1, 'preço': 150.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Desta forma, facilmente adicionamos ou removemos produtos no carrinho e em cada produto
# Podemos ter certeza sobre cada operação

# Métodos de dicionários

d = dict(a = 1, b = 2, c=3)

print(d)
print(type(d))

#Limpar o dicionário
d.clear()

print(d)

# Copiando um dicionário para outro

# Forma 1

novo = d.copy() # deep copy
print(novo)

novo['d'] = 4

print(d)
print(novo)

# Forma 2 - Shallow Copy
d = dict(a = 1, b = 2, c=3)

novo = d
print(novo)

novo['d'] = 4
print(d)
print(novo)
"""
# Forma não usual de Criação de Dicionários

outro = {}.fromkeys('a', 'b')
print(outro)
print(type(outro))

usuario = {}.fromkeys(['Nome', 'Pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))

# O método fromkeys recebe dois parâmetros: um iterável e um valor.
# Ele vai gerar para cada valor do iterável uma chave e irá atribuir a esta chave o valor informado

veja = {}.fromkeys('teste', 'valor')
print(veja)

veja = {}.fromkeys(range(1,11),'novo')

print(veja)

