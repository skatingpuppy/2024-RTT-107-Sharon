import mysql.connector as mydbconnection
from mysql.connector import Error

def connect():
    """ Connect to MySQL database """
    conn = None
    try:
        conn = mydbconnection.connect(database='classicmodels',
                                             user='root',
                                             password='password')
        if conn.is_connected():
            print('Connected to MySQL database')

    except Error as e:
        print(e)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()


if __name__ == '__main__':
    connect()
