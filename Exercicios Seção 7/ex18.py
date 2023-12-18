"""
Faça um programa que leia um vetor de 10 números.
Leia um número x. conte os múltiplos de um número inteiro x
num vetor e mostre-os na tela
"""

vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 7.5]
aux = []

num_lido = int(input('Digite o num '))

for i in vetor:
    if i % num_lido == 0:
        aux.append(i)

print(len(aux))
