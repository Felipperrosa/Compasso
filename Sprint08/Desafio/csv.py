from pyspark.sql.functions import lit
import sys
import re
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import current_date

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

# Adicionar as colunas de 'ano', 'mes' e 'dia' ao DataFrame
df_raw = df_raw.withColumn("ano", lit(ano))
df_raw = df_raw.withColumn("mes", lit(mes))
df_raw = df_raw.withColumn("dia", lit(dia))

# Particionar os dados por 'ano', 'mes' e 'dia' e salvar como Parquet
df_raw.write.partitionBy("ano", "mes", "dia") \
    .mode("overwrite") \
    .parquet(f"{args['S3_TARGET_PATH']}")


job.commit()
