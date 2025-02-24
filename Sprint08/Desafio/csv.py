import sys
import re
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)

args = getResolvedOptions(sys.argv, ["JOB_NAME", "S3_INPUT_PATH", "S3_TARGET_PATH"])
job.init(args["JOB_NAME"], args)

match = re.search(r"(\d{4})/(\d{2})/(\d{2})", args["S3_INPUT_PATH"])
ano, mes, dia = match.groups()

df_raw = spark.read.csv(args["S3_INPUT_PATH"], header=True, inferSchema=True, sep="|")

# Filtrar apenas os filmes da trilogia 'O Poderoso Chefão'
godfather_movies = ["The Godfather", "The Godfather Part II", "The Godfather Part III"]
filtered_df = df_raw.filter(df_raw["tituloPincipal"].isin(godfather_movies))

# Criar caminho no S3 usando a data extraída
path = f"{args['S3_TARGET_PATH']}/{ano}/{mes}/{dia}"

# Salvar o DataFrame no S3 em formato Parquet diretamente no caminho
filtered_df.write.mode("overwrite").parquet(path)

job.commit()
