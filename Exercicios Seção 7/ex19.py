"""
Escreva um vetor de 50 números preenchido com o seguinte valor:
(i + 5 * i)%(i + 1), sendo i a posição do elemento no vetor. Em segida imprima
o vetor na tela

"""
vetor = []

for i in range(0, 50):
    vetor.append((i+5*i) % (i+1))

print(vetor)