# Desafio

Neste desafio, o objetivo foi construir uma imagem a partir de um arquivo de instruções **Dockerfile** que execute o código **carguru.py**. Após isso, deveria ser executado um contêiner a partir da imagem criada, e em seguida responder à pergunta: "É possível reutilizar contêineres?" Depois, criar um contêiner que permita receber entradas durante sua execução. Também seria necessário criar um arquivo Python que implemente o seguinte algoritmo: receber uma string via input, gerar o hash da string por meio de SHA-1, imprimir o hash na tela utilizando o método **hexdigest**. Em seguida, criar uma imagem Docker chamada **mascarar-dados** que execute o script Python criado anteriormente. Finalmente, iniciar um contêiner a partir da imagem, enviando algumas palavras para o mascaramento.

# Índice

- [Desafio](#desafio)
- [Índice](#índice)
- [Arquivo Dockerfile](#arquivo-dockerfile)
- [Construindo uma imagem](#construindo-uma-imagem)
- [Executando o container a partir da imagem criada](#executando-o-container-a-partir-da-imagem-criada)
- [É possível reutilizar contêineres?](#é-possível-reutilizar-contêineres)
- [Script Python](#script-python)
- [Criando a imagem mascar-dados](#criando-a-imagem-mascar-dados)
- [Iniciando o container](#iniciando-o-container)

# Arquivo Dockerfile

```Dockerfile
FROM python:3

WORKDIR /app

COPY carguru.py .

CMD [ "python", "carguru.py" ]
```


# Construindo uma imagem 

![Evidências](../Evidencias/criando-imagem.png)

![Evidências](../Evidencias/imagemcarguru.png)

# Executando o container a partir da imagem criada 

A opção -it combina -i (modo interativo) e -t (aloca um terminal) para permitir interações com o contêiner por meio de um terminal.

![Evidências](../Evidencias/container_carguru.png)

![Evidências](../Evidencias/containers.png)

# É possível reutilizar contêineres?

Sim, é possível reutilizar containers, desde que eles não sejam removidos. Para isso, utilize o comando

```Docker
docker start <container_id ou container_name>
```

Caso o container tenha terminado com erro ou precise ser ajustado, você pode iniciar um terminal interativo:

```Docker
docker start -i <container_id ou container_name>

```

# Script Python 

  ```Python
  import hashlib

  while True:
      input_data = input(
          "Digite uma string para gerar o hash SHA-1(ou 'sair' para encerrar): "
      )
      if input_data.lower() == "sair":
          break

      hash_result = hashlib.sha1(input_data.encode()).hexdigest()
      print(f"Hash SHA-1: {hash_result}")    

  ```

# Criando a imagem mascar-dados

![Evidências](../Evidencias/imagemmascarar-dados.png)
![Evidências](../Evidencias/image.png)

# Iniciando o container 
   

![Evidências](../Evidencias/container-hash.png)

