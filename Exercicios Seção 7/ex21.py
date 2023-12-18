"""
Crie um programa que receba do usuario dois vetores A e B
com 10 números inteiros cada. Crie um novo vetor denominado C
calculando C = A - B. Mostre na tela os dados do vetor C
"""
i = 0
A = []
B = []
C = []
while i < 10:
    A.append(int(input('Digite o valor para A')))
    B.append(int(input('Digite o valor para B')))
    i += 1

for i in range(0, len(A)):
    C.append(A[i] + B[i])

print(A, B, C)