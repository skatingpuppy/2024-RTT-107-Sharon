#Sharon Kim GLAB 342.3.3

import requests #pip installed
import mysql.connector as dbconnect

# Function to fetch data from the API endpoint
def fetch_posts():
    url = 'https://jsonplaceholder.typicode.com/posts/'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None

# Function to load data into MySQL database
def load_to_mysql(data):
    try:
        # Connect to MySQL
        conn = dbconnect.connect(
            host='localhost',
            port='3306',
            user='root',
            password='password',
            database='classicmodels'  # Database name
        )
        cursor = conn.cursor()
        # Create table if not exists
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS posts (
                id INT PRIMARY KEY,
                userId INT,
                title VARCHAR(255),
                body TEXT
            )
        ''')
        # Insert data into the table
        for post in data:
            cursor.execute('''
                INSERT INTO posts (id, userId, title, body)
                VALUES (%s, %s, %s, %s)
            ''', (post['id'], post['userId'], post['title'], post['body']))

        # Commit changes and close connection
        conn.commit()
        cursor.close()
        conn.close()
        print("Data loaded successfully to MySQL database.")
    except Exception as e:
        print(f"Error: {e}")

# Function to show data from SQL
def fetch_from_mysql():
    try:
        myconnection = dbconnect.connect(host='localhost',database='classicmodels',user='root',password='password', port='3306')
        if myconnection.is_connected():
            print('Successfully Connected to MySQL database')
            cursor = myconnection.cursor()
            SQLQuery ="SELECT * FROM posts";
            cursor.execute(SQLQuery)
            # get all records
            records = cursor.fetchall()   
            print("Total number of rows in table: ", cursor.rowcount)    
            print("\nPrinting each row")
            for row in records:
                print("order number = ", row[0],  )
                print("item counts = ", row[1])
                print("total  = ", row[2], "\n" )
    except Error as e:
            print("Error while connecting to Database", e)
    finally:
            if myconnection.is_connected():
                cursor.close()
                myconnection.close()
            print("Database connection is closed")

# Fetch data from the API
posts_data = fetch_posts()

# If data is fetched successfully, load it into MySQL database
if posts_data:
    load_to_mysql(posts_data)
    fetch_from_mysql()