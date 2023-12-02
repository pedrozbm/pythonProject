'''
Em python um dado é considerado do tipo String sempre que 

- Estiver entre aspas simples -> 'uma string', '234', 'a', 'True', '32.3'
- Estiver entre aspas duplas -> "uma string", "234", "a", "True", "32.3"
- Estiver entre aspas simples triplas ou duplas

print(type("geek"))
print('geek')
print(type("""geek"""))

nome = "Gina's Bar"
print(nome)
'''

nome = "Geek University"
print(nome.upper())
print(nome.split()) # -> Transforma em uma lista de string 'Geek', 'University'
print(nome[0:4]) # -> Imprime as 4 primeiras letras da variavel
print(nome[5:15])
# Essa operação é chamada de slice de string

print(nome.split()[0]) #imprime 'Geek' na tela

print(nome[::-1])
"comece do primeiro elemento, vá até o ultimo elemento e inverta"

print(nome.replace('e','P'))
