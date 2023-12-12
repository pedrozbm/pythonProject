"""
Fazer um programa para ler 5 valores e, em seguida
mostrar a posição onde se encontram o maior e menor valor
"""
vetor = [1,2,3,4,5]

aux = max(vetor)
print(vetor.index(aux))
aux = min(vetor)
print(vetor.index(aux))