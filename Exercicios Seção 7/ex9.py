"""
crie um Programa que lê 6 valores inteiros pares
e depois exiba na tela em ordem inversa
"""
vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

lista_pares = []
for i in range(0,12):
    if vetor[i] % 2 == 0:
        lista_pares.append(vetor[i])

lista_pares.reverse()
print(lista_pares)