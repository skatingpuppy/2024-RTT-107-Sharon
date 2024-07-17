create if not exists database RegistrationDB

use RegistrationDB

def generate_user_table():
    connect(username = "root",
            password = "password")
    curr = connect.cursor

    query = "CREATE TABLE `user` (`email` varchar(100) NOT NULL,\
  `Name` varchar(50) NOT NULL,\
  `Password` varchar(30) NOT NULL)"
    cursor.execute(myquery2)
    print("Table is created")
        insert into Name
        values(email, Name, Password)

    curr.execute(query)
    curr.close()


def get_all_users():
    connect(username = "root",
            password = "password")
    curr = connect.cursor
    
    query_A = ("""
               select * FROM tablename
               """)
    curr.execute(query_A)
    ALL_records = curr.fetchall()
    
    for i in thing:
         print(thing[stuff])

#use slide 9 in slide deck


def get_user_by_name(name):
    connect(username = "root",
            password = "password")
    curr = connect.cursor


def validate_user(email, password):
    connect(username = "root",
            password = "password")
    curr = connect.cursor
     

def update_user(email, name, password):
     


        
