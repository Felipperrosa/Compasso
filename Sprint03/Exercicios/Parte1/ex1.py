# Exercícios Parte 1
# Desenvolva um código em Python que crie variáveis para armazenar o nome e a idade de uma pessoa, juntamente com seus valores correspondentes. Como saída, imprima o ano em que a pessoa completará 100 anos de idade.

from datetime import datetime

# Entrada de dados
nome = "Felippe"
idade = 24


ano_atual = datetime.now().year


ano_100 = ano_atual + (100 - idade)


print(ano_100)
