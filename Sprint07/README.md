
# Índice

- [Índice](#índice)
- [Resumo da Sprint 7](#resumo-da-sprint-7)
  - [Exercícios](#exercícios)
  - [Apache Spark - Contador de Palavras](#apache-spark---contador-de-palavras)
    - [Realizando o pull da imagem:](#realizando-o-pull-da-imagem)
    - [Criando um container:](#criando-um-container)
    - [Jupyter Lab:](#jupyter-lab)
    - [Obtendo arquivos do git:](#obtendo-arquivos-do-git)
    - [Comandos para contar a quantidade de ocorrências de cada palavra contida](#comandos-para-contar-a-quantidade-de-ocorrências-de-cada-palavra-contida)
  - [TMDB](#tmdb)
  - [Conta e API criada com sucesso](#conta-e-api-criada-com-sucesso)
  - [Testando as Credencias e a biblioteca](#testando-as-credencias-e-a-biblioteca)
  - [Resultado](#resultado)

   
   
# Resumo da Sprint 7

## Exercícios

## Apache Spark - Contador de Palavras


### Realizando o pull da imagem: 

![Foto 1](./Exercicios/Spark/Evidencias_Spark/pull.png)


### Criando um container:

![Foto 1](./Exercicios/Spark/Evidencias_Spark/criando_container.png)


![Foto 2](./Exercicios/Spark/Evidencias_Spark/criando_container2.png)

### Jupyter Lab:

![Foto 1](./Exercicios/Spark/Evidencias_Spark/Jupyterlab.png)


### Obtendo arquivos do git: 

![Foto 1](./Exercicios/Spark/Evidencias_Spark/git.png)


### Comandos para contar a quantidade de ocorrências de cada palavra contida 

![Foto 1](./Exercicios/Spark/Evidencias_Spark/container.png)


![Foto 2](./Exercicios/Spark/Evidencias_Spark/comandos.png)


![Foto 3](./Exercicios/Spark/Evidencias_Spark/comandos2.png)


## TMDB

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