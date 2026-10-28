from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType, IntegerType, DoubleType


spark= SparkSession.builder \
    .appName("ComprasStreaming") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

esquema = StructType() \
    .add("producto", StringType()) \
    .add("cantidad", IntegerType()) \
    .add("precio", DoubleType()) \
    .add("timestamp", DoubleType())

compras = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "compras") \
    .option("startingoffsets", "latest") \
    .load()

compras = compras.select(
    from_json(col("value").cast("string"), esquema).alias("datos")
).select("datos.*")

compras = compras.withColumn(
    "total",
    col("cantidad") * col("precio")
)

def procesar_batch(lote, numero_batch):
    print("===== BATCH:", numero_batch, "=====")
    print("Compras procesadas:", lote.count())
    lote.show(truncate=False)

consulta = compras.writeStream \
    .foreachBatch(procesar_batch) \
    .start()

consulta.awaitTermination()
