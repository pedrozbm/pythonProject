"""
Faça um programa que receba do usuário um vetor com 10 posições.
Em seguida deverá ser impresso o maior e o menor elemento do vetor
"""

vetor = []
for i in range(0, 9):
    vetor.append(int(input()))


print(f'Mínimo: {min(vetor)}')
print(f'Máximo: {max(vetor)}')

