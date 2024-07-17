import mysql.connector as mydbconnection
from mysql.connector import Error

try:
    conn = mydbconnection.connect(database='usersdb', user='root',password='password', port='3306')

    mySql_insert_query = """INSERT INTO Laptop (Id, Name, Price, Purchase_date) 
                           VALUES 
                           (15, 'Lenovo ThinkPad P71', 6459, '2019-08-14') """

    cursor = conn.cursor()
    cursor.execute(mySql_insert_query)
    conn.commit()
    print(cursor.rowcount, "Record inserted successfully into Laptop table")
    cursor.close()

except Error as e:
    print("Failed to insert record into Laptop table {}".format(error))

finally:
   if conn.is_connected():
    conn.close()
    print("MySQL connection is closed")
