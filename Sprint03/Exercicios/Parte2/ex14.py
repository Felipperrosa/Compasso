# Exercícios Parte 2
# Escreva uma função que recebe um número variável de parâmetros não nomeados e um número variado de parâmetros nomeados e imprime o valor de cada parâmetro recebido.

# Teste sua função com os seguintes parâmetros:

# (1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)


def leitura_parametros(*args, **kwargs):
    # Imprime os parâmetros não nomeados
    for arg in args:
        print(arg)

    # Imprime os parâmetros nomeados (apenas valores, como no exemplo)
    for value in kwargs.values():
        print(value)


# Teste da função
leitura_parametros(1, 3, 4, "hello", parametro_nomeado="alguma coisa", x=20)
