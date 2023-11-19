# Install Mysql on your computer
# https://dev.mysql.com/downloads/installer/
# pip install mysql
# pip*install*mysql-connector
# pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Cottonwood8690!',

    )

# prepare a cursor object
cursorObject = dataBase.cursor()

#create a database
cursorObject.execute("CREATE DATABASE doyles")

print("ALL DONE!")