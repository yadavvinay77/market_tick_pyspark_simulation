from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, LongType

KAFKA_BROKER = "localhost:9092"
TOPIC = "market_ticks"

def main():
    spark = SparkSession.builder \
        .appName("KafkaSparkConsumer") \
        .master("local[*]") \
        .getOrCreate()

    schema = StructType([
        StructField("time", LongType(), True),
        StructField("bid", DoubleType(), True),
        StructField("ask", DoubleType(), True),
        StructField("last", DoubleType(), True),
        StructField("volume", DoubleType(), True),
        StructField("symbol", StringType(), True),
    ])

    df = spark.readStream.format("kafka") \
        .option("kafka.bootstrap.servers", KAFKA_BROKER) \
        .option("subscribe", TOPIC) \
        .option("startingOffsets", "latest") \
        .load()

    # Kafka value is in binary, convert to string
    json_df = df.selectExpr("CAST(value AS STRING) as json_str")

    # Parse JSON data
    parsed_df = json_df.select(from_json(col("json_str"), schema).alias("data")).select("data.*")

    query = parsed_df.writeStream \
        .outputMode("append") \
        .format("console") \
        .start()

    query.awaitTermination()

if __name__ == "__main__":
    main()
