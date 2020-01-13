import os
import pymysql

#get username 
username = os.getenv ("root")

#connect to the database

connection = pymysql.connect(db='chinook', user='root', passwd='plyn1985', host='localhost', port=3306)

try:
    # Run a query
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist LIMIT 5;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
   
    connection.close()