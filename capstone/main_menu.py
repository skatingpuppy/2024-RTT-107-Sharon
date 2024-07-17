#Main Menu

#scripts
import capstone_2
import visualization_capstone_3
import loan_app_capstone_4
import visualization_loan_app_5

#import modules
import pymysql
import pymysql.cursors 
import sys
import os
import pandas as pd
from datetime import datetime
from tabulate import tabulate
import matplotlib.pyplot as plt
import seaborn as sns
import requests
from pyspark.sql import SparkSession
from pyspark.sql import types as T

def main():
    while True:
        print("\n--------------------------------------------------------\n")
        print("MENU")
        print("\nTransaction Details Module")   #2.1
        print("0. Sort Transactions by Zip Code and Date")
        
        print("\nCustomer Details Module")   #2.2
        print("1. Check Customer Details")
        print("2. Modify Customer Details")
        print("3. Generate Monthly Bill")
        print("4. Display Transactions Between Dates")

        print("\nData Analysis and Visualization")
        print("5. Calculate Highest Transaction Count")   #3.1
        print("6. Calculate States with Most Customers")   #3.2
        print("7. Calculate Highest Customer Total Transaction Sums")   #3.3
        
        print("\nLOAN Application")
        print("8. Get LOAN Application Data")   #4
        print("9. Calculate Percentage of Approved Self-Employed Applicants")  #5.1
        print("10. Calculate Percentage of Rejected Married Male Applicants")   #5.2
        print("11. Calculate Top 3 Months with Largest Volume of Transaction Data")   #5.3
        print("12. Calculate Branch that Processed Highest Total Dollar Value of Healthcare Transactions")   #5.4

        print("\n13. Exit")
        print("\n--------------------------------------------------------\n")
              
        choice = input("MENU: \nWhat would you like to do? Write the number. ")
        
        if choice == '0':
            print("You have selected 'Sort Transactions by Zip Code and Date'.\n")
            capstone_2.get_transactions_by_zip_month_year()
        if choice == '1':
            print("You have selected 'Check Customer Details'.\n")
            capstone_2.check_customer_details()
        elif choice == '2':
            print("You have selected 'Modify Customer Details'.\n")
            capstone_2.modify_customer_details()
        elif choice == '3':
            print("You have selected 'Generate Monthly Bill'.\n")
            capstone_2.generate_monthly_bill()
        elif choice == '4':
            print("You have selected 'Display Transactions'.\n")
            capstone_2.display_transactions_between_dates()
        elif choice == '5':
            print("You have selected 'Calculate Highest Transaction Count'.\n")
            visualization_capstone_3.calculate_plot_highest_transaction_count()
        elif choice == '6':
            print("You have selected 'Calculate States with Most Customers'.\n")
            visualization_capstone_3.calculate_plot_top_10_states_most_customers()
        elif choice == '7':
            print("You have selected 'Calculate Highest Customer Total Transaction Sums'.\n")
            visualization_capstone_3.calculate_plot_top_10_customer_total_transaction_sums()
        elif choice == '8':
            print("You have selected 'Get LOAN Application Data'.\n")
            loan_app_capstone_4.get_loan_application_data()
        elif choice == '9':
            print("You have selected 'LOAN Application Data: Calculate Percentage of Approved Self-Employed Applicants'.\n")
            visualization_loan_app_5.calculate_plot_percentage_approved_self_employed()
        elif choice == '10':
            print("You have selected 'LOAN Application Data: Calculate Percentage of Rejected Married Male Applicants'.\n")
            visualization_loan_app_5.calculate_plot_percentage_rejected_married_male()
        elif choice == '11':
            print("You have selected 'LOAN Application Data: Calculate Top 3 Months with Largest Volume of Transaction Data'.\n")
            visualization_loan_app_5.calculate_plot_top_3_months_most_transaction_data()
        elif choice == '12':
            print("You have selected 'LOAN Application Data: Calculate Branch that Processed Highest Total Dollar Value of Healthcare Transactions'.\n")
            visualization_loan_app_5.calculate_plot_branch_highest_value_healthcare_transactions()
        elif choice == '13':
            print("Exiting the program...")
            sys.exit(0)
        else:
            print("Invalid choice. Please try again. ")

        # input("\nPress Enter to return to the main menu. ")

#Run
if __name__ == "__main__":
    main()