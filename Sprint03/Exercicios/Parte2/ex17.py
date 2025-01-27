# Exercícios Parte 2
# Escreva uma função que recebe como parâmetro uma lista e retorna 3 listas: a lista recebida dividida em 3 partes iguais. Teste sua implementação com a lista abaixo


# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


def divide_lista(lista):
    tamanho = len(lista) // 3
    lista = lista[: 3 * tamanho]

    return lista[:tamanho], lista[tamanho : 2 * tamanho], lista[2 * tamanho :]


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
resultado = divide_lista(lista)


print(*resultado)
