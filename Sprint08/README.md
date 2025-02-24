
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

[numeros.](./Exercicios/Geração_e_massa_de_dados/warmup.ipynb)

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
[animals.csv.](./Exercicios/Geração_e_massa_de_dados/animals.csv)


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
[nomes_aleatorios.txt.](./Exercicios/Geração_e_massa_de_dados/nomes_aleatorios.txt)





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

