"""
Módulo Collections - Counter (Contador)

Collections -> High-performance Container Datetypes

Counter -> Recebe um iterável como parâmetro e cria um projeto do tipo
Collection Counter que é parecido com um dicionário, contendo como chave
o elemento da lista passada como valor a quantidade de ocorrencias desse elemento

# Utilizando o counter

from collections import Counter

# Podemos utilizar qualquer iterável, aqui usamos lista
lista = [1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5, 4, 66, 88, 7, 8, 34, 45]

# Utilizando o Counter
res = Counter(lista)

print(type(res))

print(res)
# Note que, para cada elemento da lista, o Counter criou uma chave e colocou
# como valor a quantidade de ocorrencias.

"""
from collections import Counter

# Exemplo 2:
print(Counter('Geek University'))

# Exemplo 3:
texto = """O Cerco de Guînes ocorreu de maio a julho de 1352, quando um exército francês comandado
 por Geoffrey de Charny tentou, sem sucesso, recapturar o castelo francês em Guînes, que havia sido tomado 
 pelos ingleses em janeiro anterior. O cerco fez parte da Guerra dos Cem Anos e ocorreu durante a precária e pouco respeitada
trégua de Calais (1347-1355). O castelo altamente fortificado tinha sido conquistado pelos ingleses durante um período
 de trégua nominal e o rei inglês, Eduardo III, decidiu mantê-lo. Charny liderou uma força de 4500 homens e retomou a cidade,
  mas não conseguiu bloquear o castelo. Após dois meses de luta intensa, um grande ataque noturno inglês ao acampamento francês 
  infligiu uma pesada derrota e os franceses retiraram-se. Guînes foi incorporado ao Pale de Calais. O castelo foi sitiado pelos
   franceses em 1436 e 1514, mas conseguiu resistir em cada uma das vezes, até cair nas mãos dos franceses em 1558. """

palavras = texto.split()

res = Counter(palavras)
print(res)

# Encontrando as 5 palavras com mais ocorrencia de texto
print(res.most_common(5))
