from pyspark.sql import SparkSession


if __name__ == '__main__':
    # create Spark session
    spark = SparkSession.builder.appName("TwitterSentimentAnalysis").getOrCreate()

    # read the tweet data from socket
    lines = spark.readStream.format("socket").option("host", "0.0.0.0").option("port", 5555).load()

    query = lines.writeStream.queryName("all_tweets") \
        .outputMode("append").format("parquet") \
        .option("path", "./parc") \
        .option("checkpointLocation", "./check") \
        .trigger(processingTime='60 seconds').start()
    query.awaitTermination()
