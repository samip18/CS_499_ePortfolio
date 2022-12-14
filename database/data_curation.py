#!/usr/bin/env python

from pyspark.sql import SparkSession
from pyspark.sql.types import StructField,StructType
from pyspark.sql.types import StringType, IntegerType, DoubleType
from pyspark.sql.functions import col, when

spark = SparkSession.builder\
        .master('yarn') \
        .appName('Data Curator and Validator') \
        .getOrCreate()


# schema enforcement to maintain constrains and ensure quality of data
cust_schema= StructType([ \
        StructField("first_name", StringType(), True), \
        StructField("last_name", StringType(), True), \
        StructField("city", StringType(), True), \
        StructField("county", StringType(), True), \
        StructField("state", StringType(), True), \
        StructField("zip", IntegerType(), True), \
        StructField("zip_2", IntegerType(), True), \
        StructField("resturant_number", IntegerType(), True), \
        StructField("resturant_visit_count", IntegerType(), True), \
        StructField("web_purchase_Y_N", IntegerType(), True), \
        StructField("webstore_spent_amount", DoubleType(), True), \
        StructField("webstore_visit_count", IntegerType(), True), \
        StructField("third_spent_amount", DoubleType(), True), \
        StructField("third_visit_count", IntegerType(), True), \
        StructField("age", IntegerType(), True), \
        StructField("married_Y_N", StringType(), True), \
        StructField("marriage_bin", IntegerType(), True), \
        StructField("income", DoubleType(), True) ])

# reading and standerdized the data
customer_data_df = spark.read.option("delimiter",",") \
        .option("header",True) \
        .option("mode", "DROPMALFORMED") \
        .option("inferSchema", False) \
        .schema(cust_schema) \
        .csv("gs://raw_store_buppa_gump/buppa_gump_dat220.csv")

# check on schema and data
customer_data_df.printSchema()
customer_data_df.show(20,truncate=False)

# efficient efficient data stored back to silver layer for further analysis
customer_data_df.write.mode("overwrite") \
        .parquet("gs://silver_store_buppa_gump/buppa_gump_2022_12.parquet")

print("WRITE COMPLTED")

spark.read.parquet("gs://silver_store_buppa_gump/buppa_gump_2022_12.parquet").show(20, False)

print("CHECK COMPLETED")