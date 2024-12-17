# Exercícios Parte 1
# Escreva um código Python que use a função range() para adicionar três números em uma lista(Esta lista deve chamar-se 'números')  e verificar se esses três números são pares ou ímpares. Para cada número, imprima como saída Par: ou Ímpar: e o número correspondente (um linha para cada número lido).


# Importante: Aplique a função range() em seu código.


# Exemplos de saída:

# Par: 2
# Ímpar: 3

numeros = []

for i in range(1, 4):
    numeros.append(i)
    if i % 2 == 0:
        print(f"Par: {i}")
    else:
        print(f"Ímpar: {i}")
