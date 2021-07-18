import findspark
from pyspark.sql import SparkSession
from pyspark.conf import SparkConf
findspark.init()
SparkSession.builder.config(conf=SparkConf())
sc = SparkSession.builder.appName('helloworld').getOrCreate()

print(type(sc),"\n")
print(dir(sc))
