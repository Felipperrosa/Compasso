
# Índice

- [Índice](#índice)
- [Resumo da Sprint 8](#resumo-da-sprint-8)
- [Certificados](#certificados)
    - [Não houve certificados nessa Sprint](#não-houve-certificados-nessa-sprint)
- [Exercícios](#exercícios)
- [Apache Spark](#apache-spark)
- [Geração e massa de dados](#geração-e-massa-de-dados)
  - [Warm up](#warm-up)
    - [1.Números Aleatórios](#1números-aleatórios)
    - [Resultado](#resultado)
    - [2. Animais](#2-animais)
    - [Resultado](#resultado-1)
  - [Nomes Aleatórios](#nomes-aleatórios)
    - [Resultado](#resultado-2)
  - [TMDB(Feito na sprint07)](#tmdbfeito-na-sprint07)
  - [Conta e API criada com sucesso](#conta-e-api-criada-com-sucesso)
  - [Testando as Credencias e a biblioteca](#testando-as-credencias-e-a-biblioteca)
  - [Resultado](#resultado-3)

   
   
# Resumo da Sprint 8
Nesta sprint, colocamos em prática os conhecimentos adquiridos sobre o Apache Spark na sprint 07, juntamente com o uso do AWS Glue, para realizar o processamento e a transformação de dados no contexto de um data lake. O objetivo principal foi avançar na construção da camada Trusted, que representa a etapa em que os dados estão limpos, padronizados e prontos para análise, após serem integrados a partir de diversas fontes da camada Raw.

# Certificados

### Não houve certificados nessa Sprint


# Exercícios

- [Geração e massa de dados.](./Exercicios/Geração_e_massa_de_dados/)
- [TMDB.](./Exercicios/TMBD/)
- [Spark.](./Exercicios/Spark/)

# Apache Spark 
O Exercício se encontra no notebook abaixo

[Spark.](./Exercicios/Spark/spark.ipynb)



# Geração e massa de dados

## Warm up 

### 1.Números Aleatórios 

```python

import random

numbers = [random.randint(1, 500) for _ in range(250)]
numbers.reverse()

print(numbers)


```
### Resultado 

[41, 100, 63, 54, 380, 335, 223, 198, 195, 362, 341, 107, 59, 467, 265, 462, 433, 166, 79, 21, 451, 371, 94, 399, 44, 428, 382, 273, 223, 113, 68, 18, 438, 257, 213, 152, 180, 138, 282, 65, 259, 60, 91, 316, 73, 72, 412, 352, 315, 200, 190, 230, 304, 384, 136, 198, 369, 103, 176, 29, 350, 325, 61, 214, 107, 481, 156, 122, 256, 485, 449, 328, 174, 175, 285, 376, 100, 54, 498, 159, 388, 193, 25, 296, 121, 269, 364, 196, 197, 289, 411, 325, 247, 74, 251, 202, 335, 120, 290, 344, 237, 115, 130, 298, 469, 312, 190, 115, 145, 470, 78, 141, 365, 131, 68, 472, 452, 361, 226, 302, 467, 298, 420, 171, 278, 288, 117, 16, 199, 226, 356, 146, 489, 190, 390, 167, 27, 472, 187, 35, 17, 134, 21, 344, 289, 100, 60, 69, 352, 464, 8, 272, 398, 405, 278, 175, 70, 326, 83, 318, 327, 145, 205, 163, 153, 166, 54, 419, 7, 279, 294, 417, 260, 312, 276, 234, 357, 292, 64, 402, 290, 243, 226, 405, 97, 67, 62, 178, 31, 285, 379, 406, 239, 346, 211, 484, 3, 368, 491, 294, 393, 111, 99, 96, 7, 179, 66, 364, 405, 113, 56, 398, 266, 405, 165, 337, 212, 235, 184, 79, 446, 471, 315, 259, 4, 495, 11, 105, 47, 398, 204, 338, 32, 164, 297, 99, 499, 105, 195, 60, 453, 7, 356, 404, 6, 459, 364, 277, 323, 262]


### 2. Animais 


```python
import csv

animals  = ["Leão", "Tigre", "Elefante", "Girafa", "Lobo", "Cachorro", "Gato", "Urso", "Águia", "Tubarão",
"Cobra", "Cavalo", "Panda", "Cervo", "Rinoceronte", "Gorila", "Jacaré", "Raposa", "Coelho", "Arraia",
"Golfinho", "Falcão", "Zebra", "Porco-espinho", "Pinguim"]

animals.sort()

[print(x) for x in animals]

with open('animals.csv', mode ='w',newline='') as file:
    writer = csv.writer(file)
    for x in animals:
        writer.writerow([x])

print("Nomes armazenados com sucesso!")
```
### Resultado 
[Geração e massa de dados.](./Exercicios/Geração_e_massa_de_dados/animals.csv)

## Nomes Aleatórios 

```python
import random
import names
import time

random.seed(40)

amount_unique_names = 3000

amount_random_names = 10000000

aux=[]

for i in range(0,amount_unique_names):
    
    aux.append(names.get_full_name())

print("Gerando {} nomes aleatórios".format(amount_random_names))

dados=[]

for i in range(0,amount_random_names):
    dados.append(random.choice(aux))
    
with open("nomes_aleatorios.txt", "w", encoding="utf-8") as f:
    for row in dados:
        f.write(f"{row}\n")
    

```

### Resultado 
[Geração e massa de dados.](./Exercicios/Geração_e_massa_de_dados/nomes_aleatorios.txt)





## TMDB(Feito na sprint07)

## Conta e API criada com sucesso 

![Foto 1](./Exercicios/TMBD/Evidencias_TMBD/Conta_tmdb.png)


## Testando as Credencias e a biblioteca
```python
import requests
import pandas as pd
from IPython.display import display

api_key = "MINHA_CHAVE"
url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={api_key}&language=pt-BR"


response = requests.get(url)
data = response.json()

filmes = []

for movie in data["results"]:
    df = {
        "Título": movie["title"],
        "Data de lançamento": movie["release_date"],
        "Visão geral": movie["overview"],
        "Votos": movie["vote_count"],
        "Média de votos": movie["vote_average"],
    }
    filmes.append(df)

df = pd.DataFrame(filmes)
display(df)
```
## Resultado

![Foto 1](./Exercicios/TMBD/Evidencias_TMBD/Resultado.png)

