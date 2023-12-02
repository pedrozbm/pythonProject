"""
Recebendo dados do usuario

input() -> Todo dado recebido via input eh do tipo String

Em Python Tudo que estiver entre:
- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas;
"""
# entrada de dados
# print('Qual seu nome?')
# print moderno

nome = input('Qual seu nome?')

# Input -> Entrada

# print antigo v2.x
# print('Seja bem vindo(a) %s' % nome)

# print moderno v3.x
# print('Seja bem vindo(a) {0}'.format(nome))

# Exemplo de print mais atual v3.7
print(f'Seja bem-vindo(a){nome}')

#print('Qual sua idade?')
idade = int(input('Qual sua idade?'))

# Processamento

# Saida de Dados antiga
# print('A %s tem %s anos' % (nome, idade))

# Exemplo de print v3.x
# print('A {0} tem {1} anos'.format(nome, idade))

# Exemplo de print v3.7
print(f'A {nome} tem {idade} anos')

'''
Cast eh a 'conversão' de um tipo de um tipo de dado para outro
'''
print(f'A {nome} nasceu em {2023 - int(idade)}')

