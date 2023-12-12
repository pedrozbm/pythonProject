"""
Leia um vetor de dez posições. Contar e escrever quantos valores pares ele possui

"""

vetor = []

for i in range(0, 9):
    vetor.append(input())

contagem = 0

for i in vetor:
    if int(i) % 2 == 0:
        contagem = contagem + 1

print(contagem)
