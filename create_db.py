# create_db.py
import mysql.connector
import os

mysql_pwd = os.environ.get("MYSQL_PASSWORD")

# Connect to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=mysql_pwd,
    database="user_data"
)

# Create a database
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS user_data")

# Create a table
mycursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), email VARCHAR(255))")
