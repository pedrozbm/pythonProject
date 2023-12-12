"""
Faça um programa que preencha um vetor com 10 números reias,
calcule e mostre a quantidade de números negativos e a soma dos números positivos desse vetor

"""
vetor = []
for i in range(-4, 11):
    vetor.append(i)

soma = 0
lista_aux = []
cont = 0
for i in vetor:
    if vetor[i]<0:
        cont = cont+1
    else:
        soma = vetor[i] + soma

print(cont)
print(soma)
print(vetor)