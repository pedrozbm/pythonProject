"""
Loop for

Loop -> Estrutura de repetição.
For -> Uma dessas esrtruturas

for item in interével:
    Execução do loop

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis

Exemplo de iteráveis:
- String
   nome = "Geek University"
- Lista
   lista = [1, 3, 5, 7, 9]
- Range
   números = range(1,10)

nome = "Geek University"
lista = [1, 3, 5, 7, 9]
numeros = range(1, 18)  # Temos que transformar em uma lista

# Exemplo de for 1
for letra in nome:
    print(letra)

# Exemplo 2
for numero in lista:
    print(numero)

# Exemplo 3 (Iterando sobre range)
for numero in range(1, 10):
    print(numero)

# Exemplo 4
for i, letra in enumerate(nome):
    print(letra)

# outro exemplo:
for _, letra in enumerate(nome):  # Quando queremos descartar uma variável, usamos "_"
    print(letra)
"""

soma = 0
qtd = int(input("Quantas vezes o cod deve rodar? \n"))
for n in range(1, qtd + 1):
    num = int(input(f'Informe o número {n}/{qtd} \n'))
    soma = soma+num
print(soma)

nome = "Geek University"
for i in nome:
    print(i, end="")
# O comando "end" faz com que o python não pule uma linha(padrão da linguagem) no print
