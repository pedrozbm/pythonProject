"""
Leia um vetor de 10 posições e atribua valor 0
para todos os elementos que possuirem valores negativos.
"""
vetor = [-1, 2, -3, 4, -5, 6, 7, 8, 9, 7.5]

print(vetor)

for i in range(0,10):
    if vetor[i] < 0:
        vetor[i] = 0
print(vetor)