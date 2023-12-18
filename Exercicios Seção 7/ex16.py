"""
Faça um programa que leia um vetor de 5 posições para
numeros reais e, depois, um codigo inteiro. Se o codigo
for zero, finalize o programa, se for 1, mostre o vetor na
ordem direta, se for 2, mostre o vetor na ordem inversa.
Caso, o codigo for diferente de 1 e 2 escreva uma mensagem
informando que o codigo é invalido

"""

vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 7.5]
print(vetor)

opt = True

while opt is True:
    option = int(input('Digite uma opção: '))

    if option == 0:
        print('Saindo...')
        opt = False
    elif option == 1:
        print(vetor)
    elif option == 2:
        print(vetor[::-1])
    elif option >= 2:
        print("Código inválido")
