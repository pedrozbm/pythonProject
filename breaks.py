"""
Saindo de loops com breaks

utilizamos break para sair de loops de maneira projetada
"""

for numero in range(1, 11):
    if numero == 6:
        break
    else:
        print(numero)
print("Sai do loop")

while True:
    comando = input('digite sair para sair')
    if comando == 'sair':
        break;
    