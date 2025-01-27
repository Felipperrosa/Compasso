# Exercícios Parte 2
# Leia o arquivo person.json, faça o parsing e imprima seu conteúdo.

# Dica: leia a documentação do pacote jsonimport json

import json

caminho_arquivo = "person.json"

with open(caminho_arquivo, "r") as arquivo:

    dados = json.load(arquivo)

# Imprimir o conteúdo
print(dados)
