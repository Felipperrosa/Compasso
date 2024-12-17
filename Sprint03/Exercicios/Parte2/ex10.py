# Exercícios Parte 2
# Escreva uma função que recebe uma lista e retorna uma nova lista sem elementos duplicados. Utilize a lista a seguir para testar sua função.


# ['abc', 'abc', 'abc', '123', 'abc', '123', '123']


def remover_duplicados(lista):
    return list(set(lista))


lista_com_duplicados = ["abc", "abc", "abc", "123", "abc", "123", "123"]
lista_sem_duplicados = remover_duplicados(lista_com_duplicados)
print(lista_sem_duplicados)
