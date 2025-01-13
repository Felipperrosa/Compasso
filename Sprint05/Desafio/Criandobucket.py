import boto3


session = boto3.Session(profile_name="AdministratorAccess-442426891183")

s3 = session.client("s3")

try:
    s3.create_bucket(Bucket="meu-bucket-compasso-sprint5")
    print("Bucket criado com sucesso!")
except Exception as e:
    print(f"Erro ao criar o bucket: {e}")
