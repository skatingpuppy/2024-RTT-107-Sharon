###2.1 Transaction Details Module

import main_menu
import secret_user

import pymysql.cursors  #MySQL Connector for Python
import os

#Function to interact with user and retrieve transactions
def get_transactions_by_zip_month_year():

    #connect to MySQL database
    connection = pymysql.connect(host="localhost",
                                 user=secret_user.username(),
                                 password=secret_user.password(),
                                 db="creditcard_capstone",
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    

    try:
        with connection.cursor() as cursor:
            #2.1.1: Prompt user for zip code and validate
            while True: 
                zip_code = input("Enter the ZIP code (5 digits): ")
                if zip_code.isdigit() and len(zip_code) == 5:
                    break
                else:
                    print("Invalid ZIP code format. Please enter a 5-digit ZIP code. ")

            #2.1.2: Prompt user for month and year and validate
            while True:
                month = input("Enter the month (1-12): ")
                year = input("Enter the year (YYYY): ")
                if len(month) == 1:
                    month = "0" + month
                if month.isdigit() and year.isdigit() and 1 <= int(month) <= 12 and len(year) == 4:
                    break
                else:
                    print("Invalid input format. Please enter a valid month (1-12) and year (YYYY). ")

            year_month = year+month+'%'

            #2.1.3: Query database
            sql = """
                SELECT card.TIMEID, 
                card.TRANSACTION_ID,
                card.TRANSACTION_VALUE,
                cust.CUST_ZIP
                FROM cdw_sapp_credit_card card
                LEFT JOIN cdw_sapp_customer cust ON card.CREDIT_CARD_NO = cust.CREDIT_CARD_NO
                GROUP BY card.TRANSACTION_ID, card.TRANSACTION_VALUE, card.TIMEID, cust.CUST_ZIP
                HAVING card.TIMEID LIKE %s AND cust.CUST_ZIP LIKE %s
                ORDER BY card.TIMEID DESC;
            """

            cursor.execute(sql, (year_month, zip_code))
            transactions = cursor.fetchall()

            #2.1.4: Display results
            if transactions:
                print(f"\nTransactions for ZIP code {zip_code} in {year}-{month}, sorted by day: ")
                for transaction in transactions:
                    print(f"Date: {transaction['TIMEID']}, ID: {transaction['TRANSACTION_ID']}, Amount: ${transaction['TRANSACTION_VALUE']}")
            else:
                print(f"No transactions found for ZIP code {zip_code} in {year}-{month}")

    except pymysql.Error as e:
        print(f"Error querying the database: {e}")
    finally:
        connection.close()
        #GO BACK TO MAIN MENU
        print("\nGoing back to main menu...\n\n")
        return main_menu.main()




###2.2 Customer Details Module

import pymysql
import sys
import os
import pandas as pd
from datetime import datetime
from tabulate import tabulate


def connect_to_db():
    #Connect to MySQL database
    connection = pymysql.connect(
        host="localhost",
        user=secret_user.username(),
        password=secret_user.password(),
        db="creditcard_capstone"
    )
    return connection

def check_customer_details():
    connection = connect_to_db()

    #SSN: allow user input and validate
    while True:
        SSN = input("Enter customer's SSN. \nIf you would like to go back to main menu, write 'Menu'. ")
        if SSN.isdigit() and len(SSN) == 9:
            break
        elif SSN.lower() == 'menu':
            #GO BACK TO MAIN MENU
            print("\nGoing back to main menu...\n\n")
            return main_menu.main()
        else:
            print("Invalid SSN format. Please enter as XXXXXXXXX (9 digits). ")
    
    while True:
        try:
            query = "SELECT * FROM CDW_SAPP_CUSTOMER WHERE SSN = %s;"
            df = pd.read_sql(query, connection, params=(SSN))
            if not df.empty:
                print(f"\nCustomer details for SSN {SSN}:")
                print(df)      #would use tabulate to make dataframe prettier, but tabulate doesn't wrap text, and too many columns pushes the data off
                #print(tabulate(df, headers='keys', tablefmt='psql')) 
            else:
                print(f"\nNo customer found with SSN {SSN}")
        except Exception as e:
            print(f"\nError querying the database: {e}")
        finally:
            connection.close()
            #GO BACK TO MAIN MENU
            print("\nGoing back to main menu...\n\n")
            return main_menu.main()


def modify_customer_details():
    connection = connect_to_db()

    #SSN: allow user input and validate
    while True:
        SSN = input("Enter customer's SSN. If you would like to go back to main menu, write 'Menu'. ")
        if SSN.isdigit() and len(SSN) == 9:
            break
        elif SSN.lower() == 'menu':
            #GO BACK TO MAIN MENU
            print("\nGoing back to main menu...\n\n")
            return main_menu.main()
        else:
            print("Invalid SSN format. Please enter as XXXXXXXXX (9 digits). ")
    
    #Column: allow user input
    while True:
        print("Columns:\nEnter FIRST_NAME for customer first name\nEnter MIDDLE_NAME for customer middle name\nEnter LAST_NAME for customer last name\nEnter FULL_STREET_ADDRESS for customer full street address\nEnter CREDIT_CARD_NO for credit card number\nEnter CUST_CITY for customer city\nEnter CUST_STATE for customer state\nEnter CUST_COUNTRY for customer country\nEnter CUST_ZIP for customer zip code\nEnter CUST_EMAIL for customer email\nEnter CUST_PHONE for customer phone\nIf you would like to go back to main menu, write 'Menu'.\n")
        column = input("Which column would you like to modify? ")
        if column.upper() in ["FIRST_NAME", "MIDDLE_NAME", "LAST_NAME", "FULL_STREET_ADDRESS", "CREDIT_CARD_NO", "CUST_CITY", "CUST_STATE", "CUST_COUNTRY", "CUST_ZIP", "CUST_EMAIL", "CUST_PHONE"]:
            break
        elif column.lower() == 'menu':
            #GO BACK TO MAIN MENU
            print("\nGoing back to main menu...\n\n")
            return main_menu.main()
        else: 
            print("Not a valid input. Please re-enter. ")
            continue

    #Column Check: validate     
    while True:
        column_check = input(f"You entered {column}. Would you like to modify {column}? Write 'Yes' or 'No'. \nIf you would like to go back to main menu, write 'Menu'. ")
        if column_check.lower() == 'yes':
            break
        elif column_check.lower() == 'no':
            print(f"{column} will not be modified. Going back to main menu...\n\n")
            return main_menu.main()
        elif column_check.lower() == "menu":
            #GO BACK TO MAIN MENU
            print("\nGoing back to main menu...\n\n")
            return main_menu.main()
        else:
            print("Not a valid option.")
            #GO BACK TO MAIN MENU
            print("\nGoing back to main menu...\n\n")
            return main_menu.main()

    #New Value: allow user input and validate        
    while True:
        new_value = input(f"Enter the new value for {column}. If you would like to go back to main menu, write 'Menu'. ")
        if new_value.lower() == "menu":
            #GO BACK TO MAIN MENU
            print("\nGoing back to main menu...\n\n")
            return main_menu.main()
        new_value_check = input(f"You entered {new_value}. Would you like {column} to be modified as {new_value}? Write 'Yes' or 'No'. If you would like to go back to main menu, write 'Menu'. ")
        if new_value_check.lower() == 'yes':
            break
        elif new_value_check.lower() == 'no':
            print("Please re-enter.")
            continue
        elif new_value_check.lower() == 'menu':
            #GO BACK TO MAIN MENU
            print("\nGoing back to main menu...\n\n")
            return main_menu.main()
        else:
            print("Not a valid input. Please try again. ")
            #GO BACK TO MAIN MENU
            print("\nGoing back to main menu...\n\n")
            return main_menu.main()

    #Change value
    while True: 
        try:
            with connection.cursor() as cursor:
                query = "UPDATE CDW_SAPP_CUSTOMER SET %s = %s WHERE SSN = %s;"
                cursor.execute(query, connection, params=(column, new_value, SSN))
                connection.commit()
                print(f"Successfully updated {column} for Customer SSN {SSN} to {new_value}.")
        except Exception as e:
            print(f"Error updating the database: {e}")
        finally:
            connection.close()
            #GO BACK TO MAIN MENU
            print("\nGoing back to main menu...\n\n")
            return main_menu.main()


def generate_monthly_bill():
    connection = connect_to_db()

    #Card No: allow user input and validate
    while True:
        CREDIT_CARD_NO = input("Enter credit card number. If you would like to go back to main menu, write 'Menu'. ")
        if CREDIT_CARD_NO.isdigit() and len(CREDIT_CARD_NO) == 16:
            break
        elif CREDIT_CARD_NO.lower() == 'menu':
            #GO BACK TO MAIN MENU
            print("\nGoing back to main menu...\n\n")
            return main_menu.main()
        else:
            print('Invalid format. Please re-enter as XXXXXXXXXXXXXXXX (16 digits).')

    #Dates: allow user input and validate
    while True:
        year = input("Enter year (YYYY): ")
        if len(year) != 4 or not year.isdigit():
            print("Not a valid format.")
            #GO BACK TO MAIN MENU
            print("\nGoing back to main menu...\n\n")
            return main_menu.main()
        month = input("Enter month (01-12). Write a 0 in front if a single-digit month, e.g. 01 for January. ")
        if len(month) != 2 or not month.isdigit() or int(month) > 12:
            print("Not a valid format.")
            #GO BACK TO MAIN MENU
            print("\nGoing back to main menu...\n\n")
            return main_menu.main()
        year_mo = year+month+"%"
        date_check = input(f"Is {month}/{year} the correct month and year you are looking for? Write 'Yes' or 'No'. \nIf you would like to go to main menu, write 'Menu'. ")
        if date_check.lower() == 'yes':
            break
        elif date_check.lower() == 'no':
            print("Let's try re-entering the dates. ")
        elif date_check.lower() == 'menu':
            #GO BACK TO MAIN MENU
            print("\nGoing back to main menu...\n\n")
            return main_menu.main()
        else:
            print("Invalid input. Please try again. ")
            #GO BACK TO MAIN MENU
            print("\nGoing back to main menu...\n\n")
            return main_menu.main()
        
    while True:
        try:
            query = """
            SELECT SUM(TRANSACTION_VALUE) AS monthly_bill
            FROM CDW_SAPP_CREDIT_CARD
            WHERE CREDIT_CARD_NO = %s
            AND TIMEID LIKE %s;
            """
            df = pd.read_sql(query, connection, params=(CREDIT_CARD_NO, year_mo))
            if not df.empty:
                if df.iat[0, 0] == None:
                    print(f"\nNo transactions found for credit card {CREDIT_CARD_NO} for {year}-{int(month):02d}")
                else: 
                    print(f"\nMonthly bill for credit card {CREDIT_CARD_NO} for {year}-{int(month):02d}: ${df.iat[0, 0]}")
                    print(tabulate(df, headers='keys', tablefmt='psql'))
                    try:
                        query = """
                        SELECT TRANSACTION_VALUE, TRANSACTION_TYPE, TRANSACTION_ID, TIMEID
                        FROM CDW_SAPP_CREDIT_CARD
                        WHERE CREDIT_CARD_NO = %s
                        AND TIMEID LIKE %s;
                        """
                        df_separate_columns = pd.read_sql(query, connection, params=(CREDIT_CARD_NO, year_mo))
                        print(tabulate(df_separate_columns, headers='keys', tablefmt='psql'))
                    except Exception as e:
                        print(f"Error querying the database: {e}")
            else:
                print(f"\nNo transactions found for credit card {CREDIT_CARD_NO} for {year}-{int(month):02d}")
        except Exception as e:
            print(f"Error querying the database: {e}")
        finally:
            connection.close()
            #GO BACK TO MAIN MENU
            print("\nGoing back to main menu...\n\n")
            return main_menu.main()


def display_transactions_between_dates():
    connection = connect_to_db()

    #SSN: allow user input and validate
    while True:
        SSN = input("Enter customer's SSN. If you would like to return to main menu, write 'Menu'. ")
        if SSN.isdigit() and len(SSN) == 9:
            break
        elif SSN.lower() == 'menu':
            #GO BACK TO MAIN MENU
            print("\nGoing back to main menu...\n\n")
            main_menu.main()
        else:
            print("Invalid SSN format. Please enter as XXXXXXXXX (9 digits). ")
    
    #start date: allow user input and validate
    while True: 
        start_date = input("Enter start date (YYYYMMDD). If you would like to return to main menu, write 'Menu'. ")
        if start_date.lower() == 'menu':
            #GO BACK TO MAIN MENU
            print("\nGoing back to main menu...\n\n")
            main_menu.main()
        elif start_date.isdigit() and len(start_date) == 8 and start_date.startswith("20"):
            break
            # if datetime.strptime(start_date, '%Y%m%d') is True:
            #     break
            # else:
            #     print("Invalid date. Please enter as (YYYYMMDD).")
        else:
            print("Invalid date format. Please enter as (YYYYMMDD). ")

    #end date: allow user input and validate
    while True:
        end_date = input("Enter end date (YYYYMMDD). If you would like to return to main menu, write 'Menu'. ")
        if end_date.lower() == 'menu':
            #GO BACK TO MAIN MENU
            print("\nGoing back to main menu...\n\n")
            main_menu.main()
        elif end_date.isdigit() and len(end_date) == 8 and end_date.startswith("20"):
            break
            # if datetime.strptime(end_date, '%Y%m%d') is True:
            #     break
        else:
            print("Invalid date format. Please enter as (YYYYMMDD). ")

    try:
        query = """
        SELECT TIMEID, TRANSACTION_ID, TRANSACTION_TYPE, TRANSACTION_VALUE FROM CDW_SAPP_CREDIT_CARD
        WHERE CUST_SSN = %s
        AND TIMEID BETWEEN %s AND %s
        ORDER BY TIMEID DESC;
        """
        df = pd.read_sql(query, connection, params=(SSN, start_date, end_date))
        if not df.empty:
            print(f"\nTransactions for SSN {SSN} between {start_date} and {end_date}:")
            #print(df)
            print(tabulate(df, headers='keys', tablefmt='psql'))
        else:
            print(f"\nNo transactions found for SSN {SSN} between {start_date} and {end_date}")
    except Exception as e:
        print(f"\nError querying the database: {e}")
    finally:
        connection.close()
        #GO BACK TO MAIN MENU
        print("\nGoing back to main menu...\n\n")
        return main_menu.main()