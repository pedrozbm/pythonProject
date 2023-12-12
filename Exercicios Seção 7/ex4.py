"""
Faça um programa que leia um veotr de 8 posições e, em seguida, leia
também dois valores X e Y quaisquer correspondentes a duas posições no vetor.
Ao final seu programa deverá escrever a soma dos valores encontrados nas respectivas posições X e Y

"""

vetor = []

for num in range(0, 8):
   vetor.append(input(f'Digite o valor {num} do vetor \n'))

X = int(input('Digite o index do numero \n'))
Y = int(input('Digite o index do outro numero \n'))

print(f'A soma dos numeros dos indices selecionados é: {int(vetor[X])+int(vetor[Y])}')



