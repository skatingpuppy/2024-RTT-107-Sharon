###3. Functional Requirements - Data Analysis and Visualization

import secret_user

import pymysql
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


#establish connection to database
def connect_to_db():
    return pymysql.connect(
        host='localhost',
        user=secret_user.username(),
        password=secret_user.password(),
        db='creditcard_capstone'
    )

#3.1 Calculate and plot which transaction type has the highest transaction count.
def calculate_plot_highest_transaction_count():
    query = """
    SELECT TRANSACTION_TYPE, COUNT(TRANSACTION_TYPE) AS TRANSACTION_COUNT
    FROM CDW_SAPP_CREDIT_CARD
    GROUP BY TRANSACTION_TYPE
    ORDER BY TRANSACTION_COUNT DESC;
    """
    connection = connect_to_db()
    transaction_type_df = pd.read_sql(query, connection)
    connection.close()

    #Plot
    plt.figure(figsize=(10, 6))
    ax = sns.barplot(x='TRANSACTION_TYPE', y='TRANSACTION_COUNT', data=transaction_type_df)
    for i in ax.containers:
        ax.bar_label(i,)      #add value labels to the bars 
    plt.title('Transaction Count by Transaction Type')
    plt.xlabel('Transaction Type')
    plt.ylabel('Transaction Count')
    plt.show()


#3.2 Calculate and plot top 10 states with the highest number of customers
def calculate_plot_top_10_states_most_customers():
    query = """
    SELECT CUST_STATE, COUNT(CREDIT_CARD_NO) AS CUSTOMER_COUNT
    FROM CDW_SAPP_CUSTOMER
    GROUP BY CUST_STATE
    ORDER BY CUSTOMER_COUNT DESC
    LIMIT 10;
    """
    connection = connect_to_db()
    top_states_df = pd.read_sql(query, connection)
    connection.close()

    #Plot
    plt.figure(figsize=(10, 6))
    ax = sns.barplot(x='CUST_STATE', y='CUSTOMER_COUNT', data=top_states_df)
    for i in ax.containers:
        ax.bar_label(i,)      #add value labels to the bars 
    plt.title('Top 10 States with Highest Number of Customers')
    plt.xlabel('State')
    plt.ylabel('Customer Count')
    plt.show()


#3.3 
#Calculate the total transaction sum for each customer based on their individual transactions. 
#Identify the top 10 customers with the highest transaction amounts (in dollar value). 
#Create a plot to showcase these top customers and their transaction sums.

def calculate_plot_top_10_customer_total_transaction_sums():
    query = """
    SELECT CUST_SSN, SUM(TRANSACTION_VALUE) AS TOTAL_TRANSACTION_SUM
    FROM CDW_SAPP_CREDIT_CARD
    GROUP BY CUST_SSN
    ORDER BY TOTAL_TRANSACTION_SUM DESC
    LIMIT 10;
    """

    connection = connect_to_db()
    top_customers_df = pd.read_sql(query, connection)
    connection.close()

    #Plot
    plt.figure(figsize=(10, 6))
    ax = sns.barplot(x='CUST_SSN', y='TOTAL_TRANSACTION_SUM', data=top_customers_df, order=top_customers_df.sort_values(by='TOTAL_TRANSACTION_SUM', ascending=False)['CUST_SSN'])
    for i in ax.containers:
        ax.bar_label(i,)      #add value labels to the bars  
    plt.title('Top 10 Customers with Highest Transaction Amounts')
    plt.xlabel('Customer SSN')
    plt.ylabel('Total Transaction Sum ($)')
    plt.xticks(rotation=45)
    plt.show()