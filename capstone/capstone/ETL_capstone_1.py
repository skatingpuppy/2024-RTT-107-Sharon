###1. Functional Requirements - Load Credit Card Database (SQL)

import secret_user

import pyspark
from pyspark.sql import SparkSession
import os

spark = SparkSession.builder.appName('capstone').getOrCreate()

#read each multiline json file into dataframe
CDW_SAPP_BRANCH = spark.read.option("multiline", "true").json("C:\\Users\\SGKsk\\Development - Per Scholas\\2024-RTT-107-Sharon\\capstone\\cdw_sapp_branch.json")
CDW_SAPP_CREDIT_CARD = spark.read.option("multiline", "true").json("C:\\Users\\SGKsk\\Development - Per Scholas\\2024-RTT-107-Sharon\\capstone\\cdw_sapp_credit.json")
CDW_SAPP_CUSTOMER = spark.read.option("multiline", "true").json("C:\\Users\\SGKsk\\Development - Per Scholas\\2024-RTT-107-Sharon\\capstone\\cdw_sapp_customer.json")

#Replace null values in branch_zip column with 99999
from pyspark.sql.functions import col, when
CDW_SAPP_BRANCH = CDW_SAPP_BRANCH.withColumn("BRANCH_ZIP", when(col("BRANCH_ZIP").isNull(), 99999).otherwise(col("BRANCH_ZIP")))

#Change format of phone number to (XXX)XXX-XXXX
from pyspark.sql.functions import col, concat, lit
CDW_SAPP_BRANCH = CDW_SAPP_BRANCH.withColumn(
    "BRANCH_PHONE",
    concat(
        lit('('), col("BRANCH_PHONE").substr(1, 3), lit(')'),
        col("BRANCH_PHONE").substr(4, 3), lit('-'),
        col("BRANCH_PHONE").substr(7, 4)
    )
)

#Change first and last name columns to upper case and middle name column to lower case
from pyspark.sql.functions import col, upper, lower
CDW_SAPP_CUSTOMER = CDW_SAPP_CUSTOMER.withColumn("FIRST_NAME", upper(col("FIRST_NAME")))
CDW_SAPP_CUSTOMER = CDW_SAPP_CUSTOMER.withColumn("LAST_NAME", upper(col("LAST_NAME")))
CDW_SAPP_CUSTOMER = CDW_SAPP_CUSTOMER.withColumn("MIDDLE_NAME", lower(col("MIDDLE_NAME")))

#Concatenate Apartment no and Street name of customer's Residence with comma as a separator (Street, Apartment)
#then drop the original 2 columns
from pyspark.sql.functions import col, concat_ws
CDW_SAPP_CUSTOMER = CDW_SAPP_CUSTOMER.withColumn(
    "FULL_STREET_ADDRESS",
    concat_ws(", ", col("APT_NO"), col("STREET_NAME"))
)
CDW_SAPP_CUSTOMER = CDW_SAPP_CUSTOMER.drop("APT_NO", "STREET_NAME")

#Change format of customer phone number to XXX-XXXX
from pyspark.sql.functions import col, concat
CDW_SAPP_CUSTOMER = CDW_SAPP_CUSTOMER.withColumn(
    "CUST_PHONE",
    concat(
        col("CUST_PHONE").substr(1, 3), lit('-'),
        col("CUST_PHONE").substr(4, 4)
    )
)

#Convert Day, Month, Year into TIMEID (YYYYMMDD) and drop original 3 columns
from pyspark.sql.functions import col, concat_ws, lpad
CDW_SAPP_CREDIT_CARD = CDW_SAPP_CREDIT_CARD.withColumn(
    "TIMEID",
    concat_ws("", 
              col("YEAR"), 
              lpad(col("MONTH").cast("string"), 2, "0"), 
              lpad(col("DAY").cast("string"), 2, "0"))
)
CDW_SAPP_CREDIT_CARD = CDW_SAPP_CREDIT_CARD.drop("YEAR", "MONTH", "DAY")

#MySQL database connection
host = "localhost"
port = "3306"
user = secret_user.username()
password = secret_user.password()

db = "creditcard_capstone"

#Write dataframe to MySQL
def write_to_mysql(df, table_name):
    df.write \
      .format("jdbc") \
      .option("url", f"jdbc:mysql://{host}:{port}/{db}") \
      .option("driver", "com.mysql.cj.jdbc.Driver") \
      .option("dbtable", table_name) \
      .option("user", user) \
      .option("password", password) \
      .mode("append") \
      .save()

write_to_mysql(CDW_SAPP_CUSTOMER, "CDW_SAPP_CUSTOMER")
write_to_mysql(CDW_SAPP_BRANCH, "CDW_SAPP_BRANCH")
write_to_mysql(CDW_SAPP_CREDIT_CARD, "CDW_SAPP_CREDIT_CARD")



