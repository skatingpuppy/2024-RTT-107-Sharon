###4 LOAN Application Dataset

import secret_user

import os

def get_loan_application_data():

    #4.1 Create a Python program to GET (consume) data from the above API endpoint for the loan application dataset.
    
    import requests
    #API endpoint
    api_url = "https://raw.githubusercontent.com/platformps/LoanDataset/main/loan_data.json"

    #Send GET request to API endpoint
    response = requests.get(api_url)


    #4.2 Calculate the status code of the above API endpoint.

    #Check status code
    status_code = response.status_code
    print(f"Status Code: {status_code}")

    #Check if request was successful
    if status_code == 200:
        loan_data = response.json()
        print("Data fetched successfully!")
    else:
        print("Failed to fetch data from the API.")


    #4.3 Load data into RDBMS (SQL) w/ PySpark
    from pyspark.sql import SparkSession
    import pandas as pd
    from pyspark.sql import types as T

    spark = SparkSession.builder.appName("LoanData").getOrCreate()

    #Load loan data into a Pandas DataFrame
    loan_df = pd.DataFrame(loan_data)

    schema = T.StructType([
        T.StructField("Application_ID", T.StringType(), True),
        T.StructField("Gender", T.StringType(), True),
        T.StructField("Married", T.StringType(), True),
        T.StructField("Dependents", T.StringType(), True),
        T.StructField("Education", T.StringType(), True),
        T.StructField("Self_Employed", T.StringType(), True),
        T.StructField("Credit_History", T.IntegerType(), True),
        T.StructField("Property_Area", T.StringType(), True),
        T.StructField("Income", T.StringType(), True),
        T.StructField("Application_Status", T.StringType(), True),
    ])

    spark_loan_df = spark.createDataFrame(loan_df, schema=schema)

    #data -> MySQL
    jdbc_url = "jdbc:mysql://localhost:3306/creditcard_capstone"
    table_name = "CDW_SAPP_loan_application"
    properties = {
        "user": secret_user.username(),
        "password": secret_user.password(),
        "driver": "com.mysql.cj.jdbc.Driver"
    }

    spark_loan_df.write.jdbc(url=jdbc_url, table=table_name, mode="overwrite", properties=properties)

    spark.stop()