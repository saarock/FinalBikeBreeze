import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password= 'Aayush888999',
    database = 'BIKE'
)
    

cur_sor = mydb.cursor()
