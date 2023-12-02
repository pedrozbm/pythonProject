"""
Tipo Float

Tipo real, decimal

OBS: os separados de casas decimais na programação é o pontoe não a virgula

"""
# Errado
'''valor = 1, 44
print=(valor)
'''
# Certo
valor = 1.44
print(valor)
print(type(valor))

# É possível
valor1, valor2 = 1, 44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

# podemos converter um float par int
res = int(valor)
print(res)
print(type(res))

# podemos trabalhar com numeros complexos

variavel = 5j
