"""
Ler dois conjuntos de números reais, armazenando-os em
vetores e calcular o produto escalar entre eles. Os
conjuntos têm 5 elementos cada. Imprimir os dois conjuntos
e o produto escalar, sendo que o produto escalar é dado por:
x1*y1 + x2*y2 + xn*yn

"""
conj1 = {1, 2, 3, 4, 5}
conj2 = {6, 7, 8, 9, 10}
lista1 = list(conj1)
lista2 = list(conj2)

print(conj1,'\n', conj2)
aux = []
for i in range(0, 5):
    aux.append(lista1[i] + lista2[i])
print(aux)