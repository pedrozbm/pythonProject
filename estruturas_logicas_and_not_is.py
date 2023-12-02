"""
Estruturas lógicas: and, or, not, is

Operadores unários:
    -not, is
Operadores Binários:
    -and, or

Regras de funcionamento:

Para o and, ambos os valores precisam ser True
Para o or, um ou outro valor precisa ser True
Para o not, o valor do booleano é invertido
"""
ativo = True
logado = True

if ativo and logado:
    print("Usuario ativo no sistema")
else:
    print("Você precisa ativar sua conta. Por favor, cheque seu e-mail")

if not ativo:
    print("Você precisa ativar sua conta. Por favro, cheque seu email")
else:
    print("Bem vindo usuario")

if ativo is False:
    print("Você precisa ativar sua conta. Por favor, chque seu email")
else:
    print("Bem vindo usuario")

