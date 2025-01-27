# Exercícios Parte 2
# Calcule o valor mínimo, valor máximo, valor médio e a mediana da lista gerada na célula abaixo:


# Obs.: Lembrem-se, para calcular a mediana a lista deve estar ordenada!


# import random
# # amostra aleatoriamente 50 números do intervalo 0...500
# random_list = random.sample(range(500),50)


# Use as variáveis abaixo para representar cada operação matemática:


# mediana
# media
# valor_minimo
# valor_maximo


# Importante: Esperamos que você utilize as funções abaixo em seu código:


# random

# max

# min

# sum


import random

random_list = random.sample(range(500), 50)


mediana = 0
media = 0
valor_minimo = 0
valor_maximo = 0


valor_minimo = min(random_list)
valor_maximo = max(random_list)
media = sum(random_list) / len(random_list)

# Calcula a mediana
ordenada = sorted(random_list)
tamanho = len(ordenada)

if tamanho % 2 == 1:
    # Lista de tamanho ímpar: retorna o valor do meio
    mediana = ordenada[tamanho // 2]
else:
    # Lista de tamanho par: média dos dois valores centrais
    meio1, meio2 = tamanho // 2 - 1, tamanho // 2
    mediana = (ordenada[meio1] + ordenada[meio2]) / 2

# Imprime os resultados exatamente como especificado
print(
    "Media: {:.2f}, Mediana: {:.1f}, Mínimo: {}, Máximo: {}".format(
        media, mediana, valor_minimo, valor_maximo
    )
)
