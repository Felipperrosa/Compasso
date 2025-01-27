import boto3
import pandas as pd
import os
from datetime import datetime

# Criando Sessão
session = boto3.Session(profile_name="")
s3 = session.client("s3")

# Definindo nome do bucket e caminho dos arquivos
bucket_name = "data-lake-felippe"
datas_path = "./dados"

# Definindo caminho para os arquivos
movies_path = os.path.join(datas_path, "movies.csv")
series_path = os.path.join(datas_path, "series.csv")

# Lendo os arquivos
df_movies = pd.read_csv(movies_path, sep="|", low_memory=False)
df_series = pd.read_csv(series_path, sep="|", low_memory=False)

# Obtendo a data atual para formar o caminho.
current_date = datetime.now().strftime("%Y/%m/%d")

# Criação do bucket S3
try:
    s3.create_bucket(Bucket="data-lake-felippe")
    print("Bucket criado com sucesso!")
except Exception as e:
    print(f"Erro ao criar o bucket: {e}")


# Função Upload do arquivo S3
def upload_s3(file_path, bucket, s3_path):
    try:
        s3.upload_file(file_path, bucket, s3_path)
        print(f"Arquivo '{file_path}' enviado para {bucket}!")
    except FileNotFoundError:
        print(f"Arquivo {file_path} não encontrado.")
    except Exception as e:
        print(f"Erro ao enviar o arquivo: {e}")


# Caminho o caminho no S3 para o arquivo de filmes e fazendo o upload
path_movies_s3 = f"Raw/Local/CSV/Movies/{current_date}/movies.csv"
upload_s3(movies_path, bucket_name, path_movies_s3)

# Caminho no S3 para o arquivo de séries e fazendo o upload
path_series_s3 = f"Raw/Local/CSV/Series/{current_date}/series.csv"
upload_s3(series_path, bucket_name, path_series_s3)
