"""
Escreva um programa que leia 10 numeros inteiros e os armazene
em um vetor. Imprima o vetor, o maior elemento e a posição que ele se encontra


"""

vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

print(vetor)
print(max(vetor))
aux = max(vetor)
print(vetor.index(aux))
