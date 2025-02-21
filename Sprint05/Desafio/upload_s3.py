import boto3

# Criando Sessão
session = boto3.Session(profile_name="442426891183_AdministratorAccess")

s3 = session.client("s3")


bucket_name = "bucket-compass-sprint5"
path = "DADOS_ABERTOS_TECNOVIGILANCIA.csv"
object_name = "DADOS_ABERTOS_TECNOVIGILANCIA.csv"

# Criação do bucket
try:
    s3.create_bucket(Bucket="bucket-compass-sprint5")
    print("Bucket criado com sucesso!")
except Exception as e:
    print(f"Erro ao criar o bucket: {e}")

# Upload do arquivo
try:
    s3.upload_file(path, bucket_name, object_name)
    print(f"Arquivo '{path}' enviado!!")
except FileNotFoundError:
    print("Arquivo não encontrado")
except Exception as e:
    print(f"Erro:{e}")
