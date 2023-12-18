"""
Faça um programa que leia dois vetores de 10 posições
e calcule outro vetor contendo, nas posições pares os
valores do primeiro e nas posições impares os valores do
segundo
"""

vetor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
vetor2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
aux = []

for i in range(0, 10):
    if i % 2 == 0:
        aux.append(vetor1[i])
    if i % 2 != 0:
        aux.append(vetor2[i])

print(vetor1)
print(vetor2)
print(aux)
