"""
Faça um programa que leia um vetor de 10 posições e verifique se
existem valores iguais e os escrever na tela

"""
vetor = [2, 2, 2, 4, 5, 5, 5, 8, 9, 2]

for i in range(0, 10):
    for j in vetor:
        vetor.count(i)
    if vetor.count(i) > 1:
       print(f'{vetor[i]} se repete {vetor.count(i)} vezes')


