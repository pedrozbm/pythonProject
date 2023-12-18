"""
Escreva um programa que leia números inteiros no intervalo[0,50]
e armazene em um vetor com 10 posições. Preencha um segundo vetor
apenas com os números impáres do primeiro vetor, imprima os dois vetores
2 elementos por linha
"""

lista = []
aux = []

for i in range(0, 50):
    while i < 10:
        lista.append(i)
        break
for i in range (0,len(lista),2):
    print(lista[i:i+2])

for i in lista:
    if i % 2 != 0:
        aux.append(i)

for i in range(0, len(aux), 2):
    print(aux[i:i+2])
