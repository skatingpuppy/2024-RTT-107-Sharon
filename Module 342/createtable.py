import mysql.connector as mydbconnection
from mysql.connector import Error
try:
	conn = mydbconnection.connect(database='usersdb', user='root',password='password', port ='3306')
	cursor=conn.cursor()
	myquery2 = "CREATE TABLE `laptop` (`Id` int(11) NOT NULL,\
  `Name` varchar(250) NOT NULL,\
  `Price` float NOT NULL,\
  `Purchase_date` date NOT NULL)"
	cursor.execute(myquery2)
	print("Table is created")
except Error as e:
    print("Failed tocreate table {}".format(e))
finally:
   if conn.is_connected():
    conn.close()
    print("MySQL connection is closed")
