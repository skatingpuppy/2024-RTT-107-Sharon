###5 Data Analysis and Visualization for LOAN Application

import secret_user

import pandas as pd
import pymysql
import matplotlib.pyplot as plt
import seaborn as sns
import os


def connect_to_db():
    return pymysql.connect(
        host='localhost',
        user=secret_user.username(),
        password=secret_user.password(),
        db='creditcard_capstone'
    )

#5.1 Calculate and plot the percentage of applications approved for self-employed applicants. 
# Use the appropriate chart or graph to represent this data.

def calculate_plot_percentage_approved_self_employed():
    connection = connect_to_db()
    query = "SELECT * FROM CDW_SAPP_loan_application"
    loan_df = pd.read_sql(query, connection)
    connection.close()

    #Calculate % of approved applications for self-employed applicants
    self_employed_total = loan_df[loan_df['Self_Employed'] == 'Yes'].shape[0]
    self_employed_approved = loan_df[(loan_df['Self_Employed'] == 'Yes') & (loan_df['Application_Status'] == 'Y')].shape[0]
    approval_percentage = (self_employed_approved / self_employed_total) * 100

    #Plot
    labels = ['Approved', 'Not Approved']
    sizes = [approval_percentage, 100 - approval_percentage]
    colors = ['#d1eeee', '#f88379']
    explode = (0.1, 0)  # explode 1st slice

    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('Percentage of Applications Approved for Self-Employed Applicants')
    plt.show()


#5.2 
#Calculate the percentage of rejection for married male applicants. 
#Use the ideal chart or graph to represent this data.

def calculate_plot_percentage_rejected_married_male():
    connection = connect_to_db()
    query = "SELECT * FROM CDW_SAPP_loan_application"
    loan_df = pd.read_sql(query, connection)
    connection.close()

    #Calculate % rejected applications for married male applicants
    married_male_total = loan_df[(loan_df['Gender'] == 'Male') & (loan_df['Married'] == 'Yes')].shape[0]
    married_male_rejected = loan_df[(loan_df['Gender'] == 'Male') & (loan_df['Married'] == 'Yes') & (loan_df['Application_Status'] == 'N')].shape[0]
    rejection_percentage = (married_male_rejected / married_male_total) * 100

    #Plot
    labels = ['Rejected', 'Not Rejected']
    sizes = [rejection_percentage, 100 - rejection_percentage]
    colors = ['#f88379', '#d1eeee']
    explode = (0.1, 0)  # explode 1st slice

    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('Percentage of Rejection for Married Male Applicants')
    plt.show()


#5.3 
#Calculate and plot the top three months with the largest volume of transaction data. 
#Use the ideal chart or graph to represent this data.

def calculate_plot_top_3_months_most_transaction_data():
    connection = connect_to_db()
    query = "SELECT * FROM CDW_SAPP_CREDIT_CARD"
    credit_card_df = pd.read_sql(query, connection)
    connection.close()

    #Extract year and month
    credit_card_df['YEAR_MONTH'] = credit_card_df['TIMEID'].astype(str).str[:6]
    monthly_transaction_volume = credit_card_df.groupby('YEAR_MONTH').size().reset_index(name='TRANSACTION_COUNT')

    #Get top 3 months
    top_three_months = monthly_transaction_volume.nlargest(3, 'TRANSACTION_COUNT')

    #Plot
    plt.figure(figsize=(10, 6))
    ax = sns.barplot(x='YEAR_MONTH', y='TRANSACTION_COUNT', data=top_three_months, palette='viridis')
    for i in ax.containers:
        ax.bar_label(i,)      #add value labels to the bars  
    plt.title('Top Three Months with the Largest Volume of Transaction Data')
    plt.xlabel('Year-Month')
    plt.ylabel('Transaction Count')
    plt.show()


#5.4 
#Calculate and plot which branch processed the highest total dollar value of healthcare transactions. 
#Use the ideal chart or graph to represent this data.

def calculate_plot_branch_highest_value_healthcare_transactions():
    connection = connect_to_db()
    query = "SELECT * FROM CDW_SAPP_CREDIT_CARD"
    credit_card_df = pd.read_sql(query, connection)
    connection.close()

    #filter healthcare transactions
    healthcare_transactions = credit_card_df[credit_card_df['TRANSACTION_TYPE'] == 'Healthcare']

    #group by branch and calculate total $ value
    branch_total_value = healthcare_transactions.groupby('BRANCH_CODE')['TRANSACTION_VALUE'].sum().reset_index()

    #get branch with highest total $ value
    top_branch = branch_total_value.nlargest(10, 'TRANSACTION_VALUE')

    #plot
    plt.figure(figsize=(10, 6))
    ax = sns.barplot(x='BRANCH_CODE', y='TRANSACTION_VALUE', data=top_branch, palette='viridis', order=top_branch.sort_values(by='TRANSACTION_VALUE', ascending=False)['BRANCH_CODE'])
    for i in ax.containers:
        ax.bar_label(i,)      #add value labels to the bars  
    plt.title('Branches with the Highest Total Dollar Value of Healthcare Transactions')
    plt.xlabel('Branch Code')
    plt.ylabel('Total Transaction Value')
    plt.show()
