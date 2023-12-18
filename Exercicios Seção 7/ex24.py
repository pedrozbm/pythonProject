"""
Faça um programa que leia dez conjuntos de dois valores, o primeiro
representando o número do aluno e o segundo representando sua
altura em metros. Encontre o aluno mais baixo e o mais alto.
Mostre o número do aluno mais baixo e do mais alto, juntamente com suas
alturas
"""

a1 = {1, 1.85}
a2 = {2, 1.88}
a3 = {3, 1.75}
a4 = {4, 1.84}
a5 = {5, 1.61}
a6 = {6, 1.92}

lista_conj = [a1, a2, a3, a4, a5, a6]

print(lista_conj)
print(type(max(a6)))
maior = 0
menor = 10

for i in lista_conj:
    for elemento in i:
        if elemento > maior and elemento %1 != 0:
            maior = elemento

for i in lista_conj:
    for elemento in i:
        if elemento < menor and elemento %1 != 0:
            menor = elemento

for i in lista_conj:
    for elemento in i:
        if elemento == menor:
            print(i)
for i in lista_conj:
    for elemento in i:
        if elemento == maior:
            print(i)



