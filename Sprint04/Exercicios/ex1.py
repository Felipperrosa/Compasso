# E01
# Você está recebendo um arquivo contendo 10.000 números inteiros, um em cada linha. Utilizando lambdas e high order functions, apresente os 5 maiores valores pares e a soma destes.
# Você deverá aplicar as seguintes funções no exercício:

# map

# filter

# sorted

# sum
# Seu código deverá exibir na saída (simplesmente utilizando 2 comandos `print()`):
# a lista dos 5 maiores números pares em ordem decrescente;

# a soma destes valores.


with open("number.txt", "r") as file:

    numeros = list(map(int, file.readlines()))


numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))

maiores_pares = sorted(numeros_pares, reverse=True)[:5]


soma_maiores_pares = sum(maiores_pares)

print(maiores_pares)
print(soma_maiores_pares)
