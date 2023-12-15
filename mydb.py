#Install MySql on computer
#pip install mysql
#pip install mysql-connerctor
#pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '@Maliseli027'
)

#prepare a cursor object
cursorObject = dataBase.cursor()

#create a database
cursorObject.execute("CREATE DATABASE dcrm_db")

print("All Done!")